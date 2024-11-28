from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class SonarSweep:
    data: list[str]

    def count_larger_measurements(self, slice: int) -> int:
        data = list(map(int, self.data))
        return sum(x < y for x, y in zip(data, data[slice:]))  

    @property
    def part_one_sol(self) -> int:
        return self.count_larger_measurements(1)
    
    @property
    def part_two_sol(self) -> int:
        return self.count_larger_measurements(3)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day01_test.txt' 
    PATH = 'inputs/day01.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    sonar_sweep = SonarSweep(data.split('\n'))
    ic(sonar_sweep.part_one_sol)
    ic(sonar_sweep.part_two_sol)
