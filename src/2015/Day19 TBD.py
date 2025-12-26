from src.misc.starter_code import parse_file
from collections import defaultdict

data = parse_file()
data = data.split('\n')

newline_idx = data.index('')
molecule = data[newline_idx + 1]
data = data[:newline_idx]

conversions = defaultdict(list)
decompositions = defaultdict(list)
for line in data:
    line = line.split(' ')
    conversions[line[0]].append(line[-1])
    decompositions[line[-1]].append(line[0])

seen_molecules = set()
for k in conversions:
    for v in conversions[k]:
        for idx, l in enumerate(molecule):
            if k == molecule[idx:idx + len(k)]:
                seen_molecules.add(molecule[:idx] + molecule[idx:].replace(k, v, 1))
print(f"Part one answer: {len(seen_molecules)}")