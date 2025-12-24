data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
data = data.split(',')

def is_invalid(num: int) -> bool:
    num = str(num)
    if len(num) % 2 != 0:
        return False
    first_half = num[:len(num) // 2]
    second_half = num[len(num) // 2:]
    if first_half != second_half:
        return False
    else:
        return True

result = 0
for r in data:
    r = [int(bound) for bound in r.split('-')]
    for id in range(r[0], r[1] + 1):
        if is_invalid(id):
            result += id
print(result)