from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class PointOfIncidence:
    data: list[str]

    def transpose(self, matrix: list[str]) -> list[str]:
        return list(map(''.join, zip(*matrix)))

    def rotate(self, matrix: list[str]) -> list[str]:
        return list(map(''.join, (zip(*matrix[::-1]))))
    
    def slide_rocks_north(self, data: list[str]) -> list[str]:
        data = self.transpose(data)
        for i, line in enumerate(data):
            while ".O" in line:
                line = line.replace(".O", "O.")
            data[i] = line
        return self.transpose(data)
    
    def calc_load(self, data: list[str]) -> int:
        loan = 0
        for i, line in enumerate(data[::-1], 1):
            for char in line:
                loan += i*(char=='O')
        return loan
    
    def spin_cycle(self, data: list[str]) -> list[str]:
        for _ in range(4):
            data = self.slide_rocks_north(data)
            data = self.rotate(data)
        return data
    
    def cycle_n_times(self, n: int) -> list[str]:
        data = list(self.data)  
        seen = {tuple(data)}  
        seen_list = [data]  
        grid_cycle = data
        for i in range(n):
            grid_cycle = self.spin_cycle(grid_cycle)
            if tuple(grid_cycle) in seen:
                break
            seen.add(tuple(grid_cycle)) 
            seen_list.append(grid_cycle)
        first_cycle_grid_index = seen_list.index(grid_cycle)
        target = (n - first_cycle_grid_index) % (i + 1 - first_cycle_grid_index) \
                  + first_cycle_grid_index
        final_grid = seen_list[target]
        return final_grid 

    @property
    def part_one_sol(self) -> int:
        slide_rocks = self.slide_rocks_north(self.data)
        return self.calc_load(slide_rocks)
    
    @property
    def part_two_sol(self) -> int:
        grid = self.cycle_n_times(n=10**9)        
        return self.calc_load(grid)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day14_test.txt'
    PATH = 'inputs/day14.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    point_of_incidence = PointOfIncidence(data.split('\n'))
    ic(point_of_incidence.part_one_sol)
    ic(point_of_incidence.part_two_sol)
