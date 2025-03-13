import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class RedNosedReports:
    data: list[str]

    def parse_line(self, line: str) -> list[int]:
        return list(map(int, line.split(' ')))

    def count_safe(self) -> int:
        result = 0
        for line in self.data:
            line = self.parse_line(line)
            result += self.is_safe(line)
        return result

    def is_safe(self, line: list[int]) -> bool:
        diff_line = {line[i] - line[i+1] for i in range(len(line)-1)}
        return diff_line <= {1, 2, 3} or diff_line <= {-1, -2, -3}

    @property
    def part_one_sol(self) -> int:
        return self.count_safe()
    
    @property
    def part_two_sol(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day02_test.txt'
    PATH = 'inputs/day02.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    red_nosed_reports = RedNosedReports(data.split('\n'))
    ic(red_nosed_reports.part_one_sol)
    ic(red_nosed_reports.part_two_sol)
