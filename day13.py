from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class PointOfIncidence:
    data: list[str]

    def __post_init__(self):
        self.data = self.create_grids(self.data)

    def transpose(self, 
                  matrix: list[list[str | int]]) -> list[list[str | int]]:
        return [*zip(*matrix)]

    def create_grids(self, data: list[str]) -> list[list[str]]:
        grids = [[]]
        for string in data:
            if string == '':
                grids.append([])
                continue
            grids[-1].append(string)
        return grids

    def summarizing_notes(self, grids: list[list[str]]) -> int:
        result = 0
        for pattern in grids:
            horizontal = self.find_perfect_reflection(pattern)
            vertical = self.find_perfect_reflection(self.transpose(pattern))
            if horizontal != 0:
                result += 100*horizontal
            if vertical != 0:
                result += vertical
        return result

    def find_perfect_reflection(self, pattern: list[str]) -> int:
        for i in range(1, len(pattern)):
            left = pattern[i-1::-1]
            right = pattern[i:]
            diff = [l != r for l, r in zip(left, right)]
            if sum(diff) == 0:
                return i 
        return 0
    
    def part_one_sol(self) -> int:
        return self.summarizing_notes(self.data)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day13_test.txt'
    # PATH = 'inputs/day13.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    point_of_incidence = PointOfIncidence(data.split('\n'))
    ic(point_of_incidence.part_one_sol())
