import os 
from dataclasses import dataclass
from collections import defaultdict

from icecream import ic # type: ignore

@dataclass
class ResonantCollinearity:
    data: list[str]

    def antenna_location(self) -> dict[complex, str]:
        loc = defaultdict(list)
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                if col != '.':
                    position = complex(i, j)
                    loc[col].append(position)
        return loc

    def is_in_grid(self, pos: complex) -> bool:
        return (0 <= pos.real < len(self.data[0]) and 
                0 <= pos.imag < len(self.data))
    
    # def find_antinode(self, p1: complex, p2: complex):
        

    def antinode_locations(self) -> int:
        antenna_loc = self.antenna_location()
        antinodes = set()
        for locs in antenna_loc.values():
            for i in range(len(locs)):
                for j in range(i + 1, len(locs)):
                    p1, p2 = locs[i], locs[j]
                    dp = p2 - p1
                    if self.is_in_grid(p1 - dp):
                        antinodes.add(p1 - dp)
                    if self.is_in_grid(p2 + dp):
                        antinodes.add(p2 + dp)
        return len(antinodes)

    @property
    def part_one(self) -> int:
        return self.antinode_locations()
    
    @property
    def part_two(self) -> int:
        return 

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day08_test.txt'
    PATH = 'inputs/day08.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    resonant_collinearity = ResonantCollinearity(data)
    ic(resonant_collinearity.part_one)
    ic(resonant_collinearity.part_two)
