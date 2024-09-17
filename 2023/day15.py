from dataclasses import dataclass
import os
from collections import defaultdict
import re

from icecream import ic  # type: ignore

@dataclass
class LensLibrary:
    data: str
    
    def find_hash(self, string: str) -> int:
        value = 0
        for char in string:
            value += ord(char)
            value = (value*17) % 256
        return value
    
    def sum_values(self) -> int:
        return sum(map(self.find_hash, self.data.split(',')))
    
    def box_contents(self, string: str) -> tuple[str, str, str]:
        match = re.search(r'(\w+)([-=]{1})(\d*)', string)
        assert match is not None, "Pattern not found"
        label, operation, focal_length = match.groups()
        return str(label), str(operation), str(focal_length)

    def create_boxes_dict(self) -> defaultdict[int, dict[str, int]]:
        boxes_dict: defaultdict[int, dict[str, int]] = defaultdict(dict)
        for string in self.data.split(','):
            label, operation, focal_length = self.box_contents(string)  # Poprawka na trzy wartości
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
        
    @property
    def part_one_sol(self) -> int:
        return self.sum_values()
    
    @property
    def part_two_sol(self) -> int:
        boxes_dict = self.create_boxes_dict()
        return self.total_focusing_power(boxes_dict)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day15_test.txt'
    PATH = 'inputs/day15.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    lens_library = LensLibrary(data)
    ic(lens_library.part_one_sol)
    ic(lens_library.part_two_sol)
