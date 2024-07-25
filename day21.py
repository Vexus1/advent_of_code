from dataclasses import dataclass
import os
from collections import deque

from icecream import ic

@dataclass
class StepCounter:
    _data: str

    def __post_init__(self):
        self.board = self.create_board()

    def create_board(self) -> dict[complex, str]:
        board = {}
        for y, row in enumerate(self._data):
            for x, col in enumerate(row):
                pos = complex(x, y)
                board[pos] = col
        return board
    
    def gardens_position(self, req_steps: int) -> set[complex]:
        queue = deque()
        seen = set()
        result = set()
        height = len(self._data) 
        width = len(self._data[0]) 
        start_point = list(self.board.keys())[list(self.board.values()).index('S')]
        queue.append((start_point, 0))
        while queue:
            pos: complex
            pos, steps = queue.popleft()
            if (pos, steps) in seen:
                continue
            seen.add((pos, steps))
            if steps == req_steps:
                result.add(pos)
            else:
                steps += 1
                if pos.real >= 0:
                    if self.board[pos+1] != '#':
                        queue.append((pos+1, steps))
                if pos.real <= width - 1:
                    if self.board[pos-1] != '#':
                        queue.append((pos-1, steps))
                if pos.imag >= 0:
                    if self.board[pos+1j] != '#':
                        queue.append((pos+1j, steps))
                if pos.imag <= height - 1:
                    if self.board[pos-1j] != '#':
                        queue.append((pos-1j, steps))
        return result           

    @property
    def part_one_sol(self) -> int:
        return len(self.gardens_position(64))

    @property
    def part_two_sol(self) -> int:
        pass


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day21_test.txt'
    PATH = 'inputs/day21.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    step_counter = StepCounter(data.split('\n'))
    ic(step_counter.part_one_sol)
    ic(step_counter.part_two_sol)
