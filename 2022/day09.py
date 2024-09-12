from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class RopeBridge:
    data: list[str]

    def __post_init__(self):
        self.directory_map = self.create_directory_map()

    def create_directory_map(self) -> dict[str, complex]:
        map = {'L': -1,
               'R': 1,
               'D': 1j,
               'U': -1j}
        return map
    
    def change_position(self, distance: complex) -> complex:
        dx = complex(0, 0)
        if distance.real > 0:
            dx += 1
        elif distance.real < 0:
            dx += -1
        if distance.imag > 0:
            dx += 1j
        elif distance.imag < 0:
            dx += -1j
        return dx

    def visited_positions(self, knots: int) -> list[set[complex]]:
        rope = [0 + 0j] * knots
        seen = [set([0 + 0j]) for _ in range(knots)]
        for line in self.data:
            travel_len = int(line[2:])
            for _ in range(travel_len):
                dir = line[0]
                rope[0] += self.directory_map[dir]
                for i in range(1, knots):
                    distance = rope[i-1] - rope[i]
                    if abs(distance) >= 2:
                        rope[i] += self.change_position(distance)
                        seen[i].add(rope[i])
        return seen

    @property
    def part_one_sol(self) -> int:
        return len(self.visited_positions(2)[1])
    
    @property
    def part_two_sol(self) -> int:
        return len(self.visited_positions(10)[9])
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day09_test.txt'
    PATH = 'inputs/day09.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    rope_bridge = RopeBridge(data.split('\n'))
    ic(rope_bridge.part_one_sol)
    ic(rope_bridge.part_two_sol)
