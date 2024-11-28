from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class Dive:
    data: list[str]

    def count_position(self) -> int:
        horizontal = 0
        depth = 0
        for line in self.data:
            command, num = line.split(' ')
            num = int(num)
            match command:
                case 'forward': 
                    horizontal += num
                case 'down':
                    depth += num
                case 'up':
                    depth -= num
        return horizontal * depth
    
    @property
    def part_one_sol(self) -> int:
        return self.count_position()
    
    @property
    def part_two_sol(self) -> int:
        return 
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day02_test.txt' 
    # PATH = 'inputs/day02.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    dive = Dive(data.split('\n'))
    ic(dive.part_one_sol)
    ic(dive.part_two_sol)
