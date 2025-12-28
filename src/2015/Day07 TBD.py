from src.misc.starter_code import parse_file


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


data = parse_file()
data = data.split('\n')

"""
i need to account for keyerrors caused by variables not already being initialized (false assumption)
im probably going to use a while-loop to check if the data list is empty, removing elements that
successfully perform the operation. that way we can keep cycling through the instructions
until we can finally use them after everything is initialized.
"""
virtual_stack = {}
for line in data:
    line = line.split(' -> ')
    left_side = line[0]
    init_var = line[1]
    parsed_left = left_side.split(' ')

    curr_result: int
    match len(parsed_left):
        case 1:
            curr_result = int(left_side)
        case 2:
            var = virtual_stack[parsed_left[1]]
            curr_result = wrap(~var)
        case 3:
            operator = parsed_left[1]
            operand1 = parsed_left[0]
            operand2 = parsed_left[-1]
            if not operand1.isdigit():
                operand1 = virtual_stack[operand1]
            if not operand2.isdigit():
                operand2 = virtual_stack[operand2]
            operand1 = int(operand1)
            operand2 = int(operand2)
            match operator:
                case 'AND':
                    curr_result = operand1 & operand2
                case 'OR':
                    curr_result = operand1 | operand2
                case 'LSHIFT':
                    curr_result = operand1 << operand2
                case 'RSHIFT':
                    curr_result = operand1 >> operand2
    virtual_stack[init_var] = curr_result
print(virtual_stack['a'])