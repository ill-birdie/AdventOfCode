# Add a newline character to the last line
data = """
"""
data = data.split("\n")
elves = []
curr_elf = 0
for cal in data:
    if cal == "":
        elves.append(curr_elf)
        curr_elf = 0
    else:
        curr_elf += int(cal)
top_three_elves = []
for i in range(3):
    largest_elf = max(elves)
    top_three_elves.append(largest_elf)
    elves.remove(largest_elf)
result = 0
for elf in top_three_elves:
    result += elf
print(result)
