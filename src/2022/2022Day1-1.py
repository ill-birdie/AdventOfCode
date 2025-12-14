data = """"""
data = data.split("\n")
elves = []
curr_elf = 0
for cal in data:
    if cal == "":
        elves.append(curr_elf)
        curr_elf = 0
    else:
        curr_elf += int(cal)
print(max(elves))
