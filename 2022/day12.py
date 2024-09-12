from dataclasses import dataclass
import os
from heapq import heappop, heappush

from icecream import ic  # type: ignore

@dataclass
class HillClimbingAlgorithm:
    _data: list[str]

    def __post_init__(self):
        self.start_pos: complex
        self.end_pos: complex
        self.board = self.create_board()

    def get_weight(self, char: str) -> int:
        return ord(char) - 96

    def create_board(self) -> dict[complex, int]:
        board = dict()
        for y, row in enumerate(self._data):
            for x, col in enumerate(row):
                position = complex(x, y)
                if col == 'S':
                    self.start_pos = position
                    board[position] = 0
                elif col == 'E':
                    self.end_pos = position
                    board[position] = -1
                else:
                    board[position] = self.get_weight(col)
        return board
    
    @property
    def multiple_start_positions(self) -> list[complex]:
        board_val = list(self.board.values())
        start_indexes = [i for i in range(len(board_val)) if board_val[i] == 1]
        positions = list(self.board.keys())
        start_positions = [positions[i] for i in start_indexes]
        start_positions.append(self.start_pos)
        return start_positions

    def dijkstra(self, max_weight: int, start: complex | list[complex], end: complex) -> int | None:
        x = 0
        seen = set()
        moves = []
        queue: list[tuple[int, int, complex, complex]]
        if isinstance(start, list):
            queue = [(0, 0, s, 1) for s in start]
        else:
            queue = [(0, 0, start, 1)]
        while queue:
            steps, _, position, direction = heappop(queue)
            if position == end:
                return steps
            if (position, direction) in seen:
                continue
            seen.add((position, direction))
            for dir in (1, 1j, -1, -1j):
                move = position + dir
                if move in self.board:
                    if self.board[move] - self.board[position] > max_weight:
                        continue
                    moves.append(move)
                    heappush(queue, (steps+1, x:=x+1, move, dir))
        return None
            
    def multiple_paths(self, start: list[complex]) -> int:
        steps_list = []
        end_pos = self.end_pos
        for start_pos in start:
            steps = self.dijkstra(1, start_pos, end_pos)
            if steps is not None:
                steps_list.append(steps)
        if steps_list:
            return min(steps_list)
        else:
            return -1

    @property
    def part_one_sol(self) -> int:
        return self.dijkstra(1, self.start_pos, self.end_pos) or -1
    
    @property
    def part_two_sol(self) -> int:
        return self.multiple_paths(self.multiple_start_positions)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day12_test.txt'
    PATH = 'inputs/day12.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    hill_climbing_algorithm = HillClimbingAlgorithm(data.split('\n'))
    ic(hill_climbing_algorithm.part_one_sol)
    ic(hill_climbing_algorithm.part_two_sol)
