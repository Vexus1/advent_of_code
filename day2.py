from dataclasses import dataclass
import os
import re

from icecream import ic

@dataclass
class CubeConundrum:
    data: list[str]

    def __post_init__(self):
        self.main_bag = {'red': 12, 'green': 13, 'blue': 14}
        self.data_colors, self.data_numbers = self.game_data_sets(self.data)

    def game_data_sets(self, 
                       data: str) -> tuple[list[list[str]], list[list[int]]]:
        data_colors = []
        data_numbers = []
        data_slice_index = data[0].index(':')
        for game in data:
            game = game[data_slice_index+2:]
            subsets = game.split(';')
            colors_list = []
            numbers_list = []
            for subset in subsets:
                colors = re.findall(r'\b(red|green|blue)\b', subset)
                numbers = re.findall(r'\d+', subset)
                numbers = list(map(int, numbers))
                colors_list.append(colors)
                numbers_list.append(numbers)
            data_colors.append(colors_list)
            data_numbers.append(numbers_list)
        return data_colors, data_numbers
    
    def win_or_lose(self, colors_list: list[list[str]],
                    numbers_list: list[list[str]]) -> list[bool]:
        for i in range(len(colors_list)):
            for j, color in enumerate(colors_list[i]):
                main_bag_value = self.main_bag[color]
                if numbers_list[i][j] > main_bag_value:
                    return False
        return True
    
    def games_score(self) -> list[bool]:
        games_results = []
        for i in range(len(self.data_colors)-1):
            result = self.win_or_lose(self.data_colors[i], self.data_numbers[i])
            games_results.append(result)
        return games_results
    
    def find_min_values(self, colors_list: list[list[str]],
                        numbers_list: list[list[str]]) -> int:
        min_red = 0
        min_green = 0
        min_blue = 0
        for i, color in enumerate(colors_list):
            for j in range(len(color)):
                if color[j] == 'red':
                    min_red = max(min_red, numbers_list[i][j])
                elif color[j] == 'green':
                    min_green = max(min_green, numbers_list[i][j])
                elif color[j] == 'blue':
                    min_blue = max(min_blue, numbers_list[i][j])
        min_value = min_red * min_green * min_blue
        return min_value
        
    def part_one_sol(self) -> int:
        games_results = self.games_score()
        win_games = 0
        for i, result in enumerate(games_results):
            if result is True:
                win_games += i+1
        return win_games
    
    def part_two_sol(self) -> int:
        min_value = 0
        for i in range(len(self.data_colors)):
            value = self.find_min_values(self.data_colors[i], self.data_numbers[i])
            min_value += value
        return min_value
                
if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day2_test.csv'
    PATH = 'inputs/day2.csv'
    with open(PATH, 'r') as f:
        data = f.read()
    cube_conundrum = CubeConundrum(data.split('\n'))
    ic(cube_conundrum.part_one_sol())
    ic(cube_conundrum.part_two_sol())
