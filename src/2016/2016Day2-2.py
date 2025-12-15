data = """ULL
RRDDD
LURDL
UUUUD"""
data = data.split("\n")

numpad = [
    ['', '', '1', '', ''],
    ['', '2', '3', '4', ''],
    ['5', '6', '7', '8', '9'],
    ['', 'A', 'B', 'C', ''],
    ['', '', 'D', '', '']
]

curr_pos = [2, 0]
def clamp(num: int, l_bound: int, u_bound: int) -> int:
    return max(l_bound, min(num, u_bound))


def get_num(l: str, pos: list):
    for letter in l:
        orig_pos = pos.copy()
        match letter:
            case "R": pos[1] += 1
            case "L": pos[1] -= 1
            case "U": pos[0] -= 1
            case "D": pos[0] += 1
        for axis in range(2):
            pos[axis] = clamp(pos[axis], 0, 4)
        if numpad[pos[0]][pos[1]] == '':
            pos = orig_pos.copy()
    return numpad[pos[0]][pos[1]], pos

result = ""
for line in data:
    curr_result = get_num(line, curr_pos)
    result += curr_result[0]
    curr_pos = list(curr_result[1])
print(result)
