from src.misc.starter_code import parse_file

data = parse_file()
data = data.split("\n")


def part1_answer() -> int:
    curr_val = 50
    result = 0
    for turn in data:
        magnitude = int(turn[1:]) % 100
        match turn[0]:
            case "R": curr_val += magnitude
            case "L": curr_val -= magnitude
        curr_val %= 100
        if curr_val == 0:
            result += 1
    return result


def part2_answer() -> int:
    curr_val = 50
    result = 0
    for turn in data:
        magnitude = int(turn[1:])
        orig_dial_point = curr_val
        if magnitude > 100:
            orig_val = magnitude
            magnitude %= 100
            result += (orig_val - magnitude) / 100

        match turn[0]:
            case "R": curr_val += magnitude
            case "L": curr_val -= magnitude

        if curr_val < 0:
            curr_val += 100
            if orig_dial_point != 0:
                result += 1
        elif curr_val > 100:
            curr_val -= 100
            if orig_dial_point != 0:
                result += 1

        if curr_val == 100 or curr_val == 0:
            curr_val = 0
            result += 1
    return int(result)


print(f"""Part 1 answer: {part1_answer()}
Part 2 answer: {part2_answer()}""")