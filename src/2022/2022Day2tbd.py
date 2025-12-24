from src.misc.starter_code import parse_file

def rps_result(opp: str, choice: str) -> int:
    curr_result = ""
    match choice:
        case "X": curr_result = "Draw"
        case "Y": curr_result = "Win"
        case "Z": curr_result = "Loss"
    return 0


def round_result(opp: str, choice: str) -> int:
    curr_result = 0
    match choice:
        case "X": curr_result += 1
        case "Y": curr_result += 2
        case "Z": curr_result += 3
    return curr_result

data = parse_file()
data = data.split('\n')

num_combos = 0
for line in data:
    line = line.split(' ')
    num_combos += round_result(line[0], line[1])
print(num_combos)