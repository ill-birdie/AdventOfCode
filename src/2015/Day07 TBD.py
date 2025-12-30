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

virtual_stack = {}
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
        if curr_result != -1 and idx not in checked_indices:
            virtual_stack[init_var] = curr_result
            checked_indices.add(idx)

print(f"""Part one answer: {virtual_stack['a']}""")
print(virtual_stack['b'])