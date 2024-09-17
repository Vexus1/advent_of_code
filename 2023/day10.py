from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class PipeMaze:
    data: list[str]

    def __post_init__(self):
        self.char_map = self.create_char_map()
        self.maze, self.graph, self.start = self.parse_data()
        self.border = self.DFS()

    def create_char_map(self) -> dict[str, tuple[complex, ...]]:
        N, S, E, W = -1j, 1j, 1, -1
        map = {'|': (N, S), '-': (E, W), 'L': (N, E),
            'J': (N, W), '7': (S, W), 'F': (S, E),
            'S': (N, E, S, W), '.':()}
        return map

    def parse_data(self) -> tuple[dict[complex, str],
                                  dict[complex, set[complex]], complex]:
        maze = dict()
        graph = dict()
        for y, row in enumerate(self.data):
            for x, col in enumerate(row):
                pos = complex(x, y)
                maze[pos] = col
                directions = set()
                for dir in self.char_map[col]:
                    directions.add(pos + dir)
                graph[pos] = directions
                if col == 'S':
                    start = pos
        return maze, graph, start
    
    def DFS(self) -> set[complex]:
        seen = {self.start}
        stack = set(self.graph[self.start])
        while stack:
            node = stack.pop()
            seen |= {node}
            stack |= self.graph[node] - seen
        return seen
    
    def irange(self, n: complex) -> list[complex]:
        return [complex(i, n.imag) for i in range(int(n.real))]
    
    def count_enclosed_tiles(self) -> int:
        enclosed_count = 0
        for p in (set(self.maze) - self.border):
            boundary_crossings = sum(self.maze.get(m, '') in "|JL" and 
                                     m in self.border for m in self.irange(p))
            if boundary_crossings % 2 == 1:
                enclosed_count += 1
        return enclosed_count
        
    @property
    def part_one_sol(self) -> int:
        return len(self.border) // 2

    @property
    def part_two_sol(self) -> int:
        return self.count_enclosed_tiles()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day10_test.txt'
    PATH = 'inputs/day10.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    pipe_maze = PipeMaze(data.split('\n'))
    ic(pipe_maze.part_one_sol)
    ic(pipe_maze.part_two_sol)
