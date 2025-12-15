data = '1,1,1,4,99,5,6,0,99'
data = [int(n) for n in data.split(',')]
print(data)

def apply_opcode(operation: str, curr_i: int) -> int:
    match operation:
        case "*": data[data[curr_i + 3]] = data[data[curr_i + 1]] * data[data[curr_i + 2]]
        case "+": data[data[curr_i + 3]] = data[data[curr_i + 1]] + data[data[curr_i + 2]]
    return curr_i + 3

for i in range(len(data) - 3):
    match data[i]:
        case 99:
            break
        case 1:
            i = apply_opcode("+", i)
        case 2:
            i = apply_opcode("*", i)
        case _:
            continue

print(data[0])