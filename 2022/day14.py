from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class RegolithReservoir:
    _data: list[str]

    def __post_init__(self):
        self.rocks_postion = list()
        self.sand_start_pos = complex(500, 0)

    def localize_rocks_and_void(self) -> tuple[set[complex], int]:
        rocks = set()
        void = 0
        for line in self._data:
            x = [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
            for (x1, y1), (x2, y2) in zip(x, x[1:]):
                x1, x2 = sorted([x1, x2])
                y1, y2 = sorted([y1, y2])
                void = max(void, y2 + 1) 
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        rocks.add(x + y * 1j)
        ic(void)
        return rocks, void
           
    def count_rest_sand(self) -> int:
        counter = 0
        rocks_pos, void = self.localize_rocks_and_void()
        occupied_pos = rocks_pos
        while True:
            curr_sand_pos = self.sand_start_pos
            while True:
                if curr_sand_pos.imag > void:
                    return counter
                if curr_sand_pos + 1j not in occupied_pos:
                    curr_sand_pos += 1j
                    continue
                if curr_sand_pos + 1j - 1 not in occupied_pos:
                    curr_sand_pos += 1j - 1
                    continue
                if curr_sand_pos + 1j + 1 not in occupied_pos:
                    curr_sand_pos += 1j + 1
                    continue
                else:
                    occupied_pos.add(curr_sand_pos)
                    counter += 1
                    break

    @property
    def part_one_sol(self) -> int:
        return self.count_rest_sand()
    
    @property
    def part_two_sol(self) -> int:
        return 
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day14_test.txt' 
    PATH = 'inputs/day14.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    regolith_reservoir = RegolithReservoir(data.split('\n'))
    print(regolith_reservoir.part_one_sol)
    ic(regolith_reservoir.part_two_sol)
