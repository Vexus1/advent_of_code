from dataclasses import dataclass
import os
from collections import defaultdict
import re

from icecream import ic

@dataclass
class LensLibrary:
    _data: str

    @property
    def data(self) -> list[str]:
        return self._data.split(',')
    
    def find_hash(self, string: str) -> int:
        value = 0
        for char in string:
            value += ord(char)
            value = (value*17)%256
        return value
    
    def sum_values(self, data: list[str]) -> int:
        return sum(map(self.find_hash, data))
    
    def box_contents(self, string: str) -> tuple[str]:
        '''
            re.search(r'(\w+)([-=]{1})(\d*)',string): \n
            \\w+ - search words more than one, \n
            [-=]{1} - search operations (-,=) exacly one, \n
            \\d* - search integers none or more
        '''
        contents = re.search(r'(\w+)([-=]{1})(\d*)',string)
        return contents.groups()

    def create_boxes_dict(self, data: list[str]) -> dict[int, dict[str, int]]:
        boxes_dict = defaultdict(dict)
        for string in data:
            label, operation, focal_length = self.box_contents(string)
            box = self.find_hash(label)
            if operation == '=':
                boxes_dict[box][label] = int(focal_length)
            else:
                boxes_dict[box].pop(label, None)
        return boxes_dict
    
    def total_focusing_power(self, boxes_dict: dict[int, dict[str, int]]) -> int:
        focus_power = 0
        for box, lenses in boxes_dict.items():
            for i, (_, focal_power) in enumerate(lenses.items()):
                focus_power += (box + 1) * (i + 1) * focal_power
        return focus_power
        
    def part_one_sol(self) -> int:
        return self.sum_values(self.data)
    
    def part_two_sol(self) -> int:
        boxes_dict = self.create_boxes_dict(self.data)
        return self.total_focusing_power(boxes_dict)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day15_test.txt'
    PATH = 'inputs/day15.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    lens_library = LensLibrary(data)
    ic(lens_library.part_one_sol())
    ic(lens_library.part_two_sol())
