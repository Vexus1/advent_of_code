from dataclasses import dataclass
import os
import re
from typing import Optional

from icecream import ic  # type: ignore

@dataclass
class SandSlabs:
    data: list[str]

    def __post_init__(self):
        self.bricks = self.parse_data()
        self.fallen = self.count_fallen()

    def parse_data(self) -> list[list[int]]:
        bricks = []
        for line in self.data:
            brick = [*map(int, re.findall(r'\d+',line))]
            bricks.append(brick)
        bricks.sort(key=lambda z: z[2])
        return bricks
    
    def drop_brick(self, update_bricks: bool = False,
                   disintegrated: Optional[list[int]] = None) -> int:
        '''Brute force, can be done faster by graph'''
        fell_times = 0
        heights_map: dict[tuple[int, int], int] = dict()
        for brick in self.bricks:
            if brick == disintegrated:
                continue
            x0, y0, z0, x1, y1, z1 = brick
            x_pos = range(x0, x1 + 1)
            y_pos = range(y0, y1 + 1)
            xy_pos = []
            for x in x_pos:
                for y in y_pos:
                    xy_pos.append((x,y))
            height = max(heights_map.get(xy, 0) for xy in xy_pos)
            drop = z0 - height - 1
            if drop:
                fell_times += 1
                z1 -= drop
                if update_bricks:
                    brick[2] -= drop
                    brick[5] -= drop
            for xy in xy_pos:
                heights_map[xy] = z1
        return fell_times
    
    def count_fallen(self) -> list[int]:
        drop_counts = []
        self.drop_brick(update_bricks=True)
        for brick in self.bricks:
            drop_counts.append(self.drop_brick(disintegrated=brick))
        return drop_counts

    @property
    def part_one_sol(self) -> int:
        return self.fallen.count(0)
    
    @property
    def part_one_two(self) -> int:
        return sum(self.fallen)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day22_test.txt'
    PATH = 'inputs/day22.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    sand_slabs = SandSlabs(data.split('\n'))
    ic(sand_slabs.part_one_sol)
    ic(sand_slabs.part_one_two)
