from dataclasses import dataclass
import os
from functools import reduce
import operator
import re
from math import sqrt

from icecream import ic

@dataclass
class WaitForIt:
    data: list[str]
    
    def __post_init__(self):
        self.time = self.race_data()[0]
        self.distance = self.race_data()[1]

    def race_data(self) -> tuple[list[int], list[int]]:
        data = re.findall(r'\d+', self.data)
        data = list(map(int, data))
        time = data[:len(data)//2]
        distance = data[len(data)//2:]
        return time, distance    
    
    def ways_to_win(self, time: list[int], distance: list[int]) -> list[int]:
        win_list = []
        for i in range(len(time)):
            ways_to_win = 0
            for speed in range(1, time[i]):
                travel = 0
                time_passed = speed
                while time_passed != time[i]:
                    time_passed += 1
                    travel += speed
                    if travel > distance[i]:
                        ways_to_win += 1
                        break
            win_list.append(ways_to_win)
        return win_list
            
    def prod(self, iterable: list[int]) -> int:
        return reduce(operator.mul, iterable, 1)

    def connect_list(self, data: list[int]) -> int:
        new_data = str(data[0])
        for i in range(1, len(data)):
            new_data += str(data[i])
        return int(new_data)
    
    def ways_to_win_for_one(self, time: int, distance: int) -> int:
        exact_acceleration = (time - sqrt((time**2 - 4*distance))) / 2
        min_acceleration = int(exact_acceleration + 1)
        return time - 2*min_acceleration + 1

    def part_one_sol(self) -> int:
        win_list = self.ways_to_win(self.time, self.distance)
        return self.prod(win_list)
    
    def part_two_sol(self) -> int:
        time = self.connect_list(self.time)
        distance = self.connect_list(self.distance)
        wins = self.ways_to_win_for_one(time, distance)
        return wins
                

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day6_test.csv'
    PATH = 'inputs/day6.csv'
    with open(PATH, 'r') as f:
        data = f.read()
    waitforit = WaitForIt(data)
    ic(waitforit.part_one_sol())
    ic(waitforit.part_two_sol())
