from dataclasses import dataclass
import os
from heapq import heappop, heappush

from icecream import ic


@dataclass
class HillClimbingAlgorithm:
    _data: list[str]

    def __post_init__(self):
        self.board = self.create_board()

    def get_weight(self, char: str) -> int:
        return ord(char) - 96

    def create_board(self) -> dict[complex, int]:
        board = dict()
        for y, row in enumerate(self._data):
            for x, col in enumerate(row):
                position = complex(x, y)
                board[position] = self.get_weight(col)
        return board
    
    def start_pos(self) -> complex:
        start_index = list(self.board.values()).index(-13)
        pos = list(self.board.keys())[start_index]
        self.board[pos] = 0
        return pos

    def end_pos(self) -> complex:
        end_index = list(self.board.values()).index(-27)
        pos = list(self.board.keys())[end_index]
        self.board[pos] = -1
        return pos

    def dijkstra(self, max_weight: int) -> int:
        start = self.start_pos()
        end = self.end_pos()
        x = 0
        seen = set()
        moves = []
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

    @property
    def part_one_sol(self) -> int:
        return self.dijkstra(1)
    
    @property
    def part_two_sol(self) -> int:
        return
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day12_test.txt'
    PATH = 'inputs/day12.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    hill_climbing_algorithm = HillClimbingAlgorithm(data.split('\n'))
    ic(hill_climbing_algorithm.part_one_sol)
    ic(hill_climbing_algorithm.part_two_sol)
