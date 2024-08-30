from dataclasses import dataclass
import os
from functools import reduce
from typing import Iterable
from operator import mul
import re
from collections import deque

from icecream import ic

@dataclass
class ProboscideaVolcanium:
    _data: list[str]

    def __post_init__(self):
        pass
        
    def mult(self, sequence: Iterable) -> int:
        return reduce(mul, sequence)

    def _parse_data(self) -> tuple[set[str], list[int], list[str]]:
        nodes = set()
        rates = []
        dests = []
        for line in self._data:
            values = re.findall(r'Valve (\w+) .*=(\d*); .* valves? (.*)', line)
            node, rate, dest = values[0]
            dest = dest.split(',')
            nodes.add(node)
            rates.append(rate)
            dests.append(dest)
        return nodes, rates, dests
    
    def BFS():
        pass
    
    def _presure_release(self, node: str, rate: int, dests: str) -> int:
        ic(self._parse_data())

    def _most_pressure_release(self, minutes: int) -> int:
        pass

    @property
    def part_one_sol(self) -> int:
        return self._most_pressure_release(30)
    
    @property
    def part_two_sol(self) -> int:
        return
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day16_test.txt' 
    # PATH = 'inputs/day16.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    proboscidea_volcanium = ProboscideaVolcanium(data.split('\n'))
    ic(proboscidea_volcanium.part_one_sol)
    ic(proboscidea_volcanium.part_two_sol)
