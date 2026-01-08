from src.starter_code import parse_file

month_days = {}
for month in range(1, 13):
    days = 31
    if month == 2:
        days = 28
    elif month in {4, 6, 9, 11}:
        days = 30
    month_days[month] = days


def month_valid(m: int) -> bool:
    return m in range(1, 13)

def day_valid(m: int, d: int) -> bool:
    if month_valid(m):
        return d in range(1, month_days.get(m) + 1)
    else:
        return False

def year_valid(y: int) -> bool:
    return y in range(2000, 2100 + 1)


data = parse_file().split('\n')

result = 0
for line in data:
    line = line.strip('/').split('/')
    line = [int(n) for n in line]
    for month, day, year in zip(line, line[1:], line[2:]):
        if day_valid(month, day) and year_valid(year):
            result += (month + day + year)
print(result)