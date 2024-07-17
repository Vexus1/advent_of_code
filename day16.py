from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class TheFloorWillBeLava:
    _data: list[str]

    def __post_init__(self):
        self.board = self.create_board()

    def create_board(self) -> dict[complex, str]:
        board = {}
        for i, row in enumerate(self._data):
            for j, col in enumerate(row):
                position = complex(j, i)
                board[position] = col
        return board

    def energized_board(self, path: list[int | complex]) -> set[complex | int]:
        visited = set()
        while path:
            pos, dir = path.pop()
            while not (pos, dir) in visited:
                visited.add((pos, dir))
                pos += dir
                match self.board.get(pos):
                    case '|':
                        dir = 1j
                        path.append((pos, -dir))
                    case '-':
                        dir = 1 
                        path.append((pos, -dir))
                    case '/':
                        dir = -complex(dir.imag, dir.real)
                    case '\\':
                        dir = complex(dir.imag, dir.real)
                    case None:
                        break
        return visited
    
    def count_energized_titles(self, board: dict[complex, str]) -> int:
        return len(set(pos for pos, _ in board)) - 1
    
    def find_highest_title(self, positions: list[list[complex]]) -> int:
        boards = map(self.energized_board, positions)
        return max(map(self.count_energized_titles, boards))

    @property
    def part_one_sol(self) -> int:
        energized_board = self.energized_board([(-1, 1)])
        return self.count_energized_titles(energized_board)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day16_test.txt'
    PATH = 'inputs/day16.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    the_floor_will_be_lava = TheFloorWillBeLava(data.split('\n'))
    ic(the_floor_will_be_lava.part_one_sol)
