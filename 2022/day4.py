from dataclasses import dataclass
import os
import re

from icecream import ic

@dataclass
class CampCleanup:
    _data: str

    def create_section_set(self, section: str) -> tuple[set[int], set[int]]:
        ranges = re.findall(r'(\d+)', section)
        ranges = map(int, ranges)
        min1, max1, min2, max2 = ranges
        section_one = set(range(min1, max1 + 1))
        section_two = set(range(min2, max2 + 1))
        return section_one, section_two

    def count_fully_contains(self) -> int:
        counter = 0
        for section in self._data:
            section_one, section_two = self.create_section_set(section)
            if (section_one.issubset(section_two) or
                section_two.issubset(section_one)):
                counter += 1
        return counter
    
    def count_overlap_parts(self) -> int:
        counter = 0
        for section in self._data:
            section_one, section_two = self.create_section_set(section)
            if section_one & section_two:
                counter += 1
        return counter

    @property
    def part_one_sol(self) -> int:
        return self.count_fully_contains()
    
    @property
    def part_two_sol(self) -> int:
        return self.count_overlap_parts()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day4_test.txt'
    PATH = 'inputs/day4.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    camp_cleanup = CampCleanup(data.split('\n'))
    ic(camp_cleanup.part_one_sol)
    ic(camp_cleanup.part_two_sol)
