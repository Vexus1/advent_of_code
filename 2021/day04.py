from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class Board:
    grid: list[list[int]]

    def drop(self, num: str) -> None:
        for i, row in enumerate(self.grid):
            for j, n in enumerate(row):
                if n == int(num):
                    self.grid[i][j] = -1

    def horizontal(self) -> bool:
        for row in self.grid:
            if row == [-1, -1, -1, -1, -1]:
                return True
    
    def vertical(self) -> bool:
        grid = list(map(list, zip(*self.grid)))
        for row in grid:
            if row == [-1, -1, -1, -1, -1]:
                return True


@dataclass
class GiantSquid:
    data: list[str]

    def parse_data(self) -> tuple[list[str], list[Board]]:
        draw_nums = self.data[0].split(',')
        board_list: list[Board] = []
        board = []
        for row in self.data[2:]:
            if row == '':
                board_list.append(Board(board))
                board = []
                continue
            else:
                row = list(map(int, row.split()))
                board.append(row)
        board_list.append(Board(board))
        return draw_nums, board_list
    
    def score(self) -> int:
        draw_nums, board_list = self.parse_data()
        winning_board = None
        last_num = 0
        for num in draw_nums:
            for board in board_list:
                board.drop(num)
                print(board)
                if board.horizontal() or board.vertical():
                    winning_board = board.grid
                    last_num = num
                    break
            if winning_board:
                break
        board_sum = board_sum = sum(
            r for row in winning_board for r in row if r != -1
        )
        return board_sum * int(last_num)
            
    @property
    def part_one_sol(self) -> int:
        return self.score()
    
    @property
    def part_two_sol(self) -> int:
        return 
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day04_test.txt' 
    PATH = 'inputs/day04.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    giant_squid = GiantSquid(data.split('\n'))
    ic(giant_squid.part_one_sol)
    ic(giant_squid.part_two_sol)
