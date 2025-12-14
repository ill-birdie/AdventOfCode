data_raw = ""
data_ranges = data_raw.split(",")
data = []
for i in data_ranges:
    bounds = i.split("-")
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])
    for num in range(lower_bound, upper_bound + 1):
        data.append(str(num))

def num_occurrences(num, target) -> int:
    count = 0
    i = 0
    while i < len(num):
        if num[i:i + len(target)] != target:
            i += 1
        else:
            count += 1
            i += len(target)
    return count

def is_invalid(num) -> bool:
    factors = []
    for i in range(1, len(num) // 2 + 1):
        if len(num) % i == 0:
            factors.append(i)
    for j in factors:
        if num_occurrences(num, num[0:j]) == len(num) / j:
            return True
    return False

result = 0
for num in data:
    if is_invalid(num):
        result += int(num)
print(result)
