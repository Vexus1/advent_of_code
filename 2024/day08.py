import os 
from dataclasses import dataclass
from collections import defaultdict
from itertools import combinations
from typing import Iterator

from icecream import ic # type: ignore

@dataclass
class ResonantCollinearity:
    data: list[str]

    def __post_init__(self):
        self.part_one, self.part_two = self.antinode_locations()

    def antenna_location(self) -> defaultdict[str, list[complex]]:
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
    
    def antinode_line(self, start: complex, step: complex) -> Iterator[complex]:
        p = start + step
        while self.is_in_grid(p):
            yield p
            p += step

    def antinode_locations(self) -> tuple[int, int]:
        antenna_loc = self.antenna_location()
        antinodes1, antinodes2 = set(), set()
        for locs in antenna_loc.values():
            for p1, p2 in combinations(locs, 2):
                step = p2 - p1
                for candidate in (p1 - step, p2 + step):
                    if self.is_in_grid(candidate):
                        antinodes1.add(candidate)
                antinodes2.add(p1)
                antinodes2.add(p2)
                for p in self.antinode_line(p1, step):
                    antinodes2.add(p)
                for p in self.antinode_line(p1, -step):
                    antinodes2.add(p)
        return len(antinodes1), len(antinodes2)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day08_test.txt'
    PATH = 'inputs/day08.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    resonant_collinearity = ResonantCollinearity(data)
    ic(resonant_collinearity.part_one)
    ic(resonant_collinearity.part_two)
