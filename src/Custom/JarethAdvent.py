tree = """ *
      **o
     ***o*
    *o@*oo*
   *@oo**@*o"""

tree = [row.strip() for row in tree.split('\n')]
cost = len(tree) * 50
tree = "".join(tree)
for char in tree:
    match char:
        case "o": cost += 2
        case "@": cost += 5
profit = cost * 0.20
print(profit)