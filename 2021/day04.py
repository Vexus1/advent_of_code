from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class Board:
    grid: list[list[int]]
    won: bool = False

    def drop(self, num: int) -> None:
        for i, row in enumerate(self.grid):
            for j, n in enumerate(row):
                if n == int(num):
                    self.grid[i][j] = -1

    def wins(self) -> bool:
        return (
            any(all(value == -1 for value in row) 
                for row in self.grid
            )
            or any(all(row[col] == -1 for row in self.grid) 
                   for col in range(5)
            )
        )

    def unmarked_sum(self) -> int:
        return sum(value for row in self.grid 
                   for value in row if value != -1
        )


@dataclass
class GiantSquid:
    data: list[str]

    def parse_data(self) -> tuple[list[int], list[Board]]:
        draw_nums = list(map(int, self.data[0].split(',')))
        board_list: list[Board] = []
        board: list[list[int]] = []
        for row in self.data[2:]:
            if row == '':
                board_list.append(Board(board))
                board = []
            else:
                row = list(map(int, row.split()))
                board.append(row)
        board_list.append(Board(board))
        return draw_nums, board_list
    
    def score(self) -> int:
        draw_nums, board_list = self.parse_data()
        for num in draw_nums:
            for board in board_list:
                board.drop(num)
                if board.wins():
                    return board.unmarked_sum() * num
    
    def last_score(self) -> int:
        draw_nums, board_list = self.parse_data()
        last_board = None
        last_num = 0
        for num in draw_nums:
            for board in board_list:
                if board.won:
                    continue
                board.drop(num)
                if board.wins():
                    board.won = True
                    last_board = board
                    last_num = num
        return last_board.unmarked_sum() * last_num

    @property
    def part_one_sol(self) -> int:
        return self.score()
    
    @property
    def part_two_sol(self) -> int:
        return self.last_score()
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day04_test.txt' 
    PATH = 'inputs/day04.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    giant_squid = GiantSquid(data.split('\n'))
    ic(giant_squid.part_one_sol)
    ic(giant_squid.part_two_sol)
