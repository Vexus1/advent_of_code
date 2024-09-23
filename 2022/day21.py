from dataclasses import dataclass
import os
from typing import Any

from icecream import ic  # type: ignore

@dataclass
class MonkeyMath:
    data: list[str]

    def root_number(self) -> int:
        namespace: dict[str, Any] = {}
        finished = False
        for i, line in enumerate(self.data):
            self.data[i] = line.replace(': ', ' = ')
        while not finished:
            finished = True
            for line in self.data:
                try:
                    exec(line, {}, namespace)
                except NameError:
                    finished = False
        return int(namespace.get('root', None))

    @property
    def part_one_sol(self) -> int:
        return self.root_number()
    
    # @property
    # def part_two_sol(self) -> int:
    #     return 
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day21_test.txt' 
    PATH = 'inputs/day21.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    monkey_math = MonkeyMath(data.split('\n'))
    ic(monkey_math.part_one_sol)
    # ic(monkey_math.part_two_sol)
