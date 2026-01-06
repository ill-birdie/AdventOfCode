from src.misc.starter_code import parse_file


class Solution:
    def __init__(self):
        self._depth = 0

    @property
    def depth(self):
        return self.depth

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


    def contains_red(self, d: str) -> bool:
        """
        Searches the current depth for an instance of 'R'.
        :param d: A string representing a nested object.
        :return: A boolean representing whether 'R' exists in the depth it began.
        """
        curr_depth = self._depth
        for char in d[1:-1]:
            self.change_depth(char)
            if curr_depth == self._depth and char == 'R':
                return True
        return False


data = parse_file()
data = data.replace("\"red\"", 'R')

foo = Solution()
answers = foo
part1_answer = 0
part2_answer = 0

print(foo.contains_red(data))

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")

