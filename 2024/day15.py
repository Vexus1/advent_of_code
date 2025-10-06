import os
from dataclasses import dataclass

from icecream import ic  # type: ignore

@dataclass
class WarehouseWoes:
    data: list[str]

    def __post_init__(self):
        self.grid, self.moves = self.data
        self.moves = self.parse_moves(self.moves)
        self.grid = self.parse_grid(self.grid.splitlines())

    def parse_grid(self, data: list[str]) -> dict[complex, str]:
        grid = {}
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                pos = complex(i, j)
                grid[pos] = col
        return grid
    
    def parse_moves(self, block: str) -> str:
        return "".join(line.strip() for line in block.splitlines())

    def map_moves(self, move: str) -> complex:
        dir_map = {'<': -1j,
                   'v': 1,
                   '>': 1j,
                   '^': -1}
        return dir_map[move]

    def parse_robot(self) -> complex:
        return next(pos for pos, ch in self.grid.items() if ch == '@')

    def update_grid(self) -> int:
        robot_pos = self.parse_robot()
        for move in self.moves:
            step = self.map_moves(move)
            next_pos = robot_pos + step
            cell = self.grid.get(next_pos, '#')
            if cell == '#':
                continue
            elif cell == '.':
                self.grid[robot_pos] = '.'
                self.grid[next_pos] = '@'
                robot_pos = next_pos
            elif cell == 'O':
                scan = next_pos
                while self.grid.get(scan, '#') == 'O':
                    scan += step
                if self.grid.get(scan, '#') == '#':
                    continue
                pos = scan
                while pos != next_pos:
                    prev = pos - step
                    self.grid[pos] = self.grid[prev]  
                    pos = prev
                self.grid[next_pos] = '@'
                self.grid[robot_pos] = '.'
                robot_pos = next_pos

    def boxes_sum(self) -> int:
        self.update_grid()
        result = 0
        for pos, char in self.grid.items():
            if char == 'O':
                result += 100 * int(pos.real) + int(pos.imag)
        return result

    @property
    def part_one(self) -> int:
        return self.boxes_sum()

    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day15_test.txt'
    PATH = 'inputs/day15.txt'
    with open(PATH, 'r') as f:
        data = f.read().split('\n\n')
    warehouse_woes = WarehouseWoes(data)
    ic(warehouse_woes.part_one)
    ic(warehouse_woes.part_two)