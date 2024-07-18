from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class ClumsyCrucible:
    _data: list[str]

    @property
    def _map_directions(self) -> dict[str, complex]:
        dir_map = {'R': complex(1, 0),
                   'D': complex(0, 1),
                   'L': complex(-1, 0),
                   'U': complex(0, -1),
                   '0': complex(1, 0),
                   '1': complex(0, 1),
                   '2': complex(-1, 0),
                   '3': complex(0, -1)}
        return dir_map
    
    @property
    def _divide_data(self) -> tuple[list[str | int]]:
        return list(map(str.split, self._data))
    
    def decode_hex(self, hex: str) -> list[tuple[str]]:
        dir = str(int(hex[7], base=16))
        len = int(hex[2:7], base=16)
        return dir, len
    
    def _lava_meters(self, data: list[tuple[str]]) -> int:
        position = 0
        lava = 1
        for dir, len in data:
            len = int(len)
            dir = self._map_directions[dir]
            position += dir.real*len
            lava += dir.imag*len * position + len/2
        return int(lava)

    @property
    def part_one_sol(self):
        data = [(dir, len) for dir, len, _ in self._divide_data]
        return self._lava_meters(data)
    
    @property
    def part_two_sol(self):
        data = [self.decode_hex(hex) for _, _, hex in self._divide_data]
        return self._lava_meters(data)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day18_test.txt'
    PATH = 'inputs/day18.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    clumsy_crucible = ClumsyCrucible(data.split('\n'))
    ic(clumsy_crucible.part_one_sol)
    ic(clumsy_crucible.part_two_sol)
