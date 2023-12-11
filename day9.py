import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MirageMaintenance:
    def __init__(self, data: list):
        self.data = data
        self.part_one_result: int = 0
        self.part_two_result: int = 0
        self._modify_data()

    def _modify_data(self):
        for i, seq in enumerate(self.data):
            new_arr = []
            value = ''
            for j in seq:
                if j != ' ':
                    value += str(j)
                else:
                    new_arr.append(int(value))
                    value = ''
            new_arr.append(int(value))
            self.data[i] = new_arr
                    
    def extrapolated_values(self) -> int:
        next_value_in_all_one = []
        next_value_in_all_two = []
        for seq in self.data:
            next_value_one = 0
            next_value_two = 0
            temp = [seq]
            diff = []
            while set(diff) != {0}:
                diff = []
                for i in range(len(seq)-1):
                    diff.append(seq[i+1]-seq[i])
                seq = diff
                temp.append(diff)
            for i in range(len(temp)-1, -1, -1):
                next_value_one += temp[i][-1]
                next_value_two = (temp[i][0] - next_value_two)
            next_value_in_all_one.append(next_value_one)
            next_value_in_all_two.append(next_value_two)
        return sum(next_value_in_all_one), sum(next_value_in_all_two)

data = pd.read_csv(f"inputs/day9.txt", header=None)[0].to_list()
mirage_maintenance = MirageMaintenance(data)
print(mirage_maintenance.extrapolated_values())
