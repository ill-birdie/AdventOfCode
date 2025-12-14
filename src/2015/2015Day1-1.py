data = ")())())"

floor = 0
for parentheses in data:
    match parentheses:
        case "(": floor += 1
        case ")": floor -= 1
print(floor)