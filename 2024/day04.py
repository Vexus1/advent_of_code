import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class CeresSearch:
    data: list[str]

    def __post_init__(self):
        self.keyword = 'XMAS'

    def create_grid(self) -> dict[complex, str]:
        grid = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                position = complex(j, i)
                grid[position] = col
        return grid


    def count_words(self) -> int:
        grid = self.create_grid()
        count = 0
        for pos, _ in grid.items():
            for dir in [1, 1j, 1+1j, 1-1j, -1, -1j, -1+1j, -1-1j]:
                try:
                    count += grid[pos] + grid[pos + dir] + \
                    grid[pos + dir*2] + grid[pos + dir*3] == self.keyword
                except:
                    continue
        return count

    @property
    def part_one(self) -> int:
        return self.count_words()
    
    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day04_test.txt'
    PATH = 'inputs/day04.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    ceres_search = CeresSearch(data.split('\n'))
    ic(ceres_search.part_one)
    ic(ceres_search.part_two)
