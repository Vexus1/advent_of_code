import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class DiskFragmenter:
    data: str

    def eval_nums(self) -> list[str]:
        blocks = []
        id = 0
        for i, n in enumerate(self.data):
            if i % 2 == 0:
                blocks.extend([str(id)] * int(n))
                id += 1
            else:
                blocks.extend('.' * int(n))
        return blocks
    
    def move_blocks(self, blocks: list[str]) -> list[str]:
        dots = blocks.count('.')
        if dots == 0:
            return blocks
        stack = [n for n in blocks if n != '.']
        moved_blocks = blocks[:]
        count_moves = 0
        for i, n in enumerate(blocks):
            if dots == count_moves:
                break
            if n == '.':
                moved_blocks[i] = stack.pop()
                count_moves += 1
        return moved_blocks[:-dots]

    def calc_checksum(self) -> int:
        filesystem = self.move_blocks(self.eval_nums())
        return sum([i*int(n) for i, n in enumerate(filesystem)])

    @property
    def part_one(self) -> int:
        return self.calc_checksum()
    
    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day09_test.txt'
    PATH = 'inputs/day09.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    disk_fragmenter = DiskFragmenter(data)
    ic(disk_fragmenter.part_one)
    ic(disk_fragmenter.part_two)
    