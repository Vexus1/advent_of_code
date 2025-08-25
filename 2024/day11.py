import os
from dataclasses import dataclass
from collections import defaultdict

from icecream import ic  # type: ignore


@dataclass
class PlutonianPebbles:
    data: list[str]

    def __post_init__(self):
        self.initial_map = self.create_stones_map()

    def create_stones_map(self) -> defaultdict[int, int]:
        stones_map = defaultdict(int)
        for stone in self.data:
            stones_map[int(stone)] += 1
        return stones_map

    def stones_number(self, blink: int) -> int:
        stones_map = defaultdict(int, self.initial_map)
        for _ in range(blink): 
            updated_stones = defaultdict(int)
            for stone, c in stones_map.items():
                if stone == 0:
                    updated_stones[1] += c
                elif len(str(stone)) % 2 == 0:
                    d = len(str(stone))
                    half = 10 ** (d // 2)
                    left = stone // half
                    right = stone % half
                    updated_stones[left] += c
                    updated_stones[right] += c
                else:
                    updated_stones[stone * 2024] += c
            stones_map = updated_stones
        return sum(stones_map.values())

    @property
    def part_one(self) -> int:
        return self.stones_number(25)
    
    @property
    def part_two(self) -> int:
        return self.stones_number(75)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day11_test.txt'
    PATH = 'inputs/day11.txt'
    with open(PATH, 'r') as f:
        data = f.read().split(' ')
    plutonian_pebbles = PlutonianPebbles(data)
    ic(plutonian_pebbles.part_one)
    ic(plutonian_pebbles.part_two)
