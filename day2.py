import pandas as pd
import os
# from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def possible_games(data: dict, bag):
    for keys, values in data.items():
        for sets in values:
            print(sets)




data_dict = {
'game1': [['3 blue', '4 red'], ['1 red', '2 green', '6 blue'], ['2 green']],
'game2': [['1 blue', '2 green'], ['3 green', '4 blue', '1 red'], ['1 green', '1 blue']],
'game3': [['8 green', '6 blue', '20 red'], ['5 blue', '4 red', '13 green'], ['5 green', '1 red']],
'game4': [['1 green', '3 red', '6 blue'], ['3 green', '6 red'], ['3 green', '15 blue', '14 red']],
'game5': [['6 red', '1 blue', '3 green'], ['2 blue', '1 red', '2 green']]
}

data_dict_sorted = {
'game1': [['4 red', '3 blue'], ['1 red', '2 green', '6 blue'], ['2 green']],
'game2': [['2 green', '1 blue'], ['1 red', '3 green', '4 blue'], ['1 green', '1 blue']],
'game3': [['20 red', '8 green', '6 blue'], ['4 red', '13 green', '5 blue'], ['1 red', '5 green']],
'game4': [['3 red', '1 green', '6 blue'], ['6 red', '3 green'], ['14 red', '3 green', '15 blue']],
'game5': [['6 red', '3 green' '1 blue'], ['1 red', '2 green', '2 blue']]
}


elf_bag = ['12 red', '13 green', '14 blue']

print(possible_games(data_dict, elf_bag))
