import os 
from dataclasses import dataclass

from icecream import ic

@dataclass
class Trebuchet:
    _data: str

    def __post_init__(self):
        self.sol_one, self.sol_two = self.sum_calibration_values()

    @property
    def text_numbers(self) -> list[str]:
        text_list = ['one', 'two', 'three', 'four',
                     'five', 'six', 'seven', 'eight', 'nine']
        return text_list

    def sum_calibration_values(self) -> tuple[int, int]:
        calib_one = 0
        calib_two = 0
        for line in self._data:
            num = []
            num_text = []
            for i, char in enumerate(line):
                if char.isdigit():
                    num.append(char)
                    num_text.append(char)
                for j, text_num in enumerate(self.text_numbers):
                    if line[i:].startswith(text_num):
                        num_text.append(str(j+1))
            calib_one += int(num[0] + num[-1])
            calib_two += int(num_text[0] + num_text[-1])
        return calib_one, calib_two

    @property
    def part_one_sol(self) -> int:
        return self.sol_one
    
    @property
    def part_two_sol(self) -> int:
        return self.sol_two


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day1_test.txt'
    PATH = 'inputs/day1.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    trebuchet = Trebuchet(data.split('\n'))
    ic(trebuchet.part_one_sol)
    ic(trebuchet.part_two_sol)
