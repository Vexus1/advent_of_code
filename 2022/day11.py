from dataclasses import dataclass
import os
import re
from collections import deque
from functools import reduce
from operator import mul
from typing import Iterable

from icecream import ic  # type: ignore

@dataclass
class Monkey:
    monkey_number: int
    items: deque[int]
    operation_tuple: tuple[str, str]
    test: int
    accepted: int
    rejected: int

    def __post_init__(self):
        self.items_inspected = 0

    def update_inspected(self) -> None:
        self.items_inspected += 1

    def add_item(self, item: int) -> None:
        self.items.append(item)

    def remove_item(self) -> None:
        self.items.popleft()

    def modify_item(self, item: int) -> int:
        item = int(item)
        if self.operation_tuple[0] == '+':
            if self.operation_tuple[1].isdigit():
                item += int(self.operation_tuple[1]) 
            else:
                item += item
        elif self.operation_tuple[0] == '*':
            if self.operation_tuple[1].isdigit():
                item *= int(self.operation_tuple[1]) 
            else:
                item *= item
        return item

    def pass_to_another(self, item: int) -> tuple[int, int]:
        self.update_inspected()
        item = self.modify_item(item)
        item //= 3
        if item % self.test == 0:
            return item, self.accepted
        else:
            return item, self.rejected
        
    def pass_to_another_modulo(self, item: int, modulo: int) -> tuple[int, int]:
        self.update_inspected()
        item = self.modify_item(item)
        item %= modulo
        if item % self.test == 0:
            return item, self.accepted
        else:
            return item, self.rejected
        

@dataclass
class MonkeyintheMiddle:
    data: list[str]

    def __post_init__(self):
        self.monkeys: dict[int, Monkey]

    def prod(self, iterable: Iterable[int]) -> int:
        return reduce(mul, iterable, 1)

    def create_monkeys(self) -> dict[int, Monkey]:
        monkeys: list[Monkey] = []
        for line in self.data:
            if line.startswith('Monkey'):
                match = re.search(r'(\d+)', line)
                assert match is not None, "Monkey number pattern not found"
                monkey_number = int(match.group())
            elif line.startswith('  Starting'):
                items = deque(re.findall(r'(\d+)', line))
            elif line.startswith('  Operation'):
                operation = line.split('=')[1].strip()  
                match = re.search(r'([+*])\s*(\d+|\w+)', operation)
                assert match is not None, "Operation pattern not found"
                operator = match.group(1)
                element = match.group(2)
                operation_tuple = (operator, element) 
            elif line.startswith('  Test'):
                match = re.search(r'(\d+)', line)
                assert match is not None, "Test pattern not found"
                test = int(match.group())
            elif line.startswith('    If true'):
                match = re.search(r'(\d+)', line)
                assert match is not None, "Accepted pattern not found"
                accepted = int(match.group())
            elif line.startswith('    If false'):
                match = re.search(r'(\d+)', line)
                assert match is not None, "Rejected pattern not found"
                rejected = int(match.group())
            if line == '':
                monkeys.append(Monkey(monkey_number, items,
                                      operation_tuple, test, accepted, rejected))
        monkeys.append(Monkey(monkey_number, items,
                              operation_tuple, test, accepted, rejected))
        monkeys_dict = {i: monkey for i, monkey in enumerate(monkeys)}
        return monkeys_dict
    
    def count_inspected(self, rounds_number: int) -> list[int]:
        for _ in range(rounds_number):
            for monkey in self.monkeys.values():
                while monkey.items:
                    item = monkey.items[0]
                    item, moneky_number = monkey.pass_to_another(item)
                    self.monkeys[moneky_number].add_item(item)
                    monkey.remove_item()
        inspected_count = list(monkey.items_inspected 
                               for monkey in self.monkeys.values())
        return inspected_count
    
    def count_inspected_alter(self, rounds_number: int) -> list[int]:
        monkeys = self.monkeys.values()
        modulo = 1
        for monkey in monkeys:
            modulo *= monkey.test
        for _ in range(rounds_number):
            for monkey in monkeys:
                while monkey.items:
                    item = monkey.items[0]
                    item, moneky_number = monkey.pass_to_another_modulo(item, modulo)
                    self.monkeys[moneky_number].add_item(item)
                    monkey.remove_item()
        inspected_count = list(monkey.items_inspected 
                               for monkey in self.monkeys.values())
        return inspected_count
    
    def monkey_buisness(self, inspected_count: list[int], n: int) -> int:
        result = []
        for _ in range(n):
            best = max(inspected_count)
            result.append(best)
            best_index = inspected_count.index(best)
            inspected_count.pop(best_index)
        return self.prod(result)

    @property
    def part_one_sol(self) -> int:
        self.monkeys = self.create_monkeys()
        inspected_count = self.count_inspected(20)
        return self.monkey_buisness(inspected_count, 2)
    
    @property
    def part_two_sol(self) -> int:
        self.monkeys = self.create_monkeys()
        inspected_count = self.count_inspected_alter(10000)
        return self.monkey_buisness(inspected_count, 2)
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day11_test.txt'
    PATH = 'inputs/day11.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    monkey_in_the_Middle = MonkeyintheMiddle(data.split('\n'))
    ic(monkey_in_the_Middle.part_one_sol)
    ic(monkey_in_the_Middle.part_two_sol)
