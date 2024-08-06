from dataclasses import dataclass
import os

from numpy import transpose
from icecream import ic

GALAXY = '#'
VOID = '.'

@dataclass
class CosmicExpansion:
    data: list[str]

    def __post_init__(self):
        self.data = self.modify_data()
        self.void = self.find_void()

    def modify_data(self) -> list[list[str]]:
        return [list(row) for row in self.data]
    
    def find_galaxy(self) -> list[tuple[int]]:
        galaxy_cord = []
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                if col == GALAXY:
                    galaxy_cord.append((i, j))
        return galaxy_cord

    def find_void(self) -> tuple[list[int]]:
        row = [i for i, line in enumerate(self.data) if set(line) == set(VOID)]
        col = [i for i, line in enumerate(transpose(self.data)) if set(line) == set(VOID)]
        void = (row, col)
        return void
    
    def manhattan(self, pair_one: tuple[int], pair_two: tuple[int]):
        return abs(pair_one[0] - pair_two[0]) + abs(pair_one[1] - pair_two[1])
    
    def expanse_dimension(self, n: int, pair_one:
                           tuple[int], pair_two: tuple[int]) -> int:
        y_min = min(pair_one[0]+1, pair_two[0])
        y_max = max(pair_one[0]+1, pair_two[0])
        x_min = min(pair_one[1]+1, pair_two[1])
        x_max = max(pair_one[1]+1, pair_two[1])
        row = range(y_min, y_max)
        col = range(x_min, x_max)
        added_path_len = 0
        void_row, void_col = self.void
        for y in row:
            if y in void_row:
                added_path_len += n-1
        for x in col:
            if x in void_col:
                added_path_len += n-1
        return added_path_len
    
    def calc_shorthest_paths(self, n: int) -> int:
        galaxies = self.find_galaxy()
        path_len = 0
        tak = []
        i = 0
        for pair_one in galaxies:
            i += 1
            for j in range(i, len(galaxies)):
                tak.append([pair_one, galaxies[j]])
                pairs = pair_one, galaxies[j]
                manh_len = self.manhattan(*pairs)
                expa_len = self.expanse_dimension(n, *pairs)
                path_len += manh_len + expa_len
        return path_len

    def part_one_sol(self) -> int:
        return self.calc_shorthest_paths(n=2)

    def part_two_sol(self) -> int:
        return self.calc_shorthest_paths(n=1000000)
                

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day11_test.csv'
    PATH = 'inputs/day11.csv'
    with open(PATH, 'r') as f:
        data = f.read()
    cosmic_expansion = CosmicExpansion(data.split('\n'))
    ic(cosmic_expansion.part_one_sol())
    ic(cosmic_expansion.part_two_sol())
