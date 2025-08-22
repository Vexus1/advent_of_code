import os
from dataclasses import dataclass
from collections.abc import Callable

from icecream import ic  # type: ignore

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
    
    def neighbors(self, pos: complex) -> list[complex]:
        num = self.grid[pos]
        target = num + 1
        out = []
        for dir in DIRS:
            next = pos + dir
            if self.grid.get(next, -1) == target:
                out.append(next)
        return out
    
    def DFS_post_order(self, pos: complex) -> int:
        count = {}
        children = {}
        stack = [(pos, 0)]
        while stack:
            pos, idx = stack[-1]
            if self.grid[pos] == 9:
                count[pos] = 1
                stack.pop()
                continue
            if pos not in children:
                children[pos] = self.neighbors(pos)
            neigh = children[pos]
            if idx < len(neigh):
                next = neigh[idx]
                stack[-1] = (pos, idx + 1)
                if next not in count:
                    stack.append((next, 0))
            else:
                total = 0
                for n in neigh:
                    total += count.get(n, 0)
                count[pos] = total
                stack.pop()
        return count.get(pos, 0)
    
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
        return self.count_trailheads(self.DFS_post_order)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day10_test.txt'
    PATH = 'inputs/day10.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    hoof_it = HoofIT(data)
    ic(hoof_it.part_one)
    ic(hoof_it.part_two)
