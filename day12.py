import pandas as pd
import os
from collections import defaultdict

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class HotSprings:
    def __init__(self, trace: str):
        self.data = self.store_data(trace)

    def store_data(self, trace: str) -> dict[str: list[int]]:
        df = pd.read_csv(trace, delim_whitespace=True, header=None, names=["col1", "col2"])
        records = df["col1"].tolist()
        brokens = df["col2"].tolist()
        brokens = [[int(i) for i in j if i != ","] for j in brokens]
        data = {records[i]: brokens[i] for i in range(len(records))}
        return data

    def find_arrangements(self):
        for records, brokens in self.data.items():
            count_springs = defaultdict(int)
            for spring in records:
                count_springs[spring] += 1

            print(count_springs)




hot_springs = HotSprings("inputs\day12_test.txt")
print(hot_springs.find_arrangements())


