from dataclasses import dataclass
import os

from icecream import ic

@dataclass
class RockPaperScissors:
    _data: str
    
    def __post_init__(self):
        self.shape_map = self.create_shape_map()
        self.win_config = [('A', 'B'), ('B', 'C'), ('C', 'A')]
        self.lose_config = [('A', 'C'), ('B', 'A'), ('C', 'B')]
        self.part_one, self.part_two = self.total_score()

    def create_shape_map(self) -> dict[str, int]:
        '''A -> rock, B -> paper, C -> scissors'''
        shape = {'A': 1, 'B': 2, 'C': 3,
                 'X': 'A', 'Y': 'B', 'Z': 'C'}
        return shape
    
    def rules(self, players: tuple[str, str]) -> int:
        """lost -> 0, draw -> 3, win -> 6"""
        if players in self.win_config:
            return 6
        elif players in self.lose_config:
            return 0
        else:
            return 3
        
    def round_result(self, antagonist: str, protagonist: str) -> int:
        round_points = self.rules((antagonist, protagonist))
        shape_points = self.shape_map[protagonist]
        return round_points + shape_points
    
    def alter_round_result(self, antagonist: str, protagonist: str) -> int:
        '''X -> lose, Y -> draw, Z -> win'''
        round_poinst = 0
        shape_points = 0
        if protagonist == 'X':
            for config in self.lose_config:
                if config[0] == antagonist:
                    shape_points = self.shape_map[config[1]]
                    round_poinst = 0
        elif protagonist == 'Y':
            shape_points = self.shape_map[antagonist]
            round_poinst = 3
        else:
            for config in self.win_config:
                if config[0] == antagonist:
                    shape_points = self.shape_map[config[1]]
                    round_poinst = 6
        return round_poinst + shape_points
    
    def total_score(self) -> int:
        part_one_score = 0
        part_two_score = 0
        for round in self._data:
            antagonist, protagonist = round.split(' ')
            part_two_score += self.alter_round_result(antagonist, protagonist)
            protagonist = self.shape_map[protagonist]
            part_one_score += self.round_result(antagonist, protagonist)
        return part_one_score, part_two_score

    @property
    def part_one_sol(self) -> int:
        return self.part_one
    
    @property
    def part_two_sol(self) -> int:
        return self.part_two


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day2_test.txt'
    PATH = 'inputs/day2.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    rock_paper_rcissors = RockPaperScissors(data.split('\n'))
    ic(rock_paper_rcissors.part_one_sol)
    ic(rock_paper_rcissors.part_two_sol)
