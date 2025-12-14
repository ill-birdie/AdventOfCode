data = """L90
R90"""
data = data.split("\n")

curr_val = 50
result = 0
for turn in data:
    magnitude = int(turn[1:]) % 100
    orig_mag = magnitude
    match turn[0]:
        case "R": curr_val += magnitude
        case "L": curr_val -= magnitude
    curr_val %= 100
    if curr_val == 0:
        result += 1
print(result)