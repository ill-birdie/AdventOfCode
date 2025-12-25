from src.misc.starter_code import parse_file


def get_attempts(l: str) -> int:
    """
    Parses and returns the amount of attempts in a given string.
    :param l: A string containing an amount of attempts (followed by x).
    :return: The amount of attempts in a given string.
    """
    return int(l[l.index('x') + 1:])


data = parse_file()
data = data.split('\n')
data = [line for line in data if 'x' in line]
attempts = 0
for line in data:
    attempts += get_attempts(line)
print(attempts)