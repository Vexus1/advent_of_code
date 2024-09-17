from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class PointOfIncidence:
    data: list[str]

    def __post_init__(self):
        self.grid = self.create_grids()

    def transpose(self, matrix: list[str]) -> list[str]:
        return list(map(''.join, zip(*matrix)))

    def create_grids(self) -> list[list[str]]:
        grids: list[list[str]] = [[]]
        for string in self.data:
            if string == '':
                grids.append([])
                continue
            grids[-1].append(string)
        return grids

    def find_reflection(self, pattern: list[str], n: int) -> int:
        for i in range(1, len(pattern)):
            left = pattern[i-1::-1]
            right = pattern[i:]
            diff = 0
            for l, r in zip(left, right):
                for char_l, char_r in zip(l, r):
                    if char_l != char_r:
                        diff += 1
            if diff == n:
                return i
        return 0
    
    def summarizing_notes(self, n: int) -> int:
        result = 0
        for pattern in self.grid:
            horizontal = self.find_reflection(pattern, n)
            vertical = self.find_reflection(self.transpose(pattern), n)
            if horizontal != 0:
                result += 100*horizontal
            if vertical != 0:
                result += vertical
        return result
    
    @property
    def part_one_sol(self) -> int:
        return self.summarizing_notes(n=0)

    @property
    def part_two_sol(self) -> int:
        return self.summarizing_notes(n=1)
        

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day13_test.txt'
    PATH = 'inputs/day13.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    point_of_incidence = PointOfIncidence(data.split('\n'))
    ic(point_of_incidence.part_one_sol)
    ic(point_of_incidence.part_two_sol)
