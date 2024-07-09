from dataclasses import dataclass
import os
from collections import defaultdict

import pandas as pd
from pandas import DataFrame
from icecream import ic

os.chdir(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class ScratchcardsOne:
    data: DataFrame

    def __post_init__(self):
        self.part_one = 0
        self.part_two = defaultdict(int)
        self.calc_points()

    def calc_points(self) -> tuple[int, int]:
        data = self.data.to_numpy()
        for i, line in enumerate(data):
            self.part_two[i] += 1
            win, our = line[0].split('|')
            _, win_clear = win.split(':')
            win_nums = [int(n) for n in win_clear.split()]
            our_nums = [int(n) for n in our.split()]
            val = len(set(win_nums) & set(our_nums))
            if val > 0:
                self.part_one += 2**(val-1)
            for j in range(val):
                self.part_two[i+1+j] += self.part_two[i]

    def sol_one(self) -> int:
        return self.part_one
    
    def sol_two(self) -> int:
        self.part_two = sum(self.part_two.values())
        return self.part_two


if __name__ == '__main__':
    data = pd.read_csv('inputs/day4.csv', header=None)
    # data = pd.read_csv('inputs/day4_test.csv', header=None)
    scratchcards_one = ScratchcardsOne(data)
    ic(scratchcards_one.sol_one())
    ic(scratchcards_one.sol_two())
