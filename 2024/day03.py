import os 
from dataclasses import dataclass
import re

from icecream import ic # type: ignore

@dataclass
class MullItOver:
    data: list[str]

    def parse_data(self) -> list[list[str]]:
        return [re.findall(r'mul\((\d+,\d+)\)', memory) for memory in self.data]
    
    def mult_result(self) -> int:
        instructions = self.parse_data()
        result = 0
        for instr in instructions:
            for word in instr:
                num1, num2 = word.split(',')
                result += int(num1) * int(num2)
        return result


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day03_test.txt'
    PATH = 'inputs/day03.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    mull_it_over = MullItOver(data.split('\n'))
    ic(mull_it_over.mult_result())
