tree = """ *
      **o
     ***o*
    *o@*oo*
   *@oo**@*o"""


def get_profit(curr_tree: str) -> float:
    """
    Parses a tree (str) and returns the amount of profit:
        Each row of the tree is worth $50.
        Each instance of an ornament (o) is worth $2.
        Each instance of @ is worth $5.
    The final profit is 20% of the total worth of the tree.
    :param curr_tree: A string representing a tree.
    :return: Returns the profit obtained from the tree.
    """
    curr_tree = [row.strip() for row in curr_tree.split('\n')]
    cost = len(curr_tree) * 50
    curr_tree = "".join(curr_tree)
    for char in curr_tree:
        match char:
            case "o": cost += 2
            case "@": cost += 5
    profit = cost * 0.20
    return profit


print(get_profit(tree))