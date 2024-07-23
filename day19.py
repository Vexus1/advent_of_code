from dataclasses import dataclass
import os
import re

from icecream import ic

@dataclass
class Aplenty:
    _data: str

    def __post_init__(self):
        self.workflows, self.parts = self._divide_data
        self.names, self.rules, self.destinations = self.parse_workflows
        self.new_workflow = {l.split("{")[0]: l.split("{")[1][:-1] for l in self.workflows}
        self.start = 'in'

    @property
    def _divide_data(self) -> tuple[list[str], list[str]]:
        workflows, parts = self._data.split('\n\n')
        return workflows.split('\n'), parts.split('\n')
    
    def start_index(self, names: list[str]) -> int:
        for i, name in enumerate(names):
            if name == self.start:
                return i

    def parse_part(self, part: str) -> list[str]:
        part_dict = {k: int(v) for k, v in re.findall(r"(.)=(\d+)", part)}
        return part_dict
    
    @property
    def parse_workflows(self) -> tuple[list[str], list[list[str]], list[str]]:
        names = []
        rules = []
        destinations = []
        for workflow in self.workflows:
            workflow = re.search(r'(.*){(.*),(.*)}', workflow).groups()
            workflow = list(workflow)
            workflow[1] = workflow[1].split(',')
            names.append(workflow[0])
            rules.append(workflow[1])
            destinations.append(workflow[2])
        return names, rules, destinations
    
    def parse_rule(self, rule: str) -> tuple[str]:
        rule = re.findall(r'(\w)([<>]{1})(\d+):(\w+)', rule)[0]
        return rule
     
    def accept_or_reject(self) -> list[str]:
        start = self.start_index(self.names)
        accepted_parts = []
        for part in self.parts:
            name = self.names[start]
            part = self.parse_part(part)
            while True:
                curr_index = self.names.index(name)
                curr_rules = self.rules[curr_index]
                for rule in curr_rules:
                    cat, oper, n, dest = self.parse_rule(rule)
                    if oper == '<':
                        if part[cat] < int(n):
                            name = dest
                            break
                        else:
                            continue
                    elif oper == '>':
                        if part[cat] > int(n):
                            name = dest
                            break
                        else:
                            continue
                else:
                    name = self.destinations[curr_index]
                if name == 'A':
                    accepted_parts.append(part)
                    break
                elif name == 'R':
                    break
        return accepted_parts
    
    def sum_accepterd_parts(self, acc_parts: list[dict[str, int]]) -> int:
        acc_sum = 0
        for part in acc_parts:
            acc_sum += sum(n for n in list(part.values()))
        return acc_sum

    @property
    def part_one_sol(self) -> int:
        return self.sum_accepterd_parts(self.accept_or_reject())
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day19_test.txt'
    PATH = 'inputs/day19.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    aplenty = Aplenty(data)
    ic(aplenty.part_one_sol)
