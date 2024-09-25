from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class BoilingBoulders:
    data: list[str]

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
        cubes = self.parse_cubes()
        for cube in cubes:
            for sides in self.locked_sides(cube):
                if sides not in cubes:
                    exposed += 1
        return exposed
    
    @property
    def part_one_sol(self) -> int:
        return self.surface_area()
    
    # @property
    # def part_two_sol(self) -> int:
    #     return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day18_test.txt' 
    PATH = 'inputs/day18.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    boiling_boulders = BoilingBoulders(data.split('\n'))
    ic(boiling_boulders.part_one_sol)
    # ic(boiling_boulders.part_two_sol)
