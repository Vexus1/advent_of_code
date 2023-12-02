import pandas as pd
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
data = pd.read_csv(f"input.txt", header=None)[0].to_list()

# PART ONE
def two_pointers(word):
    first, last = None, None
    i = 0
    j = len(word)-1
    while i <= j:
        try:
            first = int(word[i])
        except:
            i += 1
        try:
            last = int(word[j])
        except:
            j -= 1

        if first is not None and last is not None:
            return int(str(first) + str(last))

print(sum([two_pointers(i) for i in data]))

# PART TWO 
str_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def two_pointers(word):
    min_len_numbers = min([len(i) for i in str_numbers.keys()])
    max_len_numbers = max([len(i) for i in str_numbers.keys()])
    str_number_left, str_number_right = '', ''
    first, last = None, None
    i = 0
    j = len(word)-1
    while i <= j:
        if type(first) is not int:
            try:
                first = int(word[i])
            except:
                str_number_left += word[i]
                if len(str_number_left) > max_len_numbers:
                    str_number_left = str_number_left[1:]
                for k in range(0, max_len_numbers-min_len_numbers+1):
                    if str_number_left[k:] in str_numbers.keys():
                        first = str_numbers[str_number_left[k:]]
                i += 1
                
        if type(last) is not int:
            try:
                last = int(word[j])
            except:
                str_number_right += word[j]
                if len(str_number_right) > max_len_numbers:
                    str_number_right = str_number_right[1:]
                for k in range(0, max_len_numbers-min_len_numbers+1):
                    if (str_number_right[k:])[::-1] in str_numbers.keys():
                        last = str_numbers[(str_number_right[k:])[::-1]]
                j -= 1

        if first is not None and last is not None:
            return int(str(first) + str(last))
        
print(sum([two_pointers(i) for i in data]))

