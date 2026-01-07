from src.starter_code import parse_file
import re
import operator

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


def apply_operator(oper: str, num1: int, num2=None) -> int:
    if num2 is not None:
        operations = {
            'AND': operator.and_(num1, num2),
            'OR': operator.or_(num1, num2),
            'LSHIFT': operator.lshift(num1, num2),
            'RSHIFT': operator.rshift(num1, num2)
        }
        return operations[oper]
    else:
        return ~num1


class Solution:
    def __init__(self, instr: list):
        self._instructions = instr
        self._virtual_stack = {}

    def __getitem__(self, key):
        return self._virtual_stack[key]

    @property
    def instructions(self):
        return self._instructions

    @instructions.setter
    def instructions(self, new_inst):
        self._instructions = new_inst

    @property
    def virtual_stack(self):
        return self._virtual_stack

    def clear_stack(self):
        self._virtual_stack = {}

    def operand_int(self, operand) -> int:
        new_operand: int
        if operand in self._virtual_stack:
            new_operand = self._virtual_stack[operand]
        elif operand.isdigit():
            new_operand = operand
        else:
            return -1
        return int(new_operand)


    def execute(self) -> None:
        checked_indices = set()
        while len(checked_indices) < len(self._instructions):
            checked_indices = set()
            for idx, line in enumerate(self._instructions):
                line = line.split(' -> ')
                left_side = line[0]
                init_var = line[1]
                parsed_left = left_side.split(' ')

                result = -1
                match len(parsed_left):
                    # Initialize a new variable
                    case 1:
                        result = self.operand_int(left_side)

                    # Bitwise NOT operator
                    case 2:
                        operand = self.operand_int(parsed_left[-1])
                        if operand != -1:
                            result = apply_operator('NOT', operand)
                            result = wrap(result)

                    # Other bitwise operators
                    case 3:
                        operation = parsed_left[1]
                        operand1 = self.operand_int(parsed_left[0])
                        operand2 = self.operand_int(parsed_left[-1])
                        if operand1 != -1 and operand2 != -1:
                            result = apply_operator(operation, operand1, operand2)

                if result != -1:
                    self._virtual_stack[init_var] = result
                    checked_indices.add(idx)

data = parse_file()
data = data.split('\n')

foo = Solution(data)
foo.execute()
part1_answer = foo['a']

initializing_b = lambda s : bool(re.search('-> b$', s))
part2_data = [line for line in data if not initializing_b(line)]

foo.clear_stack()
foo.virtual_stack['b'] = part1_answer
foo.instructions = part2_data
foo.execute()
part2_answer = foo['a']

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")