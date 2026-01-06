from src.misc.starter_code import parse_file
from typing import Dict, List


class Solution:
    def __init__(self):
        self._depths: Dict[int, List[bool]] = {}
        self._curr_depth = 0
        self._curr_num = ''


    @property
    def depths(self):
        return self._depths

    @property
    def curr_depth(self):
        return self._curr_depth

    @property
    def curr_num(self):
        return self._curr_num


    def new_layer(self, in_object: bool, contains_red: bool) -> None:
        self._depths[self._curr_depth] = [in_object, contains_red]

    def in_object(self, d: int) -> bool:
        return self._depths[d][0]

    def contains_red(self, d: int) -> bool:
        return self._depths[d][1]

    def set_contains_red(self, state: bool) -> None:
        self._depths[self._curr_depth][1] = state


    def sum_nums(self, s):
        total_sum = 0
        without_red_in_object = 0
        for char in s:
            if char.isdigit() or char == '-':
                self._curr_num += char
            elif len(self._curr_num) != 0:
                self._curr_num = int(self._curr_num)
                total_sum += self._curr_num
                if not (self.in_object(self._curr_depth) and self.contains_red(self._curr_depth)):
                    without_red_in_object += self._curr_num
                self._curr_num = ''

            layer_above = self._curr_depth - 1
            match char:
                case '[':
                    self._curr_depth += 1
                    self.new_layer(self.in_object(layer_above), self.contains_red(layer_above))
                case '{':
                    self._curr_depth += 1
                    self.new_layer(True, self.contains_red(layer_above))
                case ']' | '}':
                    self._depths.pop(self._curr_depth)
                    self._curr_depth -= 1
                case 'R':
                    self.set_contains_red(True)

        return [total_sum, without_red_in_object]

data = parse_file()
data = data.replace("\"red\"", 'R')

foo = Solution()
answers = foo.sum_nums(data)
part1_answer = answers[0]
part2_answer = answers[1]

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")

"""
the current code has a couple major issues.
first is initializing the top layer:
    the code relies on checking the layer above. but what if that's not a thing yet?
the second is knowing that red is in the list:
    right now, the code just goes through each number, adding it to the sum as it goes.
    only when it reaches R does it know to stop counting. but what about an object like {1, 2, R}?
    it'll sum the numbers anyway.
    
i'm thinking of a new solution that'll require a couple new methods:
    one method to search the entire object to see if R exists
    another method to sum up every item at the uppermost depth if not an object and R doesn't exist in that layer.
    my previous solution was similar to a bottom-up recursive approach.
    this approach is a breadth-first approach!
"""