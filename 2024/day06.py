import os 
from dataclasses import dataclass

from icecream import ic # type: ignore

@dataclass
class GuardGallivant:
    data: list[str]

    def __post_init__(self):
        self.grid = self.create_grid()
        self.part_one, self.part_two = self.eval_results()

    def create_grid(self) -> dict[complex, str]:
        grid = {}
        for i, row in enumerate(self.data):
            for j, col in enumerate(row):
                position = complex(j, i)
                grid[position] = col
        return grid
    
    def starting_position(self) -> complex:
        return list(self.grid.keys())[list(self.grid.values()).index('^')]

    def start_walk(self, grid: dict[complex, str]) -> tuple[set[complex], bool]:
        pos = self.starting_position()
        dir = -1j
        seen = set()
        while pos in grid and (pos, dir) not in seen:
            seen |= {(pos, dir)}
            if grid.get(pos + dir) == '#':
                dir *= 1j
            else:
                pos += dir
        guard_path = {path for path, _ in seen}
        options = (pos, dir) in seen
        return guard_path, options
    
    def eval_results(self) -> tuple[int, int]:
        guard_path = self.start_walk(self.grid)[0]
        paradoxes = sum(self.start_walk(self.grid | {o: '#'})[1] 
                                        for o in guard_path)
        return len(guard_path), paradoxes


if __name__ == '__main__': 
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day06_test.txt'
    PATH = 'inputs/day06.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    guard_gallivant = GuardGallivant(data.split('\n'))
    ic(guard_gallivant.part_one)
    ic(guard_gallivant.part_two)
