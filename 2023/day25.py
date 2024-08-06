from dataclasses import dataclass
import os
from functools import reduce
import operator

import networkx as nx
import matplotlib.pyplot as plt
from icecream import ic

@dataclass
class Snowverload:
    _data: str

    def __post_init__(self):
        self.G = nx.Graph()
        self.create_graph()
        self.remove_edges()

    def prod(self, iterable: list[int]) -> int:
        return reduce(operator.mul, iterable, 1)

    @property
    def parse_data(self) -> dict[str, list[str]]:
        nodes_dict = dict()
        for line in self._data:
            key, value = line.split(': ')
            value = [word for word in value.split()]
            nodes_dict[key] = value
        return nodes_dict
    
    def create_graph(self) -> None:
        for key, value in self.parse_data.items():
            for node in value:
                self.G.add_edge(key, node)
    
    def remove_edges(self) -> None:
        cuts = nx.minimum_edge_cut(self.G)
        self.G.remove_edges_from(cuts)

    def multiply_graphs_edges(self) -> int:
        edges_count = list(map(len, nx.connected_components(self.G)))
        return self.prod(edges_count)

    def draw_graph(self) -> None:
        nx.draw(self.G, with_labels=True)
        plt.show()

    @property
    def solution(self) -> int:
        return self.multiply_graphs_edges()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day25_test.txt'
    PATH = 'inputs/day25.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    snowverload = Snowverload(data.split('\n'))
    ic(snowverload.solution)
    # snowverload.draw_graph() # only for test input
