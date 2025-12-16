from collections import Counter

data = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab"""
data = data.split('\n')

def find_times(curr_line: str, curr_times: int) -> bool:
    curr_line = Counter(curr_line)
    for letter in curr_line.keys():
        if curr_line[letter] == curr_times:
            return True
    return False


num_doubles = 0
num_triples = 0
for line in data:
    num_found = 0
    if find_times(line, 2):
        num_doubles += 1
    if find_times(line, 3):
        num_triples += 1
print(int(num_doubles) * int(num_triples))