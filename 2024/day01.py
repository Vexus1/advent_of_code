import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class HistorianHysteria:
    data: str

    def __post_init__(self):
        self.left, self.right = self.parse_data()

    def parse_data(self) -> tuple[list[int], list[int]]:
        data = [*map(int, self.data.split())]
        left, right = sorted(data[0::2]), sorted(data[1::2])
        return left, right

    def total_distance(self) -> int:
        distance = sum(abs(l - r) for l, r in zip(self.left, self.right))
        return distance 

    @property
    def part_one_sol(self) -> int:
        return self.total_distance()
    
    @property
    def part_two_sol(self) -> int:
        return


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day01_test.txt'
    PATH = 'inputs/day01.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    historian_hysteria = HistorianHysteria(data)
    ic(historian_hysteria.part_one_sol)
    ic(historian_hysteria.part_two_sol)
