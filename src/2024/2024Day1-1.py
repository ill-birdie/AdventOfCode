data = """3   4
4   3
2   5
1   3
3   9
3   3"""
data = data.split("\n")
left = []
right = []
for pair in data:
    pair = [int(num) for num in list(pair) if num != " "]
    left.append(pair[0])
    right.append(pair[1])
left = sorted(left)
right = sorted(right)

num_combos = 0
for num in range(len(left)):
    if left[num] > right[num]:
        num_combos += left[num] - right[num]
    else:
        num_combos += right[num] - left[num]
print(num_combos)
