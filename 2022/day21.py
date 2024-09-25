from dataclasses import dataclass
import os
from operator import add, sub, mul, truediv

from icecream import ic  # type: ignore

@dataclass(frozen=True)
class Monkey:
    number: int | None
    operand_1: str | None
    operator: str | None
    operand_2: str | None


@dataclass
class MonkeyMath:
    data: list[str]

    def __post_init__(self):
        self.monkeys_dict = self.parse_monkeys()

    def parse_monkeys(self) -> dict[str, Monkey]:
        monkeys_dict = {}
        for line in self.data:
            monkey: Monkey
            name, yell = line.split(": ")
            if yell.isdigit():
                monkey = Monkey(int(yell), None, None, None)
            else:
                operand_1, operator, operand_2 = yell.split()
                monkey = Monkey(None, operand_1, operator, operand_2)
            monkeys_dict[name] = monkey
        return monkeys_dict

    def monkey_number(self, name: str) -> int:
        monkey = self.monkeys_dict[name]
        if monkey.number:
            return monkey.number
        else:
            operand1 = self.monkey_number(monkey.operand_1)
            operand2 = self.monkey_number(monkey.operand_2)
            operator_func = {'+': add,
                             '-': sub,
                             '*': mul,
                             '/': truediv}[monkey.operator]
            return operator_func(operand1, operand2)

    @property
    def part_one_sol(self) -> int:
        return int(self.monkey_number('root'))

    # @property
    # def part_two_sol(self) -> int:
    #     return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day21_test.txt' 
    PATH = 'inputs/day21.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    monkey_math = MonkeyMath(data.split('\n'))
    ic(monkey_math.part_one_sol)
    # ic(monkey_math.part_two_sol)
