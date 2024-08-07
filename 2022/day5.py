from dataclasses import dataclass
import os
import re
from typing import Iterator

from icecream import ic

@dataclass
class SupplyStacks:
    _data: str

    def __post_init__(self):
        self.crates, self.procedures = self.divide_data

    @property
    def divide_data(self) -> tuple[list[str], list[str]]:
        empty_index = self._data.index('')
        crates, procedures = self._data[:empty_index], self._data[empty_index+1:]
        return crates, procedures
    
    def rotate(self, matrix: list[str]) -> Iterator[str]:
        return map(''.join, zip(*matrix[::-1]))
    
    def parse_crates(self, crates: list[str]) -> list[list[str]]:
        stacks_of_crates = []
        for stack in self.rotate(crates):
            new_stack = []
            for char in stack:
                if char.isupper():
                    new_stack.append(char)
            if new_stack:
                stacks_of_crates.append(new_stack)
        return stacks_of_crates
    
    def parse_procedures(self, procedures: list[str]) -> list[list[int]]:
        new_procedures = []
        for procedure in procedures:
            nums = re.findall(r'(\d+)', procedure)
            nums = list(map(int, nums))
            new_procedures.append(nums)
        return new_procedures
    
    def find_message(self) -> str:
        stacks_of_crates = self.parse_crates(self.crates)
        procedures = self.parse_procedures(self.procedures)
        for procedure in procedures:
            for _ in range(procedure[0]):
                crate = stacks_of_crates[procedure[1]-1].pop()
                stacks_of_crates[procedure[2]-1].append(crate)
        messege = ''
        for stack in stacks_of_crates:
            messege += stack[-1]
        return messege

    @property
    def part_one_sol(self) -> int:
        return self.find_message()
    
    @property
    def part_two_sol(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day5_test.txt'
    PATH = 'inputs/day5.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    supply_stacks = SupplyStacks(data.split('\n'))
    ic(supply_stacks.part_one_sol)
    ic(supply_stacks.part_two_sol)
