from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class NeverTellMeTheOdds:
    _data: str

    def __post_init__(self):
        self.hailstones = self.parse_data()

    def parse_data(self) -> list[list[int]]:
        hailstones = []
        for line in self._data:
            position, velocity = line.split('@')
            px, py, pz = list(map(int, position.split(', ')))
            vx, vy, vz = list(map(int, velocity.split(', ')))
            hailstones.append((px, py, pz, vx, vy, vz))
        return hailstones
    
    def count_intersections(self, least: int, most: int) -> int:
        intersections = 0
        for i, hailstone1 in enumerate(self.hailstones):
            for hailstone2 in self.hailstones[i:]:
                if self.find_intersection(hailstone1, hailstone2,
                                          least, most):
                    intersections += 1
        return intersections

    def find_intersection(self, hailstone_A: list[int], hailstone_B: list[int],
                          least: int, most: int) -> bool:
        px1, py1, _, vx1, vy1, _ = hailstone_A
        px2, py2, _, vx2, vy2, _ = hailstone_B
        a1 = vy1/vx1
        a2 = vy2/vx2
        b1 = py1 - a1*px1
        b2 = py2 - a2*px2
        if a1 == a2:
            return False
        xpos = (b2 - b1)/(a1-a2)
        ypos = a1*xpos + b1
        if xpos < px1 and vx1 > 0:
            return False
        elif xpos > px1 and vx1 < 0:
            return False
        elif xpos < px2 and vx2 > 0:
            return False
        elif xpos > px2 and vx2 < 0:
            return False
        if least <= xpos <= most and least <= ypos <= most:
            return True

    @property
    def part_one_sol(self) -> int:
        return self.count_intersections(200000000000000, 400000000000000)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day24_test.txt'
    PATH = 'inputs/day24.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    never_tell_me_the_odds = NeverTellMeTheOdds(data.split('\n'))
    ic(never_tell_me_the_odds.part_one_sol)
