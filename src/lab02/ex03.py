StudentRecord = tuple[str, str, float]

def format_record(rec: StudentRecord) -> str:
    if not isinstance(rec, tuple):
        raise TypeError()
    if len(rec) != 3:
        raise ValueError()

    f, g, gp = rec

    if not isinstance(f, str) or not isinstance(g, str) or not isinstance(gp, (int, float)):
        raise TypeError()

    fp = [p for p in f.split() if p]
    if len(fp) < 2:
        raise ValueError()

    g = g.strip()
    if not g:
        raise ValueError()

    if not (0.0 <= gp <= 5.0):
        raise ValueError()

    s = fp[0].capitalize()
    i = "".join([f"{p[0].upper()}." for p in fp[1:3]])

    return f"{s} {i}, гр. {g}, GPA {gp:.2f}"



print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
# Вывод: Иванов И.И., гр. BIVT-25, GPA 4.60

print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
# Вывод: Петров П., гр. IKBO-12, GPA 5.00

print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
# Вывод: Петров П.П., гр. IKBO-12, GPA 5.00

print(format_record(("  сидорова  анна   сергеевна  ", "ABB-01", 3.999)))
# Вывод: Сидорова А.С., гр. ABB-01, GPA 4.00
