from dataclasses import dataclass
import os
from heapq import heappush, heappop

from icecream import ic

@dataclass
class ClumsyCrucible:
    _data: list[str]

    def __post_init__(self):
        self.board = self.create_board

    @property
    def create_board(self) -> dict[complex, str]:
        board = {}
        for y, row in enumerate(self._data):
            for x, col in enumerate(row):
                position = complex(x, y)
                board[position] = int(col)
        return board
    
    def minimal_heat(self, start: complex, end: complex, min: int, max: int) -> int:
        x = 0
        seen = set()
        queue = [(0, 0, start, 1)]
        while queue:
            heat, _, position, direction = heappop(queue)
            if position == end:
                return heat
            if (position, direction) in seen:
                continue
            seen.add((position, direction))
            for dir in 1j/direction, -1j/direction:
                for i in range(min, max+1):
                    move = position + dir*i
                    if move in self.board:
                        h = sum(self.board[position + dir*j] for j in range(1, i+1))
                        heappush(queue, (heat+h, x:=x+1, move, dir))
    
    @property
    def part_one_sol(self) -> int:
        return self.minimal_heat([*self.board][0], [*self.board][-1], 1, 3)
    
    @property
    def part_two_sol(self) -> int:
        return self.minimal_heat([*self.board][0], [*self.board][-1], 4, 10)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day17_test.txt'
    PATH = 'inputs/day17.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    clumsy_crucible = ClumsyCrucible(data.split('\n'))
    ic(clumsy_crucible.part_one_sol)
    ic(clumsy_crucible.part_two_sol)
