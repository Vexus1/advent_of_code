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
        crates, procedures = [part.split("\n") for part in self._data]
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
    
    def parse_procedures(self, procedures: list[str]) -> list[tuple[int]]:
        '''index: 0 -> count, 1 -> from, 2 -> to'''
        new_procedures = []
        for procedure in procedures:
            nums = re.findall(r'(\d+)', procedure)
            nums = tuple(map(int, nums))
            new_procedures.append(nums)
        return new_procedures
    
    def find_message(self, stacks_of_crates: list[list[str]],
                     procedures: tuple[list[int]], direction: int) -> str:
        for count, fr, to in procedures:
            new_stack = []
            for _ in range(min(len(stacks_of_crates[fr-1]), count)):
                new_stack.append(stacks_of_crates[fr-1].pop())
            stacks_of_crates[to-1].extend(new_stack[::direction])  
        message = ''.join([stack[-1] for stack in stacks_of_crates])
        return message

    @property
    def part_one_sol(self) -> str:
        stacks_of_crates = self.parse_crates(self.crates)
        procedures = self.parse_procedures(self.procedures)
        return self.find_message(stacks_of_crates, procedures, 1)
    
    @property
    def part_two_sol(self) -> int:
        stacks_of_crates = self.parse_crates(self.crates)
        procedures = self.parse_procedures(self.procedures)
        return self.find_message(stacks_of_crates, procedures, -1)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day5_test.txt'
    PATH = 'inputs/day5.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    supply_stacks = SupplyStacks(data.split('\n\n'))
    ic(supply_stacks.part_one_sol)
    ic(supply_stacks.part_two_sol)
