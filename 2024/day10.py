import os
from dataclasses import dataclass
from collections.abc import Callable

from icecream import ic

DIRS = (1, 1j, -1, -1J)

@dataclass
class HoofIT:
    data: list[str]

    def __post_init__(self):
        self.grid = self.create_grid()
    
    def create_grid(self) -> dict[complex, int]:
        grid = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                pos = complex(i, j)
                grid[pos] = int(col)
        return grid
    
    def DFS(self, pos: complex) -> int:
        reached = set()
        seen = set()
        stack = [pos]
        while stack:
            pos = stack.pop()
            if pos in seen:
                continue
            seen.add(pos)
            num = self.grid[pos]
            if num == 9:
                reached.add(pos)
                continue
            target = num + 1
            for dir in DIRS:
                next = pos + dir
                if next in self.grid and self.grid[next] == target:
                    stack.append(next)
        return len(reached)

    def count_trailheads(self, method: Callable[[complex], int]) -> int:
        result = 0
        for pos, num in self.grid.items():
            if num == 0:
                result += method(pos)
        return result

    @property
    def part_one(self) -> int:
        return self.count_trailheads(self.DFS)
    
    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day10_test.txt'
    PATH = 'inputs/day10.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    hoof_it = HoofIT(data)
    ic(hoof_it.part_one)
    ic(hoof_it.part_two)
