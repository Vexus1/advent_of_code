from dataclasses import dataclass
import os
import re
import math as mt

from icecream import ic

@dataclass
class Fertilizer:
    data: str

    def __post_init__(self):
        self.data = data.split('\n\n')
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

    def min_location(self, seeds) -> list[int]:
        min_loc = float('inf')
        for seed in seeds:
            min_loc = min(min_loc, self.find_location(seed))
        return min_loc
    
    def modify_seeds_dat(self, seed) -> list[int]:
        # new_seeds = []
        min_loc = float('inf')
        for i in range(len(seed)//2):
            start = seed[i*2]
            dt = seed[(i+1)*2-1]-1
            stop = start + dt
            for new_seed in range(start, stop, 100):
                min_loc = min(min_loc, self.find_location(new_seed))
        return min_loc
    
    def part_one_sol(self) -> int:
        return self.min_location(self.seeds)

    def part_two_sol(self) -> int:
        seeds = self.modify_seeds_dat(self.seeds)
        # return self.min_location(seeds)
        return seeds

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # with open('inputs/day5_test.csv', 'r') as f:
    with open('inputs/day5.csv', 'r') as f:
        data = f.read()
    fertilizer = Fertilizer(data)
    ic(fertilizer.part_one_sol())
    # ic(fertilizer.part_two_sol())
