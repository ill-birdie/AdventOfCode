from src.misc.starter_code import parse_file

data = parse_file()

floor = 0
for parentheses in data:
    match parentheses:
        case "(": floor += 1
        case ")": floor -= 1
print(floor)