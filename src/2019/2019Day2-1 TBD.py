data = '1,1,1,4,99,5,6,0,99'
data = [int(n) for n in data.split(',')]
data[1] = 12
data[2] = 2
print(data)

def apply_opcode(operation: str, curr_i: int) -> None:
    print("hi")

for i in range(len(data)):
    match data[i]:
        case 99:
            break
        case 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        case 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        case _:
            continue
print(data[0])