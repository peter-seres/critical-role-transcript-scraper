def write_list_to_file(lst: list, filename: str) -> None:
    with open(filename, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")


def read_video_ids(filename: str) -> list:
    with open(filename) as f:
        return f.read().splitlines()


def write_to_json(d: dict, filename: str) -> None:
    import json
    j = json.dumps(d)
    with open(filename, 'w') as f:
        f.write(j)
    print(f" Wrote dictionary to file: {filename}")


def load_json(filename: str) -> dict:
    import json
    with open(filename) as f:
        return json.load(f)
