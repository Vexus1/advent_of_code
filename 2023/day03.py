import os 
from dataclasses import dataclass
import re
from functools import reduce
from collections.abc import Iterable
from operator import mul
from collections import defaultdict

from icecream import ic  #type: ignore  

@dataclass
class GearRatios:
    data: list[str]

    def __post_init__(self):
        self.engine_parts, self.gears = self.count_engine_parts()

    def prod(self, iterable: Iterable[int]) -> int:
        return reduce(mul, iterable, 1)
    
    def localize_symbols(self) -> dict[tuple[int, int], str]:
        symbols = dict()
        for y, line in enumerate(self.data):
            for x, char in enumerate(line):
                if char not in '0123456789.':
                    symbols[(x, y)] = char
        return symbols
    
    def count_engine_parts(self) -> tuple[int, defaultdict[tuple[int, int],
                                                           list[int]]]:
        gears = defaultdict(list)
        engine_parts = 0
        symbols = self.localize_symbols()
        for i, line in enumerate(self.data):
            for match in re.finditer(r'\d+', line):
                for (x, y), char in symbols.items():
                    if (match.start() - 1 <= x <= match.end() and
                        i - 1 <= y <= i + 1):
                        n = int(match.group())
                        engine_parts += n
                        if char == '*':
                            gears[(x, y)].append(n)
        return engine_parts, gears

    @property
    def part_one_sol(self) -> int:
        return self.engine_parts
    
    @property
    def part_two_sol(self) -> int:
        result = 0
        for values in self.gears.values():
            if len(values) == 2:
                result += self.prod(values)
        return result


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day03_test.txt'
    PATH = 'inputs/day03.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    gear_ratios = GearRatios(data.split('\n'))
    ic(gear_ratios.part_one_sol)
    ic(gear_ratios.part_two_sol)
