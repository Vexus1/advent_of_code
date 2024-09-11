from dataclasses import dataclass
import os
from collections import defaultdict

from icecream import ic  # type: ignore

@dataclass
class Scratchcards:
    data: list[str]

    def __post_init__(self):
        self.part_one = 0
        self.part_two = defaultdict(int)
        self.calc_points()

    def calc_points(self) -> None:
        for i, line in enumerate(self.data):
            self.part_two[i] += 1
            win, our = line.split('|')
            _, win_clear = win.split(':')
            win_nums = [int(n) for n in win_clear.split()]
            our_nums = [int(n) for n in our.split()]
            val = len(set(win_nums) & set(our_nums))
            if val > 0:
                self.part_one += 2**(val-1)
            for j in range(val):
                self.part_two[i+1+j] += self.part_two[i]
        return None

    @property
    def part_one_sol(self) -> int:
        return self.part_one
    
    @property
    def part_two_sol(self) -> int:
        self.part_two = sum(self.part_two.values())
        return self.part_two


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day4_test.txt'
    PATH = 'inputs/day4.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    scratchcards = Scratchcards(data.split('\n'))
    ic(scratchcards.part_one_sol)
    ic(scratchcards.part_two_sol)
