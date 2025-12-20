import hashlib
import time

start_time = time.perf_counter()

secret_key = "iwrupvqb"
encoded = ""

def encode_key(key: str) -> str:
    return hashlib.md5(key.encode()).hexdigest()

num_zeros = 6
i = 0
while encoded[:num_zeros] != "0" * num_zeros:
    encoded = encode_key(secret_key + str(i))
    i += 1

print(f"Lowest number: {i}")
print(f"Operation took {round(time.perf_counter() - start_time, 3)} seconds.")