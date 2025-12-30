from src.misc.starter_code import parse_file
import re

def wrap(n: int) -> int:
    """
    Forces a number outside the 16-bit range to overflow (wrap around).
    :param n: The input number (int).
    :return: The new number (int).
    """
    wrap_const = 65535 + 1
    if n < 0:
        n += wrap_const
    elif n > wrap_const:
        n -= wrap_const
    return n


class Solution:
    def __init__(self, instr: list):
        self._instructions = instr
        self._virtual_stack = {}

    def __getitem__(self, key):
        return self._virtual_stack[key]


    @property
    def virtual_stack(self):
        return self._virtual_stack


    def operand_int(self, operand) -> int:
        new_operator: int
        if operand in self._virtual_stack:
            new_operator = self._virtual_stack[operand]
        elif operand.isdigit():
            new_operator = operand
        else:
            new_operator = -1
        return int(new_operator)


    def execute(self) -> None:
        checked_indices = set()
        while len(checked_indices) < len(data):
            checked_indices = set()
            for idx, line in enumerate(data):
                line = line.split(' -> ')
                left_side = line[0]
                init_var = line[1]
                parsed_left = left_side.split(' ')

                curr_result = -1
                match len(parsed_left):
                    # Initialize a new variable
                    case 1:
                        curr_result = self.operand_int(left_side)

                    # Bitwise NOT operator
                    case 2:
                        operand = parsed_left[1]
                        if operand in self._virtual_stack:
                            var = self._virtual_stack[operand]
                            curr_result = wrap(~var)

                    # Other bitwise operators
                    case 3:
                        operator = parsed_left[1]
                        operand1 = self.operand_int(parsed_left[0])
                        operand2 = self.operand_int(parsed_left[-1])
                        if operand1 != -1 and operand2 != -1:
                            match operator:
                                case 'AND':
                                    curr_result = operand1 & operand2
                                case 'OR':
                                    curr_result = operand1 | operand2
                                case 'LSHIFT':
                                    curr_result = operand1 << operand2
                                case 'RSHIFT':
                                    curr_result = operand1 >> operand2
                if curr_result != -1:
                    self._virtual_stack[init_var] = curr_result
                    checked_indices.add(idx)

data = parse_file()
data = data.split('\n')

part1 = Solution(data)
part1.execute()
part1_answer = part1['a']

part2_data = data.copy()
part2_data = [line for line in part2_data if not bool(re.search('-> b$', line))]
part2 = Solution(part2_data)
part2.virtual_stack['b'] = part1_answer

"""
for some reason this step evaluates b to the same thing as part a,
even though i removed the line that initializes b. im not sure why, 
but i'll definitely work on it tomorrow.
"""
part2.execute()
print(part2['b'])
part2_answer = part2['a']

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")