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
        self.part_one, self.part_two = self.total_price()

    def create_grid(self) -> dict[complex, str]:
        grid = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                pos = complex(i, j)
                grid[pos] = col
        return grid
    
    def count_edges(self, region: set[complex]) -> int:
        row_indices = [int(p.real) for p in region]
        col_indices = [int(p.imag) for p in region]
        r_min, r_max = min(row_indices) - 1, max(row_indices) + 1
        c_min, c_max = min(col_indices) - 1, max(col_indices) + 1
        sides = 0
        for row in range(r_min, r_max):
            for col in range(c_min, c_max):
                top_left = complex(row, col) in region
                bottom_left = complex(row+1, col) in region
                top_right = complex(row, col+1) in region
                bottom_right = complex(row+1, col+1) in region
                count = top_left + bottom_left + top_right + bottom_right
                if count == 1 or count == 3:
                    sides += 1
                elif count == 2:
                    if ((top_left and bottom_right) or 
                        (bottom_left and top_right)):
                        sides += 2
        return sides
    
    def bfs(self, pos: complex, char: str) -> tuple[int, int, set[complex]]:
        queue = deque([pos])
        self.visited.add(pos)
        region = set([pos])
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
                    region.add(next)
                    queue.append(next)
        return area, perimeter, region

    def total_price(self) -> tuple[int, int]:
        part_one = 0
        part_two = 0
        for pos, char in self.grid.items():
            if pos not in self.visited:
                area, perimeter, region = self.bfs(pos, char)
                part_one += area * perimeter
                part_two += area * self.count_edges(region)
        return part_one, part_two


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day12_test.txt'
    PATH = 'inputs/day12.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    garden_groups = GardenGroups(data)
    ic(garden_groups.part_one)
    ic(garden_groups.part_two)
