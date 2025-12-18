from collections import Counter

data = "1 1 2 2 3 3 4 4 5 5"
data = [int(n) for n in data.split(' ')]


def get_rigged_color(nums: list) -> str:
    """
    PRECONDITION: len(nums) >= 10

    Determines if there are a disproportionate number of
    red (even) or black (odd) numbers in a given list
    (ratio must be greater than or equal to 70:30).
    :param nums: A list of numbers.
    :return: Returns the rigged color (str)
    Otherwise, returns an empty string if neither are rigged.
    """
    reds = [n for n in nums if n % 2 == 0]
    if len(nums) / len(reds) >= 0.70:
        return "Red"
    elif len(nums) / len(reds) <= 0.30:
        return "Black"
    else:
        return ""


def get_rigged_nums(nums: list) -> list:
    """
    PRECONDITION: len(nums) >= 10

    Determines numbers that appear a disproportionate amount
    (numbers that compose 20% or more of the total data).
    :param nums: A list of numbers.
    :return: Returns a list of the rigged numbers.
    If there are no rigged numbers, an empty list is returned.
    """
    rigged = []
    threshold = len(nums) / 5
    nums = Counter(nums)
    for n in nums.keys():
        if nums[n] >= threshold:
            rigged.append(n)
    return rigged

rigged_nums = get_rigged_nums(data)
result = 1
for n in rigged_nums:
    result *= n

print(f"""Rigged numbers: {rigged_nums}
Product of rigged numbers (result): {result}""")