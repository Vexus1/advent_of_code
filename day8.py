from dataclasses import dataclass
import os

from icecream import ic

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
                if curr_position == 'ZZZ':
                    return count

    def part_one_sol(self) -> int:
        return self.calc_steps('AAA')
                
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day8_test.csv'
    PATH = 'inputs/day8.csv'
    with open(PATH, 'r') as f:
        data = f.read()
    haunted_wasteland = HauntedWasteland(data.split('\n'))
    ic(haunted_wasteland.part_one_sol())
    # ic(haunted_wasteland.part_two_sol())
