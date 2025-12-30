from src.misc.starter_code import parse_file

class Solution:
    def __init__(self):
        self._combinations = 0
        self._combination_lengths = []
        self._depth = 1

    @property
    def combinations(self):
        return self._combinations

    @property
    def combination_lengths(self):
        return self._combination_lengths

    @property
    def depth(self):
        return self._depth

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
                self._combinations += 1
                self._combination_lengths.append(self.depth)
            elif curr_diff > 0:
                self._depth += 1
                self.eval_combos(curr_diff, containers[idx + 1:])
        self._depth -= 1

data = sorted(parse_file().split('\n'), key=int, reverse=True)
data = [int(n) for n in data]

foo = Solution()
num_liters = 150
foo.eval_combos(num_liters, data)
min_length = min(foo.combination_lengths)
num_min = len([branch for branch in foo.combination_lengths if branch == min_length])

print(f"""Part one answer: {foo.combinations}
Part two answer: {num_min}""")