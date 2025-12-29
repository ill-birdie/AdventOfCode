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


def operand_int(op) -> int:
    new_operator: int
    if op in virtual_stack:
        new_operator = virtual_stack[op]
    elif op.isdigit():
        new_operator = op
    else:
        new_operator = -1
    return int(new_operator)


data = parse_file()
data = data.split('\n')

"""
i need to account for keyerrors caused by variables not already being initialized (false assumption)
im probably going to use a while-loop to check if the data list is empty, removing elements that
successfully perform the operation. that way we can keep cycling through the instructions
until we can finally use them after everything is initialized.

keyerrors are addressed. now i need to figure out how to remove the lines we've just looked at and used 
also a new bug emerged with the indices and popping the data. i think it skips an element if i pop the previous one.
"""
idx = 0
virtual_stack = {}
for line in data:
    line = line.split(' -> ')
    left_side = line[0]
    init_var = line[1]
    parsed_left = left_side.split(' ')
    print(init_var, idx)

    curr_result = -1
    match len(parsed_left):
        # Initialize a new variable
        case 1:
            curr_result = operand_int(left_side)

        # Bitwise NOT operator
        case 2:
            operand = parsed_left[1]
            if operand in virtual_stack:
                var = virtual_stack[operand]
                curr_result = wrap(~var)

        # Other bitwise operators
        case 3:
            operator = parsed_left[1]
            operand1 = operand_int(parsed_left[0])
            operand2 = operand_int(parsed_left[-1])
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
        virtual_stack[init_var] = curr_result
        data.pop(idx)
    else:
        idx += 1
print(virtual_stack)
print(data)