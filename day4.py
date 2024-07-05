from dataclasses import dataclass
import os

import pandas as pd
from pandas import DataFrame
from icecream import ic

@dataclass
class Scratchcards:
    data: DataFrame

    def clear_data(self) -> list[list[int]]:
        data = self.data.to_numpy()
        all_nums = []
        slice_index = [i for i in data[0][0]].index(':')
        for row in data:
            nums = []
            str_occ = 0
            num = ''
            row = row[0][slice_index+2:]
            if row[0] == ' ':
                row = row[1:]
            for col in row:
                try:
                    int(col)
                    num += col
                    str_occ = 0
                except:
                    str_occ += 1
                    if str_occ == 1:
                        nums.append(int(num))
                        num = ''
            nums.append(int(num))
            all_nums.append(nums)
        return all_nums

    def count_points(self) -> int:
        data = self.clear_data()
        count = 0
        for nums in data:
            eq_nums = len(nums) - len(set(nums))
            if eq_nums < 2:
                count += 2**eq_nums - 1
            else:
                count += 2**(eq_nums-1)
        return count

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    data = pd.read_csv('inputs/day4.csv', header=None)
    scratchcards = Scratchcards(data)
    ic(scratchcards.count_points())
