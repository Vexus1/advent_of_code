import os
from dataclasses import dataclass
from collections import deque

from icecream import ic  # type: ignore

@dataclass
class GardenGroups:
    data: list[str]

    def __post_init__(self):
        self.grid = self.create_grid()
        self.visited = set()

    def create_grid(self) -> dict[complex, str]:
        grid = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                pos = complex(i, j)
                grid[pos] = col
        return grid

    def bfs(self, pos: complex, char: str) -> int:
        queue = deque([pos])
        self.visited.add(pos)
        area = 0
        perimeter = 0
        while queue:
            pos = queue.popleft()
            area += 1
            for dir in (1, 1j, -1, -1j):
                next = pos + dir
                if next not in self.grid or self.grid[next] != char:
                    perimeter += 1
                elif next not in self.visited:
                    self.visited.add(next)
                    queue.append(next)
        return area * perimeter

    def total_price(self) -> int:
        total = 0
        for pos, char in self.grid.items():
            if pos not in self.visited:
                total += self.bfs(pos, char)
        return total

    @property
    def part_one(self) -> int:
        return self.total_price()
    
    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day12_test.txt'
    PATH = 'inputs/day12.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    garden_groups = GardenGroups(data)
    ic(garden_groups.part_one)
    ic(garden_groups.part_two)
