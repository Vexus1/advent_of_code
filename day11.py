import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CosmicExpansion:
    def __init__(self, data: list[list[str]]):
        self.data = data


data = pd.read_csv("inputs/day11_test.txt", header=None)[0].to_list()
cosmic_expansion = CosmicExpansion(data)
