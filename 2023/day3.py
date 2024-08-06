import pandas as pd
import os 
import string
from copy import deepcopy

os.chdir(os.path.dirname(os.path.abspath(__file__)))
data = pd.read_csv(f"inputs/day3.txt", header=None)[0].to_list()

def maping(data, key):
    number = ''
    values =  []
    map = {}
    for i, string in enumerate(data):
        for j, char in enumerate(string):
            if char in key:
                number += char
                values.append([i, j])
            elif char not in key and number != '':
                if number in map.keys():
                    map[number] += [values]
                else:
                    map[number] = [values]
                number = ''
                values = []
            if j == len(string)-1:
                if number != '':
                    if number in map.keys():
                        map[number] += [values]
                    else:
                        map[number] = [values]
                number = ''
                values = []
                
    return map

# PART ONE
def neighbors(data, index):
    arr = []
    i, j = index[0][0], index[0][1]
    for x in range(-1,2):
        for y in range(-1, len(index)+1):
            if i+x in range(len(data)) and j+y in range(len(data[0])):
                arr.append(data[i+x][j+y])
    return arr

def solution():
    number_map = maping(data, [str(i) for i in range(10)])
    symbols = [i for i in string.punctuation if i != '.']
    result = 0
    for key, value in number_map.items():
        for i in value:
            for j in neighbors(data, i):
                if j in symbols:
                    result += int(key)
    return result

print(solution())


# PART TWO
def neighbors(data, index):
    dict = {}
    i, j = index[0][0], index[0][1]
    for x in range(-1,2):
        for y in range(-1, len(index)+1):
            if i+x in range(len(data)) and j+y in range(len(data[0])):
                if data[i+x][j+y] in dict.keys():
                    dict[data[i+x][j+y]] += [[i+x, j+y]]
                else:
                    dict[data[i+x][j+y]] = [[i+x, j+y]]
    return dict

def find_key_by_value(d, value_to_find):
    for key, value in d.items():
        for i in value:
            for j in i:
                if j == value_to_find:
                    return key
    return None

def remove_value_from_dict(key, value, dict: dict):
    if key in dict:
        for i in dict.values():
            for j in i:
                for k in j:
                    if value in j:
                        dict[key].remove(j)

def solution():
    number_map = maping(data, [str(i) for i in range(10)])
    star_map = maping(data, ['*'])
    result = 0
    number_map_copy = deepcopy(number_map)
    for value in star_map.values():
        number_apperence = 0
        for i in value:
            number_apperence = 0
            num1, num2 = None, None
            cords1, cords2 = None, None
            number_map_copy = deepcopy(number_map)
            for j, k in neighbors(data, i).items():
                for h in k:
                    if j.isdigit() and h in [z for i in number_map_copy.values() for j in i for z in j]:
                        temp = find_key_by_value(number_map_copy, h)
                        if num1 is None:
                            num1 = temp
                        else:
                            num2 = temp

                        if cords1 is None:
                            cords1 = h
                        else:
                            cords2 = h  
                        try:             
                            remove_value_from_dict(num1, cords1, number_map_copy)
                            remove_value_from_dict(num2, cords2, number_map_copy)
                        except:
                            None
                        number_apperence += 1
                if number_apperence == 2:                    
                    result += (int(num1)*int(num2))
                    number_apperence = 0
                    num1, num2 = None, None
                    cords1, cords2 = None, None
    return result

print(solution())
