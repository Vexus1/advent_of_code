from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class CathodeRayTube:
    _data: list[str]

    def __post_init__(self):
        self.cycles = [20, 60, 100, 140, 180, 220]
        self.signal_strenght = []

    def update_singal_strenght(self, cycle: int, X: int) -> None:
        if cycle in self.cycles:
            self.signal_strenght.append(cycle*X)

    def execute_program(self) -> None:
        X = 1
        cycle = 0
        for line in self._data:
            line = line.split()
            match line:
                case 'addx', n:
                    cycle += 1
                    self.update_singal_strenght(cycle, X)
                    cycle += 1
                    self.update_singal_strenght(cycle, X)
                    X += int(n)
                case ['noop']:
                    cycle += 1
                    self.update_singal_strenght(cycle, X)
    
    @property
    def part_one_sol(self) -> int:
        self.execute_program()
        return sum(self.signal_strenght)
    
    @property
    def part_two_sol(self) -> int:
        return 
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day10_test.txt'
    PATH = 'inputs/day10.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    cathode_ray_tube = CathodeRayTube(data.split('\n'))
    ic(cathode_ray_tube.part_one_sol)
    ic(cathode_ray_tube.part_two_sol)
