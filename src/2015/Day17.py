from src.misc.starter_code import parse_file

class Solution:
    combinations = 0
    depth = 1
    combination_lengths = []

    # Empty constructor
    def __init__(self):
        pass

    def eval_combos(self, target: int, containers: list) -> None:
        """
        Determines the number of ways target (int) can be broken up using numbers in containers (list).
        :param target: The number being broken up.
        :param containers: The possible numbers used to break up target (int).
        :return: None; the function updates instances variables within the class.
        """
        for idx, container in enumerate(containers):
            curr_diff = target - container
            if curr_diff == 0:
                self.combinations += 1
                self.combination_lengths.append(self.depth)
            elif curr_diff > 0:
                self.depth += 1
                self.eval_combos(curr_diff, containers[idx + 1:])
        self.depth -= 1

data = sorted(parse_file().split('\n'), key=int, reverse=True)
data = [int(n) for n in data]

foo = Solution()
num_liters = 150
foo.eval_combos(num_liters, data)
min_length = min(foo.combination_lengths)
num_min = len([branch for branch in foo.combination_lengths if branch == min_length])

print(f"""Part one answer: {foo.combinations}
Part two answer: {num_min}""")