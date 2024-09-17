from dataclasses import dataclass
import os
from math import lcm

from icecream import ic  # type: ignore

@dataclass
class HauntedWasteland:
    data: list[str]

    def __post_init__(self):
        self.navigation = self.navigation_list()
        self.node_map = self.create_node_map()

    def navigation_list(self) -> list[str]:
        return [i for i in self.data[0]]

    def create_node_map(self) -> dict[str, list[str]]:
        node_data = self.data[2:]
        map = {}
        for node in node_data:
            key, value = node.split(' = (')
            map[key] = list(value[:-1].split(', '))
        return map
    
    def choose_trace(self, path: str, curr_position: str) -> str:
        if path == 'L':
            curr_position = self.node_map[curr_position][0]
        else:
            curr_position = self.node_map[curr_position][1]
        return curr_position

    def calc_steps(self, strat_pos: str) -> int:
        curr_position = strat_pos
        count = 0
        while True:
            for path in self.navigation:
                curr_position = self.choose_trace(path, curr_position)
                count += 1
                if curr_position == 'ZZZ' or curr_position.endswith('Z'):
                    return count

    def find_least_common_multiple(self) -> int:
        count = 1
        for start in list(self.node_map.keys()):
            if start.endswith('A'):
                count = lcm(count, self.calc_steps(start))
        return count

    @property
    def part_one_sol(self) -> int:
        return self.calc_steps('AAA')
    
    @property
    def part_two_sol(self) -> int:
        return self.find_least_common_multiple()
                
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day08_test.txt'
    PATH = 'inputs/day08.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    haunted_wasteland = HauntedWasteland(data.split('\n'))
    ic(haunted_wasteland.part_one_sol)
    ic(haunted_wasteland.part_two_sol)
