from src.misc.starter_code import parse_file

class Solution:
    def __init__(self):
        self.result = 0

    def get_combinations(self, curr_target, curr_containers):
        """
        A recursive function that finds and returns the total number of possible ways to
        add up curr_containers' (list) elements to reach curr_target (int) by
        incrementing result (int, instance variable).

        :param curr_target:
        :param curr_containers:
        :return:
        """
        for idx, container in enumerate(curr_containers):
            curr_diff = curr_target - container
            if curr_diff == 0:
                self.result += 1
            elif curr_diff > 0:
                self.get_combinations(curr_diff, curr_containers[idx + 1:])
        return self.result

data = sorted(parse_file().split('\n'), key=int, reverse=True)
data = [int(n) for n in data]

foo = Solution()
print(foo.get_combinations(150, data))