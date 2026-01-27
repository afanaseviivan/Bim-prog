import json

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME, "r") as file:
        python_obj = json.load(file)

    result = sum([data["score"] * data["weight"] for data in python_obj])
    return round(result, 3)


print(task())
