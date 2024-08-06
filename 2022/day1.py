from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class CalorieCounting:
    _data: str

    @property
    def find_most_calories(self) -> int:
        most_calories = float('-inf')
        elf_food = 0
        for line in self._data:
            if line.isdigit():
                elf_food += int(line)
            else:
                most_calories = max(most_calories, elf_food)
                elf_food = 0
        return most_calories

    @property
    def part_one_sol(self) -> int:
        return self.find_most_calories
    
    @property
    def part_two_sol(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day1_test.txt'
    PATH = 'inputs/day1.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    calorie_counting = CalorieCounting(data.split('\n'))
    ic(calorie_counting.part_one_sol)
    ic(calorie_counting.part_two_sol)
