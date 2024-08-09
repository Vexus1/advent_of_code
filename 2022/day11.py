from dataclasses import dataclass
import os
from typing import NamedTuple
import re

from icecream import ic

@dataclass
class Monkey:
    monkey_number: int
    items: list[int]
    operation: tuple[str, str]
    test: int
    accepted: int
    rejected: int

    def __post_init__(self):
        self.items_inspected = len(self.items)

    def update_items(self, item: int) -> None:
        self.items.append(item)

    def modify_item(self, item: int) -> int:
        item = int(item)
        if self.operation[0] == '+':
            if self.operation[1].isdigit():
                item += int(self.operation[1]) 
            else:
                item += item
        elif self.operation[0] == '*':
            ic(item)
            if self.operation[1].isdigit():
                item *= int(self.operation[1]) 
            else:
                item *= item
                ic(item)
        return item

    def pass_to_another(self, item: int) -> tuple[int, int]:
        item = self.modify_item(item)
        # ic(item)
        # ic(self.accepted, self.rejected)
        if item % self.test == 0:
            return item // 3, self.accepted
        else:
            return item // 3, self.rejected


@dataclass
class MonkeyintheMiddle:
    _data: list[str]

    def __post_init__(self):
        self.monkeys = self.create_monkeys()

    def create_monkeys(self) -> dict[int, Monkey]:
        monkeys = []
        for line in self._data:
            if line.startswith('Monkey'):
                monkey_number = int(re.search(r'(\d+)', line).group())
            elif line.startswith('  Starting'):
                items = list(re.findall(r'(\d+)', line))
            elif line.startswith('  Operation'):
                _, operation = line.split('=') 
                operation = re.search(r'([+*])\s*(\d+|\w+)', operation)
                operator = operation.group(1)
                element = operation.group(2)
                operation = (operator, element)
            elif line.startswith('  Test'):
                test = int(re.search(r'(\d+)', line).group())
            elif line.startswith('    If true'):
                accepted = int(re.search(r'(\d+)', line).group())
            elif line.startswith('    If false'):
                rejected = int(re.search(r'(\d+)', line).group())
            if line == '':
                monkeys.append(Monkey(monkey_number, items,
                                      operation, test, accepted, rejected))
        monkeys.append(Monkey(monkey_number, items,
                                    operation, test, accepted, rejected))
        monkeys = {i: monkey for i, monkey in enumerate(monkeys)}
        return monkeys
    
    def count_inspected(self, rounds_number: int) -> list[int]:
        for _ in range(rounds_number):
            for monkey in self.monkeys.values():
                for item in monkey.items:
                    # ic(monkey)
                    item, moneky_number = monkey.pass_to_another(item)
                    # ic(item, moneky_number)
                    self.monkeys[moneky_number].update_items(item)
        # ic([monkey.items for monkey in self.monkeys.values()])
        inspected_items = list(monkey.items_inspected for monkey in self.monkeys.values())
        return inspected_items

    @property
    def part_one_sol(self) -> int:
        return self.count_inspected(1)
    
    @property
    def part_two_sol(self) -> int:
        return
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day11_test.txt'
    # PATH = 'inputs/day11.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    monkey_in_the_Middle = MonkeyintheMiddle(data.split('\n'))
    ic(monkey_in_the_Middle.part_one_sol)
    ic(monkey_in_the_Middle.part_two_sol)
