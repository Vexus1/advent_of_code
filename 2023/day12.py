from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class HotSprings:
    data: list[str]

    def __post_init__(self):
        self.part_two_activate = False

    def nondet_finite_automata(self, condition: str,
                               criteria: list[int]) -> int:
        automaton_states = '.'
        for number in criteria:
            for _ in range(number):
                automaton_states += '#'
            automaton_states += '.'
        states_dict = {0: 1}
        new_states: dict[int, int] = dict()
        for char in condition:
            for state in states_dict:
                if char == '?':
                    if state + 1 < len(automaton_states):
                        new_states[state + 1] = new_states.get(state + 1, 0) + \
                                                states_dict[state]
                    if automaton_states[state] == '.':
                        new_states[state] = new_states.get(state, 0) + \
                                            states_dict[state]
                elif char == '.':
                    if (state + 1 < len(automaton_states) and 
                        automaton_states[state + 1] == '.'):
                        new_states[state + 1] = new_states.get(state + 1, 0) + \
                                                states_dict[state]
                    if automaton_states[state] == '.':
                        new_states[state] = new_states.get(state, 0) + \
                                            states_dict[state]
                elif char == '#':
                    if (state + 1 < len(automaton_states) and
                        automaton_states[state + 1] == '#'):
                        new_states[state + 1] = new_states.get(state + 1, 0) + \
                                                states_dict[state]
            states_dict = new_states
            new_states = {}
        result = states_dict.get(len(automaton_states) - 1, 0) + \
                 states_dict.get(len(automaton_states) - 2, 0)
        return result
    
    def sum_arrangements(self, data: list[str]) -> int:
        sum_arr = 0
        if self.part_two_activate:
            for record in data:
                condition, criteria = record.split(' ')
                criteria_list = list(map(int, criteria.split(',')))
                condition, criteria_list = self.unfold_records(condition, criteria_list)
                sum_arr += self.nondet_finite_automata(condition, criteria_list)
            return sum_arr
        else:   
            for record in data:
                condition, criteria = record.split(' ')
                criteria_list = list(map(int, criteria.split(',')))
                sum_arr += self.nondet_finite_automata(condition, criteria_list)
            return sum_arr
    
    def unfold_records(self, condition: str, 
                         criteria: list[int]) -> tuple[str, list[int]]:
        condition = (condition + '?') * 5
        condition = condition[:-1]
        criteria *= 5
        return condition, criteria

    @property
    def part_one_sol(self) -> int:
        return self.sum_arrangements(self.data)

    @property
    def part_two_sol(self) -> int:
        self.part_two_activate = True
        return self.sum_arrangements(self.data)
        

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day12_test.txt'
    PATH = 'inputs/day12.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    hot_springs = HotSprings(data.split('\n'))
    ic(hot_springs.part_one_sol)
    ic(hot_springs.part_two_sol)
