from dataclasses import dataclass
import os
from collections.abc import Generator
from collections import defaultdict

from icecream import ic  # type: ignore

Edge = tuple[complex, int]
EdgeSet = set[Edge]
Graph = defaultdict[complex, EdgeSet]

@dataclass
class LongWalk:
    data: list[str]

    def __post_init__(self):
        self.board = self.create_board()
        self.height = len(self.data) 
        self.width = len(self.data[0]) 
        self.start_point = self.find_unique_point(0)
        self.end_point = self.find_unique_point(len(self.data)-1)

    def create_board(self) -> dict[complex, str]:
        pos_map = dict()
        for y, row in enumerate(self.data):
            for x, col in enumerate(row):
                pos = complex(x, y)
                pos_map[pos] = col
        return pos_map
    
    def find_unique_point(self, unique_row: int) -> complex:
        unique_x_point = self.data[unique_row].index('.')
        return complex(unique_x_point, unique_row)
       
    def get_neighbours(self, pos: complex) -> Generator[complex]:
        for dir in (-1, 1, -1j, 1j):
            move = pos + dir
            if 0 <= move.real <= self.width and 0 <= move.imag <= self.height:
                if self.board[move] == '.':
                    yield move
                if self.board[move] == '>' and move.real > pos.real:
                    yield move
                if self.board[move] == 'v' and move.imag > pos.imag:
                    yield move

    def neighbours_without_slope(self) -> Graph:
        neighbours = defaultdict(set)
        for pos in self.board:
            if self.board[pos] != '#':
                for dir in (-1, 1, -1j, 1j):
                    move = pos + dir
                    if 0 < move.real < self.width and 0 < move.imag < self.height:
                        if self.board[move] in '.>v':
                            neighbours[pos].add((move, 1))
                            neighbours[move].add((pos, 1))
        return neighbours
        
    def remove_nodes(self, neighbours: Graph) -> Graph:
        while True:
            for node, edge in neighbours.items():
                if len(edge) == 2:
                    first, sec = edge
                    neighbours[first[0]].remove((node, first[1]))
                    neighbours[sec[0]].remove((node, sec[1]))
                    new_node = (complex(sec[0].real, sec[0].imag),
                                first[1] + sec[1])
                    neighbours[first[0]].add(new_node)
                    new_node = (complex(first[0].real, first[0].imag),
                                first[1] + sec[1])
                    neighbours[sec[0]].add(new_node)
                    del neighbours[node]
                    break
            else:
                break
        return neighbours
        
    def DFS_one(self) -> int:
        '''Iterative version'''
        longest_path = 0
        seen: set[complex] = set()
        stack = [(self.start_point, 0)]
        while stack:
            pos, path_len = stack.pop()
            if path_len == -1:
                seen.remove(pos)
                continue
            if pos == self.end_point:
                longest_path = max(longest_path, path_len)
                continue
            if pos in seen:
                continue
            seen.add(pos)
            stack.append((pos, -1))
            for neighbour in self.get_neighbours(pos):
                stack.append((neighbour, path_len + 1))
        return longest_path

    def DFS_two(self) -> int:
        '''Iterative version'''
        neighbours = self.remove_nodes(self.neighbours_without_slope())
        longest_path = 0
        seen: set[complex] = set()
        stack = [(self.start_point, 0)]
        while stack:
            pos, path_len = stack.pop()
            if path_len == -1:
                seen.remove(pos)
                continue
            if pos == self.end_point:
                longest_path = max(longest_path, path_len)
                continue
            if pos in seen:
                continue
            seen.add(pos)
            stack.append((pos, -1))
            for neighbour, _len in neighbours[pos]:
                stack.append((neighbour, path_len + _len))
        return longest_path

    @property
    def part_one_sol(self) -> int:
        return self.DFS_one()

    @property
    def part_two_sol(self) -> int:
        return self.DFS_two()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day23_test.txt'
    PATH = 'inputs/day23.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    long_walk = LongWalk(data.split('\n'))
    ic(long_walk.part_one_sol)
    ic(long_walk.part_two_sol)
