import csv
from pathlib import Path

from openpyxl import Workbook


def csv_to_xlsx(csv_path, xlsx_path):
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_file = Path(csv_path)

    if csv_file.suffix != ".csv":
        raise ValueError
    if not csv_file.exists():
        raise FileNotFoundError

    with open(csv_file, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))

    if len(rows) == 0:
        raise ValueError

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for column in ws.columns:
        max_len = 0
        for cell in column:
            if len(str(cell.value)) > max_len:
                max_len = len(str(cell.value))
        ws.column_dimensions[column[0].column_letter].width = max(max_len + 2, 8)

    wb.save(xlsx_path)


if __name__ == "__main__":
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")