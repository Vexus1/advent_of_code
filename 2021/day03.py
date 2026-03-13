from dataclasses import dataclass
import os

from icecream import ic  # type: ignore

@dataclass
class BinaryDiagnostic:
    data: list[str]

    def transpose(self, matrix: list[str]) -> list[str]:
        return list(map(''.join, zip(*matrix)))

    def power_consumption(self) -> int:
        transposed_report = self.transpose(self.data)
        gamma_rate = ''
        epsilon_rate = ''
        for row in transposed_report:
            ones = row.count('1')
            zeros = len(row) - ones
            if zeros > ones:
                gamma_rate += '0'
                epsilon_rate += '1'
            else:
                gamma_rate += '1'
                epsilon_rate += '0'
        power = int(gamma_rate, 2) * int(epsilon_rate, 2)
        return power
    
    def rating(self, most_common: bool) -> int:
        report = self.data[:]
        bit = 0
        while len(report) != 1:
            ones = sum(num[bit] == '1' for num in report)
            zeros = len(report) - ones
            if most_common:
                target = '1' if ones >= zeros else '0'
            else:
                target = '0' if ones >= zeros else '1'
            report = [num for num in report if num[bit] == target]
            bit += 1
        return int(report[0], 2)

    def support_rating(self) -> int:
        return self.rating(True) * self.rating(False)
            
    @property
    def part_one_sol(self) -> int:
        return self.power_consumption()
    
    @property
    def part_two_sol(self) -> int:
        return self.support_rating()
    

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # PATH = 'inputs/day03_test.txt' 
    PATH = 'inputs/day03.txt'  
    with open(PATH, 'r') as f:
        data = f.read()
    binary_diagnostic = BinaryDiagnostic(data.split('\n'))
    ic(binary_diagnostic.part_one_sol)
    ic(binary_diagnostic.part_two_sol)
