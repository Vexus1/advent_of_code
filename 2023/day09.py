from dataclasses import dataclass
import os
from math import comb
from collections.abc import Callable

from icecream import ic  # type: ignore

@dataclass
class MirageMaintenance:
    data: list[str]

    def lagrange_interpolating1(self, nums: list[int]) -> int:
        result = 0
        len_ = len(nums)
        for i, n in enumerate(nums):
            result += n * comb(len_, i) * (-1) ** (len_ - 1 - i)
        return result
 
    def lagrange_interpolating2(self, nums: list[int]) -> int:
        result = 0
        len_ = len(nums)
        for i, n in enumerate(nums):
            result += n * comb(len_, i + 1) * (-1) ** (i)
        return result

    def sum_each_history(self, func: Callable) -> int:
        result = 0
        for line in self.data:
            result += func(list(map(int, line.split())))
        return result

    @property
    def part_one_sol(self) -> int:
        return self.sum_each_history(self.lagrange_interpolating1)
    
    @property
    def part_two_sol(self) -> int:
        return self.sum_each_history(self.lagrange_interpolating2)
                

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day09_test.txt'
    PATH = 'inputs/day09.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    mirage_maintenance = MirageMaintenance(data.split('\n'))
    ic(mirage_maintenance.part_one_sol)
    ic(mirage_maintenance.part_two_sol)
