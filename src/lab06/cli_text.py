import argparse
from pathlib import Path

from src.lib.text.normalize import normalize
from src.lib.text.tokenizer import tokenize
from src.lib.text.count_freq import count_freq
from src.lib.text.top_n import top_n


def cat(input_path, number):
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError

    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if number:
                print(f"{i}: {line}")
            else:
                print(line)


def stats(input_path, top):
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError

    with open(path, encoding="utf-8") as f:
        text = f.read()

    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")
    for word, count in top_n(freq, top):
        print(f"{word}: {count}")


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов показать (по умолчанию 5)")

    args = parser.parse_args()

    if args.command == "cat":
        cat(args.input, args.n)
    elif args.command == "stats":
        if args.top <= 0:
            parser.error("--top должен быть больше 0")
        stats(args.input, args.top)


if __name__ == "__main__":
    main()
