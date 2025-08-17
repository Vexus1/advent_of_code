import os 
from dataclasses import dataclass
from typing import Callable

from icecream import ic # type: ignore

@dataclass
class BridgeRepair:
    data: list[str]

    def test(self, test: int, nums: list[int]) -> bool:
        if nums[0] > test:
            return False
        elif len(nums) == 1:
            return nums[0] == test
        elif self.test(test, [nums[0] + nums[1]] + nums[2:]):
            return True
        elif self.test(test, [nums[0] * nums[1]] + nums[2:]):
            return True
        return False
    
    def test_with_concat(self, test: int, nums: list[int]) -> bool:
        if nums[0] > test:
            return False
        elif len(nums) == 1:
            return nums[0] == test
        elif self.test_with_concat(test, [nums[0] + nums[1]] + nums[2:]):
            return True
        elif self.test_with_concat(test, [nums[0] * nums[1]] + nums[2:]):
            return True
        elif self.test_with_concat(test, [int(str(nums[0]) + str(nums[1]))] + nums[2:]):
            return True
        return False

    def total_cal_result(self, test_numbers: Callable[[int, list[int]], bool]) -> int:
        total = 0
        for line in self.data:
            test, nums = line.split(': ')
            test = int(test)
            nums = list(map(int, nums.split(' ')))
            if test_numbers(test, nums):
                total += test        
        return total

    @property
    def part_one(self) -> int:
        return self.total_cal_result(self.test)
    
    @property
    def part_two(self) -> int:
        return self.total_cal_result(self.test_with_concat)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day07_test.txt'
    PATH = 'inputs/day07.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    bridge_repair = BridgeRepair(data)
    ic(bridge_repair.part_one)
    ic(bridge_repair.part_two)
