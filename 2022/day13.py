from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class DistressSignal:
    _data: list[str]

    def __post_init__(self):
        self.pairs = self.parse()

    def parse(self) -> list[list[list | int]]:
        pairs = [[*map(eval, line.split())] for line in self._data]
        return pairs

    def compare_packet(self, left: list[list | int], right: list[list | int]) -> int:
        match left, right:
            case int(), int():
                return self.compare_values(left, right)
            case int(), list():
                return self.compare_packet([left], right)
            case list(), int():
                return self.compare_packet(left, [right])
            case list(), list():
                for result in map(self.compare_packet, left, right):
                    if result != 0:
                        return result
                return self.compare_packet(len(left), len(right))

    def compare_values(self, left: int, right: int) -> int:
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0

    def count_right_ordered(self) -> int:
        counter = 0
        for i, pair in enumerate(self.pairs, 1):
            if self.compare_packet(*pair) == 1:
                counter += i
        return counter

    @property
    def part_one_sol(self) -> int:
        return self.count_right_ordered()
    
    @property
    def part_two_sol(self) -> int:
        return
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day13_test.txt' 
    PATH = 'inputs/day13.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    distress_signal = DistressSignal(data.split('\n\n'))
    ic(distress_signal.part_one_sol)
    ic(distress_signal.part_two_sol)
