import pandas as pd
import os
from collections import defaultdict
from math import ceil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Part One
class PipeMazeOne:
    def __init__(self, data: list[str]):
        self._data = data
        self._moves = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        self.starting_position = self._starting_position() 

    def _starting_position(self):
        for i, row in enumerate(self._data):
            for j, col in enumerate(row):
                if col == 'S':
                    return [i, j]
                
    def _characters_map(self):
        '''Map == [[left], [up], [right], [down]] where:
        - | is a vertical pipe connecting north and south.
        - - is a horizontal pipe connecting east and west.
        - L is a 90-degree bend connecting north and east.
        - J is a 90-degree bend connecting north and west.
        - 7 is a 90-degree bend connecting south and west.
        - F is a 90-degree bend connecting south and east.
        - . is ground; there is no pipe in this tile.
        - S is the starting position of the animal; there is a pipe on this tile,
            but your sketch doesn't show what shape the pipe has.'''
        
        map = {'S': [True, True, True, True],
               '|': [False, True, False, True],
               '-': [True, False, True, False],
               'L': [False, True, True, False],
               'J': [True, True, False, False],
               '7': [True, False, False, True],
               'F': [False, False, True, True],
               '.': [False, False, False, False]}
        return map

    def _neighbors(self, index: list[int]) -> list[str]:
        row, col = index[0], index[1]
        neighbors = []
        for i in (-1, 1):
            if i+col in range(len(self._data[0])):
                neighbors.append(self._data[row][i+col])
            else:
                neighbors.append(' ')
            if i+row in range(len(self._data)):
                neighbors.append(self._data[i+row][col])
            else:
                neighbors.append(' ')
        return neighbors
    
    def find_route_len(self):
        route_len = 1
        current_neigbors = self._neighbors(self.starting_position)
        position = []
        characters_map = self._characters_map()
        previous = None
        while position != self._starting_position():
            for i, neighbor in enumerate(current_neigbors):
                if neighbor != ' ':
                    current_neigbors[i] = characters_map[neighbor]
                else:
                    current_neigbors[i] = [False, False, False, False]
            if position:
                char_by_pos = self._data[position[0]][position[1]]
                char_by_pos = characters_map[char_by_pos][:]
                char_by_pos[previous] = False 
                for i, bool in enumerate(char_by_pos):
                    if bool is True:
                        previous = self._moves.index([j*(-1) for j in self._moves[i]])
                        position = [position[j] + self._moves[i][j] for j in range(len(position))]
            else:
                for j, h in enumerate((2,3,0,1)):
                    if current_neigbors[j][h] is True:
                        previous = self._moves.index([i*(-1) for i in self._moves[j]])
                        position = [self.starting_position[g] + self._moves[j][g] for g in range(len(self.starting_position))]
                        break
            current_neigbors = self._neighbors(position)
            
            route_len += 1
        return ceil(route_len/2)-1

# Part Two
class PipeMazeTwo(PipeMazeOne):
    def __init__(self, data: list[str]):
        super().__init__(data)
        self.route = self._route_coordinates()

    def _route_coordinates(self) -> list[list[int]]:
        position = []
        route_coordinates = []
        current_neigbors = self._neighbors(self.starting_position)
        characters_map = self._characters_map()
        previous = None
        while position != self._starting_position():
            for i, neighbor in enumerate(current_neigbors):
                if neighbor != ' ':
                    current_neigbors[i] = characters_map[neighbor]
                else:
                    current_neigbors[i] = [False, False, False, False]
            if position:
                char_by_pos = self._data[position[0]][position[1]]
                char_by_pos = characters_map[char_by_pos][:]
                char_by_pos[previous] = False 
                for i, bool in enumerate(char_by_pos):
                    if bool is True:
                        previous = self._moves.index([j*(-1) for j in self._moves[i]])
                        position = [position[j] + self._moves[i][j] for j in range(len(position))]
            else:
                for j, h in enumerate((2,3,0,1)):
                    if current_neigbors[j][h] is True:
                        previous = self._moves.index([i*(-1) for i in self._moves[j]])
                        position = [self.starting_position[g] + self._moves[j][g] for g in range(len(self.starting_position))]
                        break
            current_neigbors = self._neighbors(position)
            route_coordinates.append(position)
        return route_coordinates
    
    def _change_data(self):
        for i, row in enumerate(self._data):
            for j in range(len(row)):
                if [i, j] not in self.route:
                    temp = [self._data[i][j] for j in range(len(self._data[i]))]
                    temp[j] = '.'
                    self._data[i] = ''.join(temp)
    
    # def _change_s_in_data(self):

    
    # def titles_enclosed(self) -> int:
    #     route_coordinates = self._route_coordinates()
    #     count = 0
    #     previous = []
    #     current = []
    #     print(route_coordinates)
    #     for i, row in enumerate(self._data):
    #         for j, col in enumerate(row):
    #             if route_coordinates and len(route_coordinates)>1:
    #                 if [i, j] == route_coordinates[0]:
    #                     previous = [i, j]
    #                 if [i, j] == route_coordinates[1]:
    #                     current = [i, j]
    #                     if len(self._data[previous[0]][previous[1]+1:current[1]]) == 0:
    #                         # print('0')
    #                         # print(self._data[previous[0]][previous[1]+1:current[1]])
    #                         route_coordinates = route_coordinates[1:]
    #                         previous = current
    #                         current = []
    #                     else:
    #                         # print('>1')
    #                         # print(self._data[previous[0]][previous[1]+1:current[1]])
    #                         count += len(self._data[previous[0]][previous[1]+1:current[1]])
    #                         route_coordinates = route_coordinates[2:]
    #                         previous = []
    #                         current = []
    #         if previous:
    #             route_coordinates = route_coordinates[1:]
    #             previous = []
    #         previous = []
    #         current = []
        
    #     return count


# data = ['FFF7F',
#         '.FJ|F',
#         'SJ.L7',
#         '|F--J',
#         'LJFFF']
# data = ['FF7FSF7F7F7F7F7F---7',
#         'L|LJ||||||||||||F--J',
#         'FL-7LJLJ||||||LJL-77',
#         'F--JF--7||LJLJ7F7FJ-',
#         'L---JF-JLJ.||-FJLJJ7',
#         '|F|F-JF---7F7-L7L|7|',
#         '|FFJF7L7F-JF7|JL---7',
#         '7-L-JL7||F7|L7F-7F7|',
#         'L.L7LFJ|||||FJL7||LJ',
#         'L7JLJL-JLJLJL--JLJ.L']

data = ['..........',
        '.S------7.',
        '.|F----7|.',
        '.||....||.',
        '.||....||.',
        '.|L-7F-J|.',
        '.|..||..|.',
        '.L--JL--J.',
        '..........']

# data = ['.F----7F7F7F7F-7....',
#         '.|F--7||||||||FJ....',
#         '.||.FJ||||||||L7....',
#         'FJL7L7LJLJ||LJ.L-7..',
#         'L--J.L7...LJS7F-7L7.',
#         '....F-J..F7FJ|L7L7L7',
#         '....L7.F7||L7|.L7L7|',
#         '.....|FJLJ|FJ|F7|.LJ',
#         '....FJL-7.||.||||...',
#         '....L---J.LJ.LJLJ...']
# data = pd.read_csv(f"inputs/day10.txt", header=None)[0].to_list()
# data = [[j for j in i] for i in data]

pipe_maze = PipeMazeTwo(data)
print(pipe_maze._change_data())
