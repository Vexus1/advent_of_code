from dataclasses import dataclass
import os
from collections import deque

import numpy as np
from icecream import ic  # type: ignore

@dataclass
class StepCounter:
    data: list[str]

    def create_board(self, data: list[str]) -> dict[complex, str]:
        board = {}
        for y, row in enumerate(data):
            for x, col in enumerate(row):
                pos = complex(x, y)
                board[pos] = col
        return board
    
    def expanded_data(self) -> list[str]:
        data = []
        for _ in range(5):
            for line in self.data:
                data.append(5 * line.replace("S", "."))
        return data
    
    def gardens_position(self, req_steps: int) -> set[complex]:
        expanded_data = self.expanded_data()
        if req_steps > 64:
            height = len(expanded_data) 
            width = len(expanded_data[0]) 
            board = self.create_board(expanded_data)
        else:
            height = len(self.data) 
            width = len(self.data[0]) 
            board = self.create_board(self.data)
        queue: deque[tuple[complex, int]] = deque()
        seen = set()
        result = set()
        mid_point = len(board) // 2
        start_point = list(board.keys())[mid_point]
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
                if pos.real >= 0:
                    if board[pos + 1] != '#':
                        queue.append((pos + 1, steps + 1))
                if pos.real <= width - 1:
                    if board[pos - 1] != '#':
                        queue.append((pos - 1, steps + 1))
                if pos.imag >= 0:
                    if board[pos + 1j] != '#':
                        queue.append((pos + 1j, steps + 1))
                if pos.imag <= height - 1:
                    if board[pos - 1j] != '#':
                        queue.append((pos - 1j, steps + 1))
        return result           

    def polynomial_extrapolation(self, req_steps: int) -> np.int64:
        len_board = len(self.data)
        expand_times = req_steps // len_board  
        residue = req_steps % len_board 
        a0 = len(self.gardens_position(residue))
        a1 = len(self.gardens_position(len_board + residue))
        a2 = len(self.gardens_position(2 * len_board + residue))
        vandermonde_matrix = np.matrix([[0, 0, 1],
                                        [1, 1, 1],
                                        [4, 2, 1]])
        b = np.array([a0, a1, a2])
        x = np.linalg.solve(vandermonde_matrix, b).astype(np.int64)
        quadratic_equation = x[0]*expand_times**2 + x[1]*expand_times + x[2]
        return quadratic_equation

    @property
    def part_one_sol(self) -> int:
        return len(self.gardens_position(64))

    @property
    def part_two_sol(self) -> np.int64:
        return self.polynomial_extrapolation(26501365)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day21_test.txt'
    PATH = 'inputs/day21.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    step_counter = StepCounter(data.split('\n'))
    ic(step_counter.part_one_sol)
    ic(step_counter.part_two_sol)
