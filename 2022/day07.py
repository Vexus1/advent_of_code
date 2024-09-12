from dataclasses import dataclass
import os
from collections import defaultdict
from itertools import accumulate

from icecream import ic  # type: ignore

@dataclass
class NoSpaceLeftOnDevice:
    data: list[str]

    def tree_traversal(self):
        '''entities -> directory path'''
        directiories = defaultdict(int)
        for line in self.data:
            line = line.split()
            match line:
                case '$', 'cd', '/':
                    entities = ['/']
                case '$', 'cd', '..':
                    entities.pop()
                case '$', 'cd', x:
                    entities.append(x+'/')
                case '$', 'ls':
                    pass
                case 'dir', _:
                    pass
                case size, _:
                    for dir in accumulate(entities):
                        directiories[dir] += int(size)
        return directiories
    
    def total_size(self, directiories: defaultdict[str, int], max_size: int) -> int:
        total = 0
        for size in directiories.values():
            if size <= max_size:
                total += size
        return total
    
    def min_directory_to_delete(self, directiories: defaultdict[str, int],
                                min_space: int, max_space: int) -> int:
        sizes = []
        total_dirs_space = directiories['/']
        space_goal = max_space - min_space
        for size in directiories.values():
            if size >= total_dirs_space - space_goal:
                sizes.append(size)
        return min(sizes)

    @property
    def part_one_sol(self) -> int:
        directories = self.tree_traversal()
        return self.total_size(directories, 100000)
    
    @property
    def part_two_sol(self) -> int:
        directories = self.tree_traversal()
        return self.min_directory_to_delete(directories, 30000000, 70000000) 
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day07_test.txt'
    PATH = 'inputs/day07.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    no_space_left_on_device = NoSpaceLeftOnDevice(data.split('\n'))
    ic(no_space_left_on_device.part_one_sol)
    ic(no_space_left_on_device.part_two_sol)
