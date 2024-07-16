from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class LensLibrary:
    data: str

    def __post_init__(self):
        self.data = self.parse_data(self.data)

    def parse_data(self, data: str) -> list[str]:
        return data.split(',')
    
    def find_hash(self, string: str) -> int:
        value = 0
        for char in string:
            value += ord(char)
            value *= 17
            value %= 256
        return value
    
    def sum_values(self, data: list[str]) -> int:
        return sum(self.find_hash(string) for string in data)

    def part_one_sol(self) -> int:
        return self.sum_values(self.data)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day15_test.txt'
    PATH = 'inputs/day15.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    lens_library = LensLibrary(data)
    ic(lens_library.part_one_sol())
