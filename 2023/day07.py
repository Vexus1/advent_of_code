import os 
from dataclasses import dataclass

from icecream import ic  # type: ignore  

@dataclass
class CamelCards:
    data: list[str]

    def eval_line(self, hand: str, trans: str) -> tuple[str, list[int]]:
        trans_table = str.maketrans('TJQKA', trans)
        hand = hand.translate(trans_table)
        best = max(self.rank_hands(hand.replace('0', r)) for r in hand)
        return hand, best
    
    def rank_hands(self, hand: str) -> list[int]:
        return sorted(map(hand.count, hand), reverse=True)

    def count_total_winnings(self, trans: str) -> int:
        data = []
        for line in self.data:
            hand, bid = line.split()
            hand, best = self.eval_line(hand, trans)
            data.append((best, hand, int(bid)))
        total_winnings = sum(i * bid for i, (*_, bid) in 
                             enumerate(sorted(data), start=1))
        return total_winnings

    @property
    def part_one_sol(self) -> int:
        trans = 'ABCDE'
        return self.count_total_winnings(trans)
    
    @property
    def part_two_sol(self) -> int:
        trans = 'A0CDE'
        return self.count_total_winnings(trans)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day07_test.txt'
    PATH = 'inputs/day07.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    camel_cards = CamelCards(data.split('\n'))
    ic(camel_cards.part_one_sol)
    ic(camel_cards.part_two_sol)
