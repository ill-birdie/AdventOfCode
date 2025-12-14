data = "()())"

floor = 0
for i in range(1, len(data) + 1):
    match data[i - 1]:
        case "(": floor += 1
        case ")": floor -= 1
    if floor < 0:
        print(i)
        break