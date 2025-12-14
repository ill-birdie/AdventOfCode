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
    left.append(int(pair[0:pair.index(" ")]))
    pair = pair[pair.index(" "):].strip(" ")
    right.append(int(pair))
left = sorted(left)
right = sorted(right)

result = 0
for num in range(len(left)):
    if left[num] > right[num]:
        result += left[num] - right[num]
    else:
        result += right[num] - left[num]
print(result)
