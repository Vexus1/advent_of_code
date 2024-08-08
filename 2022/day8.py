from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class TreetopTreeHouse:
    _data: list[str]

    def __post_init__(self):
        self.board = self.create_board()

    def create_board(self) -> dict[complex, int]:
        board = dict()
        for y, row in enumerate(self._data):
            for x, col in enumerate(row):
                position = complex(x, y)
                board[position] = int(col)
        return board
    
    def is_tree_visible(self, position: complex) -> int:
        curr_tree = self.board[position]
        for dir in (1, 1j, -1, -1j):
            max_height = len(self._data) - 1
            max_width = len(self._data[0]) - 1
            position_dx = position
            trees = []
            while 0 < position_dx.real < max_width and 0 < position_dx.imag < max_height:
                position_dx += dir
                trees.append(self.board[position_dx])
            if trees:
                if max(trees) < curr_tree:
                    return 1
            else:
                return 1
        return 0
    
    def count_visible(self) -> int:
        counter = 0
        for position in self.board.keys():
            counter += self.is_tree_visible(position)
        return counter

    @property
    def part_one_sol(self) -> int:
        return self.count_visible()
    
    @property
    def part_two_sol(self) -> int:
        return
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day8_test.txt'
    PATH = 'inputs/day8.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    treetop_tree_house = TreetopTreeHouse(data.split('\n'))
    ic(treetop_tree_house.part_one_sol)
    ic(treetop_tree_house.part_two_sol)
