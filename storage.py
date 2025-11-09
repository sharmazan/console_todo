def load_tasks(filename: str, tasks: list):
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                tasks.append(line[:-1])
    except FileNotFoundError:
        pass


def save_tasks(filename: str, tasks: list):
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task}\n")
