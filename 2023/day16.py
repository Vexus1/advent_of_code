from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class TheFloorWillBeLava:
    data: list[str]

    def __post_init__(self):
        self.board = self.create_board()

    def create_board(self) -> dict[complex, str]:
        board = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                position = complex(j, i)
                board[position] = col
        return board

    def energized_board(self, path: list[tuple[complex,
                                               complex]]) -> set[complex]:
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
        return {p for p, _ in visited}
    
    def count_energized_titles(self, energized_tiles: set[complex]) -> int:
        return len(energized_tiles) - 1
    
    def find_all_positions(self) -> list[list[tuple[complex, complex]]]:
        positions = []
        for dir in (1,1j,-1,-1j):
            for pos in self.board:
                if pos - dir not in self.board:
                    positions.append([(pos - dir, dir)])
        return positions
    
    def find_highest_title(self) -> int:
        all_positions = self.find_all_positions()
        boards = map(self.energized_board, all_positions)
        return max(map(self.count_energized_titles, boards))

    @property
    def part_one_sol(self) -> int:
        energized_board = self.energized_board([(-1, 1)])
        return self.count_energized_titles(energized_board)
    
    @property
    def part_two_sol(self) -> int:
        return self.find_highest_title()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day16_test.txt'
    PATH = 'inputs/day16.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    the_floor_will_be_lava = TheFloorWillBeLava(data.split('\n'))
    ic(the_floor_will_be_lava.part_one_sol)
    ic(the_floor_will_be_lava.part_two_sol)
