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
    
    def find_range(self, cat, gt, val, ranges):
        cat = 'xmas'.index(cat)
        ranges2 = []
        for rng in ranges:
            rng = list(rng)
            low, high = rng[cat]
            if gt:
                low = max(low, val + 1)
            else:
                high = min(high, val - 1)
            if low > high:
                continue
            rng[cat] = (low, high)
            ranges2.append(tuple(rng))
        return ranges2

    def acceptance_ranges_outer(self, rule: str):
        return self.acceptance_ranges_inner(self.new_workflow[rule].split(","))
    
    def acceptance_ranges_inner(self, rules: list[str]):
        rule = rules[0]
        if rule == 'R':
            return []
        elif rule == 'A':
            return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
        elif ':' not in rule:
            return self.acceptance_ranges_outer(rule)
        cond = rule.split(':')[0]
        cat = cond[0]
        val = int(cond[2:])
        if gt := '>' in cond:
            val_inv = val + 1
        else:
            val_inv = val - 1
        cond_is_true = self.find_range(cat, gt, val,
                                          self.acceptance_ranges_inner([rule.split(":")[1]]))
        cond_is_false = self.find_range(cat, not gt, val_inv,
                                           self.acceptance_ranges_inner(rules[1:]))
        return cond_is_true + cond_is_false
    
    def sum_ranges(self) -> int:
        result = 0
        for rng in self.acceptance_ranges_outer(self.start):
            dt = 1
            for low, high in rng:
                dt *= high - low + 1
            result += dt
        return result

    @property
    def part_one_sol(self) -> int:
        return self.sum_accepterd_parts(self.accept_or_reject())
    
    @property
    def part_two_sol(self) -> int:
        return self.sum_ranges()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day19_test.txt'
    PATH = 'inputs/day19.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    aplenty = Aplenty(data)
    ic(aplenty.part_one_sol)
    ic(aplenty.part_two_sol)
