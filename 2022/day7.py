from dataclasses import dataclass
import os
from collections import defaultdict
from itertools import accumulate

from icecream import ic

# ls, dir, cd, ..
@dataclass
class NoSpaceLeftOnDevice:
    _data: list[str]

    def tree_traversal(self):
        '''entities -> directory path'''
        directiories = defaultdict(int)
        for line in self._data:
            line = line.split()
            match line:
                case '$', 'cd', '/':
                    entities = ['/']
                case '$', 'ls':
                    pass
                case 'dir', _:
                    pass
                case '$', 'cd', '..':
                    entities.pop()
                case '$', 'cd', x:
                    entities.append(x+'/')
                case size, _:
                    size = int(size)
                    # ic(entities)
                    for p in accumulate(entities):
                        directiories[p] += int(size)
        return directiories
    
    def total_size(self, directiories: defaultdict[str, int], max_size: int) -> int:
        total = 0
        ic(directiories)
        for size in directiories.values():
            if size <= max_size:
                total += size
        return total

    @property
    def part_one_sol(self) -> int:
        directories = self.tree_traversal()
        return self.total_size(directories, 100000)
    
    @property
    def part_two_sol(self) -> int:
        return 
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day7_test.txt'
    PATH = 'inputs/day7.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    no_space_left_on_device = NoSpaceLeftOnDevice(data.split('\n'))
    ic(no_space_left_on_device.part_one_sol)
    ic(no_space_left_on_device.part_two_sol)
