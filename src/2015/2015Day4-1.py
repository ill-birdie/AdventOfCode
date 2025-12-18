import hashlib

secret_key = "iwrupvqb"
encoded = ""

def encode_key(key: str) -> str:
    return hashlib.md5(key.encode()).hexdigest()

i = -1
while encoded[:5] != "00000":
    i += 1
    encoded = encode_key(secret_key + str(i))
print(i)