from dataclasses import dataclass
import os
import re
from itertools import pairwise

from icecream import ic

@dataclass
class BeaconExclusionZone:
    _data: list[str]

    def __post_init__(self):
        self.sensors, self.beacons, self.distance = self.parse()

    def parse(self) -> tuple[list[complex], list[complex]]:
        sensors, beacons, distance = [], [], []
        for line in self._data:
            cords = re.findall(r'-?\d+', line)
            cords = list(map(int, cords))
            position = complex(cords[0], cords[1])
            sensors.append(position)
            position = complex(cords[2], cords[3])
            beacons.append(position)
            distance.append(self.manhattan(*cords))
        return sensors, beacons, distance
    
    def manhattan(self, x1: int, y1: int, x2: int, y2: int):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def count_locked_in_row(self, row: int) -> int:
        ranges = []
        for pos, dist in zip(self.sensors, self.distance):
            estimated_dist = pos.imag - row
            if estimated_dist > dist:
                continue
            ranges.append(((pos.real + abs(estimated_dist) - dist),
                           (pos.real - abs(estimated_dist) + dist + 1)))
        beacons_on_row = len(set(pos.real for pos in self.beacons if pos.imag == row))
        left, right = zip(*ranges)
        return int(max(right) - min(left) - beacons_on_row)
    
    def find_distress_beacon(self, bound: int) -> int:
        # y = ax + b
        a_coeffs = list()
        b_coeffs = list()
        for pos, dist in zip(self.sensors, self.distance):
            a_coeffs.append(pos.imag - pos.real + dist + 1)
            a_coeffs.append(pos.imag - pos.real - dist - 1)
            b_coeffs.append(pos.imag + pos.real + dist + 1)
            b_coeffs.append(pos.imag + pos.real - dist - 1)
        a_coeffs = {a for a in a_coeffs if a_coeffs.count(a) >= 2}
        b_coeffs = {b for b in b_coeffs if b_coeffs.count(b) >= 2}
        for a in a_coeffs:
            for b in b_coeffs:
                intersect = [(b - a) // 2, (a + b) // 2]
                if 0 < intersect[0] < bound and 0 < intersect[1] < bound:
                    if all(self.manhattan(*intersect, pos.real, pos.imag) > dist
                           for pos, dist in zip(self.sensors, self.distance)):
                        return int(bound * intersect[0] + intersect[1])
        
    @property
    def part_one_sol(self) -> int:
        return self.count_locked_in_row(2_000_000)
    
    @property
    def part_two_sol(self) -> int:
        return self.find_distress_beacon(4_000_000)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day15_test.txt' 
    PATH = 'inputs/day15.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    beacon_exclusion_zone = BeaconExclusionZone(data.split('\n'))
    ic(beacon_exclusion_zone.part_one_sol)
    ic(beacon_exclusion_zone.part_two_sol)
