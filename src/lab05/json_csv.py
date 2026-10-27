import csv
import json
from pathlib import Path


def _check_file(path: Path, suffix: str) -> None:
    """Проверка существования и расширения файла."""
    if path.suffix.lower() != suffix:
        raise ValueError
    if not path.exists():
        raise FileNotFoundError
    if not path.is_file():
        raise ValueError


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте, новые ключи добавляются в конец.
    """
    src = Path(json_path)
    dst = Path(csv_path)
    _check_file(src, ".json")
    if dst.suffix.lower() != ".csv":
        raise ValueError

    with open(src, encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list) or len(data) == 0:
        raise ValueError
    for item in data:
        if not isinstance(item, dict):
            raise ValueError

    columns = []
    for item in data:
        for key in item:
            if key not in columns:
                columns.append(key)

    with open(dst, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей). 
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    src = Path(csv_path)
    dst = Path(json_path)
    _check_file(src, ".csv")
    if dst.suffix.lower() != ".json":
        raise ValueError

    with open(src, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    if len(rows) == 0:
        raise ValueError

    with open(dst, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")