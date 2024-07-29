from dataclasses import dataclass
import os
from collections.abc import Generator
from collections import defaultdict

from icecream import ic

T = defaultdict[complex, list[tuple[complex, int]]]

@dataclass
class LongWalk:
    _data: str

    def __post_init__(self):
        self.board = self.create_board()
        self.height = len(self._data) 
        self.width = len(self._data[0]) 

    def create_board(self) -> dict[complex, str]:
        pos_map = dict()
        for y, row in enumerate(self._data):
            for x, col in enumerate(row):
                pos = complex(x, y)
                pos_map[pos] = col
        return pos_map
    
    def find_unique_point(self, unique_row: int) -> complex:
        unique_x_point = self._data[unique_row].index('.')
        return complex(unique_x_point, unique_row)
       
    def get_neighbours(self, pos: complex) -> Generator[complex]:
        for dir in (-1, 1, -1j, 1j):
            move = pos + dir
            if 0 <= move.real <= self.width and 0 <= move.imag <= self.height:
                if self.board[move] == '.':
                    yield move
                if self.board[move] == '>' and move.real > pos.real:
                    yield move
                if self.board[move] == 'v' and move.imag > pos.imag:
                    yield move

    def DFS(self) -> int:
        '''Iterative version'''
        start_point = self.find_unique_point(0)
        end_point = self.find_unique_point(len(self._data)-1)
        longest_path = 0
        seen = set()
        stack = [(start_point, 0)]
        while stack:
            pos, path_len = stack.pop()
            if path_len == -1:
                seen.remove(pos)
                continue
            if pos == end_point:
                longest_path = max(longest_path, path_len)
                continue
            if pos in seen:
                continue
            seen.add(pos)
            stack.append((pos, -1))
            for neighbour in self.get_neighbours(pos):
                stack.append((neighbour, path_len + 1))
        return longest_path

    @property
    def part_one_sol(self) -> int:
        return self.DFS()

    @property
    def part_two_sol(self) -> int:
        return self.DFS()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day23_test.txt'
    PATH = 'inputs/day23.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    long_walk = LongWalk(data.split('\n'))
    ic(long_walk.part_one_sol)
    ic(long_walk.part_two_sol)