from dataclasses import dataclass
from math import e
import os
import re

from icecream import ic  # type: ignore

@dataclass
class Fertilizer:
    data: list[str]

    def __post_init__(self):
        self.seeds = self.seed_list()

    def seed_list(self) -> list[int]:
        seeds = re.findall(r'\d+', self.data[0])
        seeds = list(map(int, seeds))
        return seeds
    
    def find_location(self, seed) -> int:
        for row in self.data[1:]:
            for conv in re.findall(r'(\d+) (\d+) (\d+)', row):
                stop, start, dt = map(int, conv)
                if seed in range(start, start + dt):
                    seed += stop - start
                    break
        return seed

    def min_location(self, seeds: list[int]) -> int:
        min_loc = float('inf')
        for seed in seeds:
            min_loc = min(min_loc, self.find_location(seed))
        return int(min_loc)

    def find_intervals(self) -> list[tuple[int, int, int]]:
        intervals = []
        for seed in re.findall(r'(\d+) (\d+)', self.data[0]):
            x1, dx = map(int, seed)
            x2 = x1 + dx
            intervals.append((x1, x2, 1))
        return intervals
    
    def lowest_location_number(self) -> int:
        intervals = self.find_intervals()
        min_loc = float('inf')
        while intervals:
            x1, x2, level = intervals.pop()
            if level == 8:
                min_loc = min(x1, min_loc)
                continue
            for conv in re.findall(r'(\d+) (\d+) (\d+)', self.data[level]):
                z, y1, dy = map(int, conv)
                y2 = y1 + dy
                diff = z - y1
                if x2 <= y1 or y2 <= x1:
                    continue
                if x1 < y1:
                    intervals.append((x1, y1, level))
                    x1 = y1
                if y2 < x2:
                    intervals.append((y2, x2, level))
                    x2 = y2
                intervals.append((x1 + diff, x2 + diff, level + 1))
                break
            else:
                intervals.append((x1, x2, level + 1))
        return int(min_loc)
    
    @property
    def part_one_sol(self) -> int:
        return self.min_location(self.seeds)

    @property
    def part_two_sol(self) -> int:
        return self.lowest_location_number()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day05_test.txt'
    PATH = 'inputs/day05.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    fertilizer = Fertilizer(data.split('\n\n'))
    ic(fertilizer.part_one_sol)
    ic(fertilizer.part_two_sol)
