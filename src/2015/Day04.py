import hashlib
import time
from src.starter_code import parse_file
start_time = time.perf_counter()


def encode_key(key: str) -> str:
    return hashlib.md5(key.encode()).hexdigest()


def trailing_char_num(target: str, times: int) -> int:
    i = -1
    encoded = ""
    while encoded[:times] != target * times:
        i += 1
        encoded = encode_key(secret_key + str(i))
    return i


secret_key = parse_file()
print(f"""Part one answer: {trailing_char_num("0", 5)}
Part two answer: {trailing_char_num("0", 6)}""")


print(f"Operation took {round(time.perf_counter() - start_time, 3)} seconds.")