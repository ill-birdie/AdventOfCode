from src.misc.starter_code import parse_file
import math


def get_winner(n: int) -> int:
    """
    Finds the elf that wins in the circle game.

    Let nearest (int) be the exponentiated number of base 2 below n;
    4 would be the nearest to 5, 16 is nearest to 20
    Let offset be double the difference of n and nearest;
    0 would be the offset of 4 (2 * (4 - 4)), 6 would be the offset of 7 (2 * (7 - 4))
    :param n:
    :return:
    """
    nearest = 2 ** math.floor(math.log(num_elves, 2))
    offset = 2 * (n - nearest)
    winner = offset + 1
    return winner


num_elves = int(parse_file())
print(f"""Part one answer: {get_winner(num_elves)}""")