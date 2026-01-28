from src.starter_code import parse_file
import re


def valid_triangle(sides: list) -> bool:
    """
    Tests if a triangle is valid.
    :param sides: A list containing three sides of a triangle.
    :return: Returns a boolean representing if the sides form a valid triangle.
    """
    sides = sorted(sides, key=int, reverse=False)
    return sides[0] + sides[1] > sides[2]


def get_part1(d: str) -> int:
    parsed = d.split('\n')
    num_valid = 0
    for sides in parsed:
        sides = sides.split(' ')
        sides = [int(side) for side in sides if side != '']
        if valid_triangle(sides):
            num_valid += 1
    return num_valid


def get_part2(raw: str) -> int:
    raw = re.split('\\s+', raw)
    raw = [int(side) for side in raw if side.isdigit()]
    num_valid = 0
    rows = 3
    for row in range(rows):
        curr_triangle = []
        for side in raw[row::3]:
            curr_triangle.append(side)
            if len(curr_triangle) == 3:
                if valid_triangle(curr_triangle):
                    num_valid += 1
                curr_triangle = []
    return num_valid


data = parse_file()
print(f"""Part one answer: {get_part1(data)}
Part two answer: {get_part2(data)}""")