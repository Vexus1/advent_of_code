from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class TreetopTreeHouse:
    data: list[str]

    def __post_init__(self):
        self.board = self.create_board()
        self.max_height = len(self.data)-1
        self.max_width = len(self.data[0])-1

    def create_board(self) -> dict[complex, int]:
        board = dict()
        for y, row in enumerate(self.data):
            for x, col in enumerate(row):
                position = complex(x, y)
                board[position] = int(col)
        return board
    
    def is_tree_visible(self, position: complex) -> int:
        curr_tree = self.board[position]
        for dir in (1, 1j, -1, -1j):
            position_dx = position
            trees = []
            while (0 < position_dx.real < self.max_width and
                   0 < position_dx.imag < self.max_height):
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
    
    def calc_scenic_score(self, position: complex) -> int:
        starting_height = self.board[position]
        scenic_score = 1
        for dir in (1, 1j, -1, -1j):
            position_dx = position + dir
            visible_trees = 0
            while (0 <= position_dx.real <= self.max_width and
                   0 <= position_dx.imag <= self.max_height):
                height = self.board[position_dx]
                visible_trees += 1
                if height >= starting_height:
                    break
                position_dx += dir
            scenic_score *= visible_trees
        return scenic_score

    def highest_scenic_score(self) -> int:
        highest = -1
        for position in self.board.keys():
            highest = max(highest, self.calc_scenic_score(position))
        return highest
    
    @property
    def part_one_sol(self) -> int:
        return self.count_visible()
    
    @property
    def part_two_sol(self) -> int:
        return self.highest_scenic_score()
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day08_test.txt'
    PATH = 'inputs/day08.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    treetop_tree_house = TreetopTreeHouse(data.split('\n'))
    ic(treetop_tree_house.part_one_sol)
    ic(treetop_tree_house.part_two_sol)
