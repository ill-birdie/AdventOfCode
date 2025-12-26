from src.misc.starter_code import parse_file


def clamp(n: int, l_bound: int, u_bound: int) -> int:
    return max(l_bound, min(n, u_bound))


def next_num1(l: str, pad) -> int:
    pos = [0, 0]
    for letter in l:
        match letter:
            case "R": pos[0] += 1
            case "L": pos[0] -= 1
            case "U": pos[1] += 1
            case "D": pos[1] -= 1
        for axis in range(len(pos)):
            pos[axis] = clamp(pos[axis], -1, 1)
    return pad[str(pos)]


def next_num2(l: str, pos: list, pad):
    for letter in l:
        orig_pos = pos.copy()
        match letter:
            case "R": pos[1] += 1
            case "L": pos[1] -= 1
            case "U": pos[0] -= 1
            case "D": pos[0] += 1
        for axis in range(2):
            pos[axis] = clamp(pos[axis], 0, 4)
        if pad[pos[0]][pos[1]] == '':
            pos = orig_pos
    return pad[pos[0]][pos[1]], pos


part1_numpad = {}
num = 1
for y in range(1, -2, -1):
    for x in range(-1, 2):
        part1_numpad[f"[{x}, {y}]"] = num
        num += 1

part2_numpad = [
    ['', '', '1', '', ''],
    ['', '2', '3', '4', ''],
    ['5', '6', '7', '8', '9'],
    ['', 'A', 'B', 'C', ''],
    ['', '', 'D', '', '']
]

data = parse_file()
data = data.split("\n")

part1_answer = ""
for line in data:
    part1_answer += str(next_num1(line, part1_numpad))

curr_pos = [2, 0]
part2_answer = ""
for line in data:
    curr_result = next_num2(line, curr_pos, part2_numpad)
    part2_answer += curr_result[0]
    curr_pos = list(curr_result[1])

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")
