from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class CathodeRayTube:
    _data: list[str]

    def __post_init__(self):
        self.signal_strenght = []
        self.ctr_row = ''
        self.cycle = 0

    def update_singal_strenght(self, cycle: int, X: int) -> None:
        if cycle % 40 == 20:
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

    def update_row(self, min_pos: int, max_pos: int) -> None:
        if self.cycle-1 in range(min_pos, max_pos):
            self.ctr_row += '#'
        else:
            self.ctr_row += '.'
        if len(self.ctr_row) == 40:
            print(self.ctr_row)
            self.ctr_row = ''
            self.cycle = 0

    def render_image(self) -> None:
        X = 1
        min_pos = 0
        max_pos = 3
        for line in self._data:
            line = line.split()
            match line:
                case 'addx', n:
                    self.cycle += 1
                    self.update_row(min_pos, max_pos)
                    self.cycle += 1
                    self.update_row(min_pos, max_pos)
                    min_pos += int(n)
                    max_pos += int(n)
                    X += int(n)
                case ['noop']:
                    self.cycle += 1
                    self.update_row(min_pos, max_pos)
    
    @property
    def part_one_sol(self) -> int:
        self.execute_program()
        return sum(self.signal_strenght)
    
    @property
    def part_two_sol(self) -> None:
        self.render_image()
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day10_test.txt'
    PATH = 'inputs/day10.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    cathode_ray_tube = CathodeRayTube(data.split('\n'))
    ic(cathode_ray_tube.part_one_sol)
    cathode_ray_tube.part_two_sol
