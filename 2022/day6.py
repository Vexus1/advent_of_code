from dataclasses import dataclass
import os
from collections import deque

from icecream import ic

@dataclass
class TuningTrouble:
    _data: str

    def find_marker_position(self, marker_len: int) -> int:
        potential_marker = deque(self._data[:marker_len-1])
        sliced_data = self._data[marker_len-1:]
        for i, char in enumerate(sliced_data):
            potential_marker.append(char)
            correct = set(potential_marker)
            if len(correct) == marker_len:
                return i + 1 + marker_len - 1
            potential_marker.popleft()

    @property
    def part_one_sol(self) -> int:
        return self.find_marker_position(4)
    
    @property
    def part_two_sol(self) -> int:
        return self.find_marker_position(14)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day6_test.txt'
    PATH = 'inputs/day6.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    tuning_trouble = TuningTrouble(data)
    ic(tuning_trouble.part_one_sol)
    ic(tuning_trouble.part_two_sol)
