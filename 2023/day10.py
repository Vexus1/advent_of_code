import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PipeMaze:
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
    
    def result(self):
            route_len = 1
            area = 0
            current_neigbors = self._neighbors(self.starting_position)
            position = []
            characters_map = self._characters_map()
            previous = None
            while position != self._starting_position() or route_len == 1:
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
                            step = [self._moves[i][0], self._moves[i][1]]
                            previous = self._moves.index([step[0]*(-1), step[1]*(-1)])
                            position = [position[0] + step[0], position[1] + step[1]]
                    area += position[1]*step[0]
                else:
                    for j, h in enumerate((2,3,0,1)):
                        if current_neigbors[j][h] is True:
                            step = [self._moves[j][0], self._moves[j][1]]
                            previous = self._moves.index([step[0]*(-1), step[1]*(-1)])
                            position = [self.starting_position[0] + step[0], self.starting_position[1] + step[1]]
                            area += position[1]*step[0]
                            break
                current_neigbors = self._neighbors(position)
                route_len += 1
            return f'Part one: {route_len//2}, Part Two: {abs(area)-route_len//2+1}'

    
data = pd.read_csv(f"inputs/day10.txt", header=None)[0].to_list()
data = [[j for j in i] for i in data]

pipe_maze = PipeMaze(data)
print(pipe_maze.result())
