import os 
from dataclasses import dataclass
from collections import defaultdict

from icecream import ic # type: ignore

@dataclass
class PrintQueue:
    data: str

    def __post_init__(self):
        self.rules, self.updates = self.eval_data()

    def eval_data(self) -> tuple[list[dict[int, list[int]]], list[list[int]]]:
        first, second = self.data.split('\n\n')
        rules = defaultdict(list)
        updates = []
        for line in first.splitlines():
            left, right = line.split('|')
            rules[int(left)].append(int(right))
        for line in second.splitlines():
            updates.append([int(l) for l in line.split(',')])
        return rules, updates
    
    def correct_order(self, update: list[int]) -> bool:
        for i, n1 in enumerate(update):
            for n2 in update[i + 1:]:
                if n1 in self.rules[n2]:
                    return False
        return True
    
    def count_middle(self) -> int:
        result = 0
        for update in self.updates:
            if self.correct_order(update):
                result += update[(len(update) - 1) // 2]
        return result

    @property
    def part_one(self) -> int:
        return self.count_middle()
    
    @property
    def part_two(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day05_test.txt'
    PATH = 'inputs/day05.txt'
    with open(PATH, 'r') as f:
        data = f.read().strip()
    print_queue  = PrintQueue(data)
    ic(print_queue.part_one)
    # ic(print_queue.part_two)
