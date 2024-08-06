from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class RockPaperScissors:
    _data: str
    
    def __post_init__(self):
        self.shape_map = self.create_shape_map()

    def create_shape_map(self) -> dict[str, int]:
        '''A -> rock, B -> paper, C -> scissors'''
        shape = {'A': 1, 'B': 2, 'C': 3,
                 'X': 'A', 'Y': 'B', 'Z': 'C'}
        return shape
    
    def rules(self, players: tuple[str, str]) -> int:
        """lost -> 0, draw -> 3, win -> 6"""
        if players == ('A', 'B') or players == ('B', 'C') or players == ('C', 'A'):
            return 6
        elif players == ('A', 'C') or players == ('B', 'A') or players == ('C', 'B'):
            return 0
        else:
            return 3
        
    def round_result(self, antagonist: str, protagonist: str) -> int:
        round_points = self.rules((antagonist, protagonist))
        shape_points = self.shape_map[protagonist]
        return round_points + shape_points
    
    def total_score(self) -> int:
        score = 0
        for round in self._data:
            antagonist, protagonist = round.split(' ')
            protagonist = self.shape_map[protagonist]
            score += self.round_result(antagonist, protagonist)
        return score

    @property
    def part_one_sol(self) -> int:
        return self.total_score()
    
    @property
    def part_two_sol(self) -> int:
        return 


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    PATH = 'inputs/day2_test.txt'
    PATH = 'inputs/day2.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    rock_paper_rcissors = RockPaperScissors(data.split('\n'))
    ic(rock_paper_rcissors.part_one_sol)
    ic(rock_paper_rcissors.part_two_sol)
