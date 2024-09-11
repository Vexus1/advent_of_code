import pandas as pd
import os
from collections import defaultdict
from copy import deepcopy

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Part One
class CamelCardsOne:
    def __init__(self, hands_dict: dict):
        self.hands_dict: dict = hands_dict
        self.ranks: list[str] = [str(n) for n in range(2, 10)] + list('TJQKA')
        self.cards: dict = {rank: i for i, rank in enumerate(self.ranks)}
        self.hand_len = len(list(self.hands_dict.keys())[0])
        
    def one_pair(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-1:
            return True

    def two_pair(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-2:
            rep_dict = defaultdict(int)
            for card in hand:
                rep_dict[card] += 1
            if sorted(list(rep_dict.values()), reverse=True)[:2] == [2, 2]:
                return True

    def three_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-2:
            rep_dict = defaultdict(int)
            for card in hand:
                rep_dict[card] += 1
            if sorted(list(rep_dict.values()), reverse=True)[:1] == [3]:
                return True
    
    def full_house(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-3:
            rep_dict = defaultdict(int)
            for card in hand:
                rep_dict[card] += 1
            if sorted(list(rep_dict.values()), reverse=True)[:2] == [3, 2]:
                return True

    def four_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-3:
            return True

    def five_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-4:
            return True

    def hands_type(self) -> list[dict]:
        high_card_dict = {}
        one_pair_dict = {}
        two_pair_dict = {}
        three_of_a_kind_dict = {}
        full_house_dict = {}
        four_of_a_kind_dict = {}
        five_of_a_kind_dict = {}
        for hand, hand_bit in self.hands_dict.items():
            if self.one_pair(hand) is True:
                one_pair_dict[hand] = hand_bit
            elif self.two_pair(hand) is True:
                two_pair_dict[hand] = hand_bit
            elif self.three_of_a_kind(hand) is True:
                three_of_a_kind_dict[hand] = hand_bit
            elif self.full_house(hand) is True:
                full_house_dict[hand] = hand_bit
            elif self.four_of_a_kind(hand) is True:
                four_of_a_kind_dict[hand] = hand_bit
            elif self.five_of_a_kind(hand) is True:
                five_of_a_kind_dict[hand] = hand_bit
            else:
                high_card_dict[hand] = hand_bit
        return [high_card_dict, one_pair_dict, two_pair_dict, three_of_a_kind_dict,
                full_house_dict, four_of_a_kind_dict, five_of_a_kind_dict]

    def sorted_by_ranks(self) -> list[list]:
        sorted_by_ranks = []
        hands_type = self.hands_type()
        def func(hand: str) -> tuple:
            return tuple(self.cards[card] for card in hand)

        for hand_type in hands_type:
            sorted_hand_type = sorted(hand_type, key=func)
            for hand in sorted_hand_type:
                sorted_by_ranks.append(hand_type[hand])
            
        return sorted_by_ranks

    def total_winnings(self) -> int:
        sort_by_ranks = self.sorted_by_ranks()
        return sum([bid*(i+1) for i, bid in enumerate(sort_by_ranks)])
    
# Part Two
class CamelCardsTwo:
    def __init__(self, hands_dict: dict):
        self.hands_dict = hands_dict
        self.high_card_dict = {}
        self.one_pair_dict = {}
        self.two_pair_dict = {}
        self.three_of_a_kind_dict = {}
        self.full_house_dict = {}
        self.four_of_a_kind_dict = {}
        self.five_of_a_kind_dict = {}
        self.ranks: list[str] = list('J') + [str(n) for n in range(2, 10)] + list('TQKA')
        self.cards: dict = {rank: i for i, rank in enumerate(self.ranks)}
        self.hand_len = len(list(self.hands_dict.keys())[0])
        
    def one_pair(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-1:
            return True

    def two_pair(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-2:
            rep_dict = defaultdict(int)
            for card in hand:
                rep_dict[card] += 1
            if sorted(list(rep_dict.values()), reverse=True)[:2] == [2, 2]:
                return True

    def three_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-2:
            rep_dict = defaultdict(int)
            for card in hand:
                rep_dict[card] += 1
            if sorted(list(rep_dict.values()), reverse=True)[:1] == [3]:
                return True
    
    def full_house(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-3:
            rep_dict = defaultdict(int)
            for card in hand:
                rep_dict[card] += 1
            if sorted(list(rep_dict.values()), reverse=True)[:2] == [3, 2]:
                return True

    def four_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-3:
            return True

    def five_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-4:
            return True
        
    def check_type(self, hand: str, hand_copy: str, hand_bit: int) -> None:
        if self.one_pair(hand_copy) is True:
            self.one_pair_dict[hand] = hand_bit
        elif self.two_pair(hand_copy) is True:
            self.two_pair_dict[hand] = hand_bit
        elif self.three_of_a_kind(hand_copy) is True:
            self.three_of_a_kind_dict[hand] = hand_bit
        elif self.full_house(hand_copy) is True:
            self.full_house_dict[hand] = hand_bit
        elif self.four_of_a_kind(hand_copy) is True:
            self.four_of_a_kind_dict[hand] = hand_bit
        elif self.five_of_a_kind(hand_copy) is True:
            self.five_of_a_kind_dict[hand] = hand_bit
        else:
            self.high_card_dict[hand] = hand_bit

    def hands_type(self) -> list[dict]:
        for hand, hand_bit in self.hands_dict.items():
            if 'J' in hand and 'JJJJJ' not in hand:
                rep_dict = defaultdict(int)
                for card in hand:
                    if card != 'J':
                        rep_dict[card] += 1
                most_common_card = list(rep_dict.keys())[list(rep_dict.values()).index(max(rep_dict.values()))]
                hand_copy = deepcopy(hand)
                hand_copy = [card for card in hand_copy]
                for i, card in enumerate(hand_copy):
                    if card == 'J':
                        hand_copy[i] = most_common_card
                hand_copy = ''.join(hand_copy)
                self.check_type(hand, hand_copy, hand_bit)
            else:
                self.check_type(hand, hand, hand_bit)
        return [self.high_card_dict, self.one_pair_dict, self.two_pair_dict, self.three_of_a_kind_dict,
                self.full_house_dict, self.four_of_a_kind_dict, self.five_of_a_kind_dict]

    def sorted_by_ranks(self) -> list[list]:
        sorted_by_ranks = []
        hands_type = self.hands_type()
        def func(hand: str) -> tuple:
            return tuple(self.cards[card] for card in hand)

        for hand_type in hands_type:
            sorted_hand_type = sorted(hand_type, key=func)
            for hand in sorted_hand_type:
                sorted_by_ranks.append(hand_type[hand])
        return sorted_by_ranks

    def total_winnings(self) -> int:
        sort_by_ranks = self.sorted_by_ranks()
        return sum([bid*(i+1) for i, bid in enumerate(sort_by_ranks)])
    

def data():
    df = pd.read_csv(f"inputs\day7.txt", delim_whitespace=True, header=None, names=["col1", "col2"])
    hands = df["col1"].tolist()
    hands_bit = df["col2"].tolist()
    hands_dict = {hands[i]: hands_bit[i] for i in range(len(hands))}
    return hands_dict

camel_cards = CamelCardsOne(data())
print(camel_cards.total_winnings())

camel_cards = CamelCardsTwo(data())
print(camel_cards.total_winnings())
