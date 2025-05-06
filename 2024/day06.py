import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class GuardGallivant:
    data: list[str]

    def __post_init__(self):
        self.grid = self.create_grid()

    def create_grid(self) -> dict[complex, str]:
        grid = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                position = complex(j, i)
                grid[position] = col
        return grid
    
    def starting_position(self) -> complex:
        return list(self.grid.keys())[list(self.grid.values()).index('^')]
    
    def rotate_step(self, step: complex) -> complex:
        match step:
            case -1j:
                step = 1
            case 1:
                step = 1j
            case 1j:
                step = -1
            case -1:
                step = -1j
        return step
    
    def count_distinct_positions(self) -> int:
        start = self.starting_position()
        max_widht = len(self.data[0])
        max_height = len(self.data)
        step = -1j
        count = 1
        while True:
            if (start.real + step.real >= max_widht or 
                start.imag + step.imag >= max_height or
                start.real - step.real < 0 or
                start.imag + step.imag < 0):
                break
            if self.grid[start + step] == '#':
                step = self.rotate_step(step)
            if self.grid[start] != 'X':
                count += 1
            self.grid[start] = 'X'
            start += step
        return count

    @property
    def part_one(self) -> int:
        return self.count_distinct_positions()
    
    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__': 
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day06_test.txt'
    PATH = 'inputs/day06.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    guard_gallivant = GuardGallivant(data.split('\n'))
    ic(guard_gallivant.part_one)
    ic(guard_gallivant.part_two)
