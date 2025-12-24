from src.misc.starter_code import parse_file

data = parse_file()

floor = 0
basement_idx = -1
for idx, parentheses in enumerate(data, start=1):
    match parentheses:
        case "(": floor += 1
        case ")": floor -= 1
    if floor < 0 and basement_idx == -1:
        basement_idx = idx
print(f"""Part one answer: {floor}
Part two answer: {basement_idx}""")