from dataclasses import dataclass
import os
from math import lcm
from collections import defaultdict
from typing import Optional, Iterable, overload

from icecream import ic  # type: ignore

@dataclass
class PulsePropagation:
    data: list[str]

    def __post_init__(self):
        self.main_map = self.create_main_map()

    def create_main_map(self) -> dict[str, tuple[str, list[str]]]:
        ''' key = module, values = (prefix, destinations) '''
        main_dict: dict[str, tuple[str, list[str]]] = {}
        for row in self.data:
            module, dests = row.split(' -> ')
            if module == 'broadcaster':
                prefix = ''
            else:
                prefix = module[0]
                module = module[1:]
            main_dict[module] = (prefix, dests.split(', '))
        return main_dict

    def module_map(self) -> defaultdict[str, list[str]]:
        ''' key = destination, values = modules'''
        module_dict: defaultdict[str, list[str]] = defaultdict(list)
        for module, (_, destinations) in self.main_map.items():
            for dest in destinations:
                module_dict[dest].append(module)
        return module_dict

    def memory_map(self) -> dict[str, bool | dict[str, bool]]:
        memory: dict[str, bool | dict[str, bool]] = {}
        module_map = self.module_map()
        for module, (prefix, _) in self.main_map.items():
            if prefix:
                if prefix == '%':
                    memory[module] = False
                if prefix == '&':
                    memory[module] = {value: False 
                                      for value in module_map[module]}
        return memory

    @overload
    def press_button(self, memory_map: dict[str, bool | dict[str, bool]],
                     track_modules: None = None) -> tuple[int, int]:
        ...

    @overload
    def press_button(self, memory_map: dict[str, bool | dict[str, bool]],
                     track_modules: Iterable[str]) -> list[str]:
        ...

    def press_button(self, memory_map: dict[str, bool | dict[str, bool]], 
                     track_modules: Optional[Iterable[str]] = None) -> tuple[int, int] | list[str]:
        low = 0
        high = 0
        signal_path: list[tuple[str, str, bool]] = [('', 'broadcaster', False)]
        tracked_signals: list[str] = []
        while signal_path:
            new_signal_path: list[tuple[str, str, bool]] = []
            for prefix, module, high_pulse in signal_path:
                if track_modules:
                    if module in track_modules and not high_pulse:
                        tracked_signals.append(module)
                if high_pulse:
                    high += 1
                else:
                    low += 1
                next_signal_path = self.main_map.get(module)
                if next_signal_path is None:
                    continue
                next_prefix, destinations = next_signal_path
                if next_prefix == '%':
                    if high_pulse:
                        continue
                    state = memory_map[module]
                    if isinstance(state, bool):
                        memory_map[module] = not state
                        for dest in destinations:
                            new_signal_path.append((module, dest, not state))
                elif next_prefix == '&':
                    state = memory_map[module]
                    if isinstance(state, dict):
                        state[prefix] = high_pulse
                        if sum(state.values()) == len(state):
                            send = False
                        else:
                            send = True
                        for dest in destinations:
                            new_signal_path.append((module, dest, send))
                elif next_prefix == '':
                    for dest in destinations:
                        new_signal_path.append((module, dest, high_pulse))
            signal_path = new_signal_path
        if track_modules:
            return tracked_signals
        return low, high

    def pulse_number(self, push_times: int) -> int:
        memory_map = self.memory_map()
        low_num = 0
        high_num = 0
        for _ in range(push_times):
            low, high = self.press_button(memory_map)
            low_num += low
            high_num += high
        return low_num * high_num

    def cycles_unitl_low_pulse(self, unique: str) -> int:
        module_map = self.module_map()
        memory_map = self.memory_map()
        pointer_to_unique = module_map[unique][0]
        sources = module_map[pointer_to_unique]
        cycle = 0
        low_counts: dict[str, int] = {}
        while len(low_counts) < len(sources):
            cycle += 1
            tracked_signals = self.press_button(memory_map, sources)
            for signal in tracked_signals:
                if signal in low_counts:
                    continue
                low_counts[signal] = cycle
        return lcm(*low_counts.values())

    @property
    def part_one_sol(self) -> int:
        return self.pulse_number(1000)
  
    @property
    def part_two_sol(self) -> int:
        return self.cycles_unitl_low_pulse('rx')


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day20_test.txt'
    PATH = 'inputs/day20.txt'
    with open(PATH, 'r') as f:
        data = f.read()
    pulse_propagation = PulsePropagation(data.split('\n'))
    ic(pulse_propagation.part_one_sol)
    if PATH == 'inputs/day20.txt':
        ic(pulse_propagation.part_two_sol)
