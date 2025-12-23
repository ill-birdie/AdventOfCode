from src.misc.starter_code import parse_file

class Solution:
    def __init__(self):
        self.result = 0

    def combinations(self, curr_target, curr_containers):
        for idx, container in enumerate(curr_containers):
            curr_diff = curr_target - container
            if curr_diff == 0:
                self.result += 1
            elif curr_diff > 0:
                self.combinations(curr_diff, curr_containers[idx + 1:])
        return None

data = sorted(parse_file().split('\n'), key=int, reverse=True)
data = [int(n) for n in data]

foo = Solution()
foo.combinations(150, data)
print(foo.result)