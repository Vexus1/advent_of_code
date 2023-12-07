import pandas as pd
import os 
import string
# from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))
data = pd.read_csv(f"inputs/day3.txt", header=None)[0].to_list()

# PART ONE
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

data = pd.read_csv(f"inputs/day3.txt", header=None)[0].to_list()
data = ['467..114..',
        '*..*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..']

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

def remove_value_from_dict(key, value, dict):
    if key in dict:
        if value in dict[key]:
            dict[key].remove(value)

from copy import deepcopy

def solution():
    number_map = maping(data, [str(i) for i in range(10)])
    # print(number_map)
    star_map = maping(data, ['*'])
    symbols = [i for i in string.punctuation if i != '.']
    result = 0
    number_apperence = 0
    num1, num2 = None, None
    print(number_map)
    # print(list(number_map.keys())[1])
    # print([z for i in number_map.values() for j in i for z in j])
    number_map_copy = deepcopy(number_map)
    for key, value in star_map.items():
        number_apperence = 0
        for i in value:
            number_apperence = 0
            # print(value)
            num1, num2 = None, None
            cords1, cords2 = None, None
            number_map_copy = deepcopy(number_map)
            for j, k in neighbors(data, i).items():
                # number_apperence = 0
                # num1, num2 = None, None
                # cords1, cords2 = None, None
                # print(neighbors(data, i).items())
                for h in k:
                    if j.isdigit() and h in [z for i in number_map.values() for j in i for z in j]:
                        temp = find_key_by_value(number_map, h)
                        # print(temp)
                        if num1 is None:
                            num1 = temp
                        else:
                            num2 = temp

                        if cords1 is None:
                            cords1 = h
                        else:
                            cords2 = h
                        
                        # if num1 != None and num2 != None and cords1 != None and cords2 != None:
                        #     remove_value_from_dict(num1, cords1, number_map_copy)                   
                        #     remove_value_from_dict(num1, cords2, number_map_copy)
                        remove_value_from_dict(num1, cords1, number_map)
                        if num1 != num2:
                            number_apperence += 1
                if number_apperence == 2:
                    print(num1, num2)
                    # remove_value_from_dict(num1, cords1, number_map)                   
                    # remove_value_from_dict(num1, cords2, number_map)                            
                    result += (int(num1)*int(num2))
                    number_apperence = 0
                    num1, num2 = None, None
                    cords1, cords2 = None, None
    return result

print(solution())
