from dataclasses import dataclass
import os

from sympy import Symbol, solve_poly_system  # type: ignore
from icecream import ic  # type: ignore

Hailstone = tuple[int, int, int, int, int, int]

@dataclass
class NeverTellMeTheOdds:
    data: list[str]

    def __post_init__(self):
        self.hailstones = self.parse_data()

    def parse_data(self) -> list[Hailstone]:
        hailstones = []
        for line in self.data:
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

    def find_intersection(self, hailstone_A: Hailstone, hailstone_B: Hailstone,
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
        return False

    def find_perfect_position(self) -> tuple[int, int, int]:
        '''Can be done without sympy just by 
           linear algebra for first 3 hailstones'''
        pxS = Symbol('x')
        pyS = Symbol('y')
        pzS = Symbol('z')
        vxS = Symbol('vx')
        vyS = Symbol('vy')
        vzS = Symbol('vz')
        equations = []
        times = []
        for i, hailstone in enumerate(self.hailstones[:3]):
            px, py, pz, vx, vy, vz = hailstone
            t = Symbol('t'+str(i)) 
            eqx = pxS + vxS * t - (px + vx * t)
            eqy = pyS + vyS * t - (py + vy * t)
            eqz = pzS + vzS * t - (pz + vz * t)
            equations.append(eqx)
            equations.append(eqy)
            equations.append(eqz)
            times.append(t)
        position = solve_poly_system(equations, *([pxS, pyS, pzS, vxS, vyS, vzS]+times))
        return position[0][0], position[0][1], position[0][2] 

    @property
    def part_one_sol(self) -> int:
        return self.count_intersections(200000000000000, 400000000000000)

    @property
    def part_two_sol(self) -> int:
        return sum(self.find_perfect_position())


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day24_test.txt'
    PATH = 'inputs/day24.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    never_tell_me_the_odds = NeverTellMeTheOdds(data.split('\n'))
    ic(never_tell_me_the_odds.part_one_sol)
    ic(never_tell_me_the_odds.part_two_sol)
