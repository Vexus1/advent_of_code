from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class ClumsyCrucible:
    data: list[str]

    def __post_init__(self):
        self.map_directions = self.create_map_directions()

    def create_map_directions(self) -> dict[str, complex]:
        dir_map = {'R': complex(1, 0),
                   'D': complex(0, 1),
                   'L': complex(-1, 0),
                   'U': complex(0, -1),
                   '0': complex(1, 0),
                   '1': complex(0, 1),
                   '2': complex(-1, 0),
                   '3': complex(0, -1)}
        return dir_map
    
    def divide_data(self) -> list[list[str]]:
        return list(map(str.split, self.data))
    
    def decode_hex(self, hex: str) -> tuple[str, int]:
        dir = str(int(hex[7], base=16))
        len = int(hex[2:7], base=16)
        return dir, len
    
    def lava_meters(self, data: list[tuple[str, int]]) -> int:
        position = 0
        lava = 1
        for dir, len in data:
            len = int(len)
            direction = self.map_directions[dir]
            position += direction.real * len
            lava += direction.imag * len * position + len / 2
        return int(lava)

    @property
    def part_one_sol(self):
        data = [(dir, int(len)) for dir, len, _ in self.divide_data()]
        return self.lava_meters(data)
    
    @property
    def part_two_sol(self):
        data = [self.decode_hex(hex) for _, _, hex in self.divide_data()]
        return self.lava_meters(data)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day18_test.txt'
    PATH = 'inputs/day18.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    clumsy_crucible = ClumsyCrucible(data.split('\n'))
    ic(clumsy_crucible.part_one_sol)
    ic(clumsy_crucible.part_two_sol)
