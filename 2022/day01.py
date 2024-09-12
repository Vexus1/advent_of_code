from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class CalorieCounting:
    data: list[str]
    
    def calc_elfs_calories(self) -> list[int]:
        calories = []
        elf_food = 0
        for line in self.data:
            if line.isdigit():
                elf_food += int(line)
            else:
                calories.append(elf_food)
                elf_food = 0
        calories.append(elf_food)
        return calories
    
    def sum_top(self, top_numbers: int) -> int:
        calories_sum = 0
        elfs_calories = self.calc_elfs_calories()
        for _ in range(top_numbers):
            max_calories = max(elfs_calories)
            calories_sum += max_calories
            elfs_calories.remove(max_calories)
        return calories_sum

    @property
    def part_one_sol(self) -> int:
        return self.sum_top(1)
    
    @property
    def part_two_sol(self) -> int:
        return self.sum_top(3)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day01_test.txt'
    PATH = 'inputs/day01.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    calorie_counting = CalorieCounting(data.split('\n'))
    ic(calorie_counting.part_one_sol)
    ic(calorie_counting.part_two_sol)
