data = """ULL
RRDDD
LURDL
UUUUD"""
data = data.split("\n")

numpad = {}
curr_pos = [0, 0]
num = 1
for y in range(1, -2, -1):
    for x in range(-1, 2):
        numpad[f"[{x}, {y}]"] = num
        num += 1

def clamp(num: int, l_bound: int, u_bound: int) -> int:
    return max(l_bound, min(num, u_bound))

def get_num(line: str) -> int:
    for letter in line:
        match letter:
            case "R": curr_pos[0] += 1
            case "L": curr_pos[0] -= 1
            case "U": curr_pos[1] += 1
            case "D": curr_pos[1] -= 1
        for axis in range(len(curr_pos)):
            curr_pos[axis] = clamp(curr_pos[axis], -1, 1)
    return numpad[str(curr_pos)]

result = ""
for line in data:
    result += str(get_num(line))
print(result)