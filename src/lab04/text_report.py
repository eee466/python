import argparse
from collections import Counter

from ..lib.text.normalize import normalize
from ..lib.text.tokenizer import tokenize
from ..lib.text.top_n import top_n
from .io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def main() -> None:
    parser = argparse.ArgumentParser(description="Отчёт по частотам слов")
    parser.add_argument("--in", dest="input", default="data/lab04/input.txt")
    parser.add_argument("--out", dest="output", default="data/lab04/report.csv")
    parser.add_argument("--encoding", default="utf-8")
    args = parser.parse_args()

    text = read_text(args.input, encoding=args.encoding)

    freq = frequencies_from_text(text)
    rows = sorted_word_counts(freq)
    write_csv(rows, args.output, header=("word", "count"))

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(dict(freq), 5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
