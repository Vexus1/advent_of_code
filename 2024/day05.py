import os 
from dataclasses import dataclass
from collections import defaultdict
import heapq

from icecream import ic # type: ignore

@dataclass
class PrintQueue:
    data: str

    def __post_init__(self):
        self.forward, self.backward, self.updates = self.eval_data()
        self.correct, self.incorrect = self.find_correct_incorrect()

    def eval_data(self) -> tuple[dict[int, set[int]],
                                 dict[int, set[int]],
                                 list[list[int]]]:
        first, second = self.data.split('\n\n')
        forward = defaultdict(set)
        backward = defaultdict(set)
        for line in first.splitlines():
            left, right = tuple(map(int, line.split('|')))
            forward[left].add(right)
            backward[right].add(left)
        updates = [[int(n) for n in line.split(',')] 
                   for line in second.splitlines()]
        return forward, backward, updates
    
    def is_correct(self, update: list[int]) -> bool:
        seen = set()
        in_update = set(update)
        for n1 in update:
            need = self.backward.get(n1)
            if need:
                for n2 in need:
                    if n2 in in_update and n2 not in seen:
                        return False
            seen.add(n1)
        return True
    
    def find_correct_incorrect(self) -> tuple[list[list[int]],
                                              list[list[int]]]:
        correct, incorrect = [], []
        for update in self.updates:
            (correct if self.is_correct(update) else incorrect).append(update)
        return correct, incorrect
    
    def topological_sorting(self, nodes: list[int]) -> list[int]:
        pos = {v: i for i, v in enumerate(nodes)}
        S = set(nodes)
        indeg = {v: 0 for v in nodes}
        adj = {v: set() for v in nodes}
        for a in nodes:
            for b in self.forward.get(a, ()):
                if b in S and b not in adj[a]:
                    adj[a].add(b)
                    indeg[b] += 1
        heap = [(pos[v], v) for v in nodes if indeg[v] == 0]
        heapq.heapify(heap)
        order = []
        while heap:
            _, v = heapq.heappop(heap)
            order.append(v)
            for w in adj[v]:
                indeg[w] -= 1
                if indeg[w] == 0:
                    heapq.heappush(heap, (pos[w], w))
        return order
    
    def count_middle(self, updates: list[list[int]]) -> int:
        return sum(u[(len(u) - 1) // 2] for u in updates)

    @property
    def part_one(self) -> int:
        return self.count_middle(self.correct)
    
    @property
    def part_two(self) -> int:
        fixed = [self.topological_sorting(update) 
                 for update in self.incorrect]
        return self.count_middle(fixed)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day05_test.txt'
    PATH = 'inputs/day05.txt'
    with open(PATH, 'r') as f:
        data = f.read().strip()
    print_queue  = PrintQueue(data)
    ic(print_queue.part_one)
    ic(print_queue.part_two)
