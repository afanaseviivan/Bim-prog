import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    "Десериализация файла cvs"
    with open(INPUT_FILENAME, "r") as file1:
        result = [row for row in csv.DictReader(file1)]

    "Сериализация данных в json"
    with open(OUTPUT_FILENAME, "w") as file2:
        json.dump(result, file2, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
