from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class PointOfIncidence:
    data: list[str]

    def transpose(self, matrix: list[str]) -> list[str]:
        return list(map(''.join, zip(*matrix)))
    
    def slide_rocks_north(self, data: list[str]) -> list[str]:
        data = self.transpose(data)
        for i, line in enumerate(data):
            while ".O" in line:
                line = line.replace(".O", "O.")
            data[i] = line
        return self.transpose(data)
    
    def calc_load(self, data: list[str]) -> int:
        loan = 0
        for i, line in enumerate(data[::-1], 1):
            for char in line:
                loan += i*(char=='O')
        return loan

    def part_one_sol(self) -> int:
        slide_rocks = self.slide_rocks_north(self.data)
        return self.calc_load(slide_rocks)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day14_test.txt'
    PATH = 'inputs/day14.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    point_of_incidence = PointOfIncidence(data.split('\n'))
    ic(point_of_incidence.part_one_sol())
    