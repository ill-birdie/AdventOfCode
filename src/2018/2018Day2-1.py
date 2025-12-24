from collections import Counter

data = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""
data = data.split('\n')

def found(curr_line: str, curr_times: int) -> bool:
    curr_line = Counter(curr_line)
    for letter in curr_line.keys():
        if curr_line[letter] == curr_times:
            return True
    return False

result = []
for times in range(2, 4):
    curr_count = 0
    for line in data:
        if found(line, times):
            curr_count += 1
    result.append(curr_count)
print(result[0] * result[1])