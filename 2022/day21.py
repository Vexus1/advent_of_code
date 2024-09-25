from dataclasses import dataclass
import os
from operator import add, sub, mul, truediv

from icecream import ic  # type: ignore

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

@dataclass(frozen=True)
class Monkey:
    number: float | None
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
        if monkey.number is not None:
            return monkey.number
        else:
            operand1 = self.monkey_number(monkey.operand_1)
            operand2 = self.monkey_number(monkey.operand_2)
            operator_func = OPERATORS[monkey.operator]
            return operator_func(operand1, operand2)

    def gradient_descent(self) -> int:
        prev_number = self.monkeys_dict['humn'].number
        self.monkeys_dict['root'] = Monkey(None,
                                           self.monkeys_dict['root'].operand_1,
                                           '-',
                                           self.monkeys_dict['root'].operand_2)
        target = self.monkey_number('root')
        prev_error = int(target)
        humn_number = 0
        self.monkeys_dict['humn'] = Monkey(humn_number, None, None, None)
        target = self.monkey_number('root')
        error = int(target)
        learning_rate = 0.1
        while error > 0.1:
            try:
                gradient = (humn_number - prev_number) // (error - prev_error)
            except ZeroDivisionError:
                if error < prev_error:
                    gradient = 1
                else:
                    gradient = -1
            prev_number = humn_number
            prev_error = error
            humn_number -= learning_rate * error * gradient
            self.monkeys_dict['humn'] = Monkey(humn_number, None, None, None)
            target = self.monkey_number('root')
            error = int(target)
        return round(humn_number)

    @property
    def part_one_sol(self) -> int:
        return int(self.monkey_number('root'))

    @property
    def part_two_sol(self) -> int:
        return self.gradient_descent()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day21_test.txt' 
    PATH = 'inputs/day21.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    monkey_math = MonkeyMath(data.split('\n'))
    ic(monkey_math.part_one_sol)
    ic(monkey_math.part_two_sol)
