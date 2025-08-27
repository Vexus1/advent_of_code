import os
from dataclasses import dataclass
import re

from icecream import ic  # type: ignore

@dataclass
class ClawContraption:
    data: list[str]

    def parse_data(self, line: str) -> tuple[int, int]:
        return tuple(map(int, (re.findall(r'\d+', line))))

    def find_intersections(
        self,
        ax: int, 
        ay: int, 
        bx: int, 
        by: int, 
        px: int, 
        py: int
    ) -> tuple[int, int]:
        delta = ax * by - ay * bx
        a = px * by - py * bx
        b = py * ax - px * ay
        return a // delta, b // delta


    def calc_tokens(self, increase_prize: bool) -> int:
        total = 0
        for i in range(0, len(self.data) - 1, 4):
            ax, ay = self.parse_data(self.data[i])
            bx, by = self.parse_data(self.data[i + 1])
            px, py = self.parse_data(self.data[i + 2])
            if increase_prize:
                px += 10000000000000
                py += 10000000000000
            a, b = self.find_intersections(ax, ay, bx, by, px, py)
            if (a * ax + b * bx == px) and (a * ay + b * by == py):
                total += a * 3 + b
        return int(total)
            
    @property
    def part_one(self) -> int:
        return self.calc_tokens(False)
    
    @property
    def part_two(self) -> int:
        return self.calc_tokens(True)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day13_test.txt'
    PATH = 'inputs/day13.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    claw_contraption = ClawContraption(data)
    ic(claw_contraption.part_one)
    ic(claw_contraption.part_two)
