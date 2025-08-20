import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class DiskFragmenter:
    data: str

    def eval_nums(self) -> list[str]:
        blocks = []
        file_id = 0
        for i, n in enumerate(self.data):
            if i % 2 == 0:
                blocks.extend([str(file_id)] * int(n))
                file_id += 1
            else:
                blocks.extend(['.'] * int(n))
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
    
    def create_file_map(self) -> tuple[list[tuple[int, int]],
                                       list[tuple[int, int]]]:
        disks = []
        spaces = []
        pos = 0
        for i, length in enumerate(map(int, self.data)):
            pair = (pos, length)
            if i % 2 == 0:
                disks.append(pair)
            else:
                spaces.append(pair)
            pos += length
        return disks, spaces
    
    def move_whole_files(self) -> list[tuple[int, int]]:
        disks, spaces = self.create_file_map()
        for i in range(len(disks) - 1, -1, -1):
            dpos, dlen = disks[i]
            for j, (spos, slen) in enumerate(spaces):
                if slen == 0:
                    continue
                if spos >= dpos:
                    break
                if slen >= dlen:
                    disks[i] = (spos, dlen)
                    spaces[j] = (spos + dlen, slen - dlen)
                    break
        return disks

    @property
    def part_one(self) -> int:
        filesystem = self.move_blocks(self.eval_nums())
        return sum([i*int(n) for i, n in enumerate(filesystem)])
    
    @property
    def part_two(self) -> int:
        filesystem = self.move_whole_files()
        return sum(i * dlen * (2 * dpos + dlen - 1) 
                   for i, (dpos, dlen) in enumerate(filesystem)) // 2


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day09_test.txt'
    PATH = 'inputs/day09.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    disk_fragmenter = DiskFragmenter(data)
    ic(disk_fragmenter.part_one)
    ic(disk_fragmenter.part_two)
