from collections import deque
from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class BoilingBoulders:
    data: list[str]

    def __post_init__(self):
        self.cubes = self.parse_cubes()
        self.min_range, self.max_range = self.create_ranges()

    def parse_cubes(self) -> list[tuple[int, int, int]]:
        return [tuple(map(int, line.split(','))) for line in self.data] 
    
    def locked_sides(self, cube: tuple[int, int, int]) \
                     -> set[tuple[int, int, int]]:
        neighbors = {(1, 0, 0), (0, 1, 0), (0, 0, 1),
                     (-1, 0, 0), (0, -1, 0), (0, 0, -1)}
        sides = {tuple(c + s for c, s in zip(cube, side))
                 for side in neighbors}
        return sides

    def surface_area(self) -> int:
        exposed = 0
        for cube in self.cubes:
            for sides in self.locked_sides(cube):
                if sides not in self.cubes:
                    exposed += 1
        return exposed
    
    def create_ranges(self) -> tuple[list[int, int, int],
                                     list[int, int, int]]:
        min_range = [min(c[i] - 1 for c in self.cubes) for i in range(3)]
        max_range = [max(c[i] + 1 for c in self.cubes) for i in range(3)]
        return min_range, max_range
    
    def in_space(self, cube: tuple[int, int, int]) -> bool:
        return all(self.min_range[i] <= cube[i] <= self.max_range[i]
                   for i in range(3))
    
    def exterior_surface_area(self) -> int:
        '''BFS'''
        exposed = 0
        seen = set()
        q: deque[tuple[int, int, int]] = deque()
        q.append(tuple(self.min_range))
        while q:
            cube = q.popleft()
            if cube in self.cubes:
                exposed += 1
                continue
            if cube not in seen:
                seen.add(cube)
                for sides in self.locked_sides(cube):
                    if self.in_space(sides):
                        q.append(sides)
        return exposed

    @property
    def part_one_sol(self) -> int:
        return self.surface_area()
    
    @property
    def part_two_sol(self) -> int:
        return self.exterior_surface_area()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day18_test.txt' 
    PATH = 'inputs/day18.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    boiling_boulders = BoilingBoulders(data.split('\n'))
    ic(boiling_boulders.part_one_sol)
    ic(boiling_boulders.part_two_sol)
