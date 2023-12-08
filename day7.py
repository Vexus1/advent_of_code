import pandas as pd
import os
from dataclasses import dataclass
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Solution:
    def __init__(self, hands: list[str], hands_bit: list[str]):
        self.hands = hands
        self.hands_bit = hands_bit
        self.ranks: list[str] = [str(n) for n in range(2, 11)] + list('JQKA')
        self.cards: dict = {rank: i for i, rank in enumerate(self.ranks)}
        self.hand_len = len(self.hands[0])
        
    def one_pair(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-1:
            return True

    def two_pair(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-2:
            rep_dict = defaultdict(str)
            for card in hand:
                rep_dict[card] += 1
            if sorted(rep_dict.values())[:2] == [2, 2]:
                True

    def three_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-2:
            rep_dict = defaultdict(str)
            for card in hand:
                rep_dict[card] += 1
            if sorted(rep_dict.values())[:1] == [3]:
                True
    
    def full_house(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-2:
            rep_dict = defaultdict(str)
            for card in hand:
                rep_dict[card] += 1
            if sorted(rep_dict.values())[:2] == [3, 2]:
                True

    def four_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-3:
            return True

    def five_of_a_kind(self, hand: str) -> bool:
        if len(set(hand)) == self.hand_len-4:
            return True

    # def stronger_card(self, hand: str) -> :

    # def rank_hands(self) -> dict:
    #     for hand in hands:
    #         if self.one_pair(hand) is True:

    #         if self.two_pair(hand) is True:

    #         if self.three_of_a_kind(hand) is True:

    #         if self.full_house(hand) is True:

    #         if self.four_of_a_kind(hand) is True:

    #         if self.five_of_a_kind(hand) is True:
            
    #         else:




        
hands_bit = [765, 684, 28, 220, 483]
hands = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']