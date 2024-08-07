from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class RucksackReorganization:
    _data: str

    def map_char(self, char: str) -> int:
        if char.islower():
            priority = ord(char) - 96
        else:
            priority = ord(char) - 64 + 26
        return priority
    
    @property
    def priority_sum(self) -> int:
        result = 0
        for line in self._data:
            half_line_len = len(line) // 2
            first, second = line[:half_line_len], line[half_line_len:]
            result += self.map_char(list(set(first) & set(second))[0])
        return result
    
    @property
    def priority_sum_for_group(self) -> int:
        result = 0
        for i in range(0, len(self._data), 3):
            first = set(self._data[i])
            second = set(self._data[i+1])
            third = set(self._data[i+2])
            result += self.map_char(list(first & second & third)[0])
        return result
            
    @property
    def part_one_sol(self) -> int:
        return self.priority_sum
    
    @property
    def part_two_sol(self) -> int:
        return self.priority_sum_for_group


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day3_test.txt'
    PATH = 'inputs/day3.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    rucksack_reorganization = RucksackReorganization(data.split('\n'))
    ic(rucksack_reorganization.part_one_sol)
    ic(rucksack_reorganization.part_two_sol)