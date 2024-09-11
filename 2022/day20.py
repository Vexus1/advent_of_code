from dataclasses import dataclass
import os
from itertools import cycle
from copy import deepcopy

from icecream import ic


@dataclass
class GrovePositioningSystem:
    _data: list[str]

    def __post_init__(self):
        self.numbers, self.sequence = self._parse_data()

    def _parse_data(self) -> tuple[list[int], list[tuple[int, int]]]:
        numbers = [int(n) for n in self._data]
        sequence = [n for n in enumerate(numbers)]
        return numbers, sequence

    def _move_numbers(self) -> None:
        cyc = cycle(deepcopy(self.sequence))
        cyc_len = len(self.sequence) - 1 
        for _ in range(len(self.numbers)):
            curr = next(cyc)
            old_index = self.sequence.index(curr)
            self.sequence.remove(curr)
            new_index = (old_index + curr[1] + cyc_len) % cyc_len
            self.sequence.insert(new_index, curr)
    
    def _grove_coordinates(self) -> int:
        self._move_numbers()
        zero_tuple_index = self.sequence.index((self.numbers.index(0), 0))
        sol = 0
        for i in [1000, 2000, 3000]:
            sol += self.sequence[(zero_tuple_index + i) % len(self.numbers)][1]
        return sol

    @property
    def part_one_sol(self) -> int:
        return self._grove_coordinates()
    
    @property
    def part_two_sol(self) -> int:
        return
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day20_test.txt' 
    PATH = 'inputs/day20.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    grove_positioning_system = GrovePositioningSystem(data.split('\n'))
    ic(grove_positioning_system.part_one_sol)
    ic(grove_positioning_system.part_two_sol)
