import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class CeresSearch:
    data: list[str]

    def __post_init__(self):
        self.grid = self.create_grid()
        self.result1, self.result2 = self.count_words()

    def create_grid(self) -> dict[complex, str]:
        grid = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                position = complex(j, i)
                grid[position] = col
        return grid
    
    def get_word(self, pos: complex) -> str:
        return self.grid.get(pos, '')

    def count_words(self) -> int:
        result1 = 0
        result2 = 0
        for pos, _ in self.grid.items():
            dir: complex
            for dir in [1, 1j, 1+1j, 1-1j, -1, -1j, -1+1j, -1-1j]:
                result1 += (self.get_word(pos) + \
                            self.get_word(pos + dir) + \
                            self.get_word(pos + dir*2) + \
                            self.get_word(pos + dir*3) == 'XMAS')
                if dir.imag and dir.real:
                    result2 += ((self.get_word(pos + dir) + \
                                 self.get_word(pos) + \
                                 self.get_word(pos - dir) == 'MAS') and
                                (self.get_word(pos + dir*1j) + \
                                 self.get_word(pos - dir*1j) == 'MS'))
        return result1, result2

    @property
    def part_one(self) -> int:
        return self.result1
    
    @property
    def part_two(self) -> int:
        return self.result2


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day04_test.txt'
    PATH = 'inputs/day04.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    ceres_search = CeresSearch(data.split('\n'))
    ic(ceres_search.part_one)
    ic(ceres_search.part_two)
