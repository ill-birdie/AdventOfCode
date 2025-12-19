def parse_data() -> str:
    with open("/src/data.txt", "r") as data:
        parsed = data.read()
        return parsed