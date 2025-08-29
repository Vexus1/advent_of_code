import os
from dataclasses import dataclass
import re

from icecream import ic  # type: ignore

@dataclass(frozen=True)
class Robot:
    px: int
    py: int
    vx: int
    vy: int

    def final_pos(self, t: int, width: int, height: int) -> tuple[int, int]:
        x = (self.px + t * self.vx) % width
        y = (self.py + t * self.vy) % height
        return x, y


@dataclass
class RestroomRedoubt:
    data: list[str]
    width: int = 101
    height: int = 103

    def __post_init__(self):
        self.robots: list[Robot] = self._create_robots()

    def _create_robots(self) -> list[Robot]:
        robots = []
        for line in self.data:
            px, py, vx, vy = tuple(map(int, (re.findall(r'-?\d+', line))))
            robots.append(Robot(px, py, vx, vy))
        return robots
    
    def count_safety_factors(self, t: int) -> int:
        mid_x = self.width  // 2
        mid_y = self.height // 2
        tl = tr = bl = br = 0
        for robot in self.robots:
            x, y = robot.final_pos(t, self.width, self.height)
            if x < mid_x and y < mid_y:
                tl += 1
            elif x > mid_x and y < mid_y:
                tr += 1
            elif x < mid_x and y > mid_y:
                bl += 1
            elif x > mid_x and y > mid_y:
                br += 1
        return tl * tr * bl * br
  
    @property
    def part_one(self) -> int:
        return self.count_safety_factors(100)
    
    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day14_test.txt'
    PATH = 'inputs/day14.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n')
    restroom_redoubt = RestroomRedoubt(data)
    ic(restroom_redoubt.part_one)
    ic(restroom_redoubt.part_two)
