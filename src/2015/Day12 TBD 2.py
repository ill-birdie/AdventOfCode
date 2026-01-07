from src.starter_code import parse_file


class Solution:
    def __init__(self):
        self._depth = 0
        self._depth_validity = {}

    @property
    def depth(self):
        return self._depth

    @property
    def depth_validity(self):
        return self._depth_validity

    @staticmethod
    def sum_all(d: str) -> int:
        result = 0
        curr_num = ''
        for char in d:
            if char.isdigit() or char == '-':
                curr_num += char
            elif len(curr_num) != 0:
                curr_num = int(curr_num)
                result += curr_num
                curr_num = ''
        return result


    def change_depth(self, char) -> None:
        """ Changes depth (object attribute) based on a one-character string (char). """
        match char:
            case '[' | '{': self._depth += 1
            case ']' | '}': self._depth -= 1


    def check_layer(self, d: str) -> None:
        """
        Searches the current depth for an instance of 'R' if in an object ({}).
        :param d: A string representing a nested object.
        :return: A boolean representing whether 'R' exists in the depth it began.
        """
        depth_result = True
        curr_depth = self._depth
        for idx, char in enumerate(d[1:-1]):
            print(char)
            self.change_depth(char)
            if char in {'[', '{'}:
                self.check_layer(d[idx])
            if curr_depth == self._depth and char == 'R':
                depth_result = False
        self._depth_validity[self._depth] = depth_result


data = parse_file()
data = data.replace("\"red\"", 'R')

foo = Solution()
answers = foo
part1_answer = 0
part2_answer = 0

foo.check_layer(data)
print(foo.depth_validity)

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")

