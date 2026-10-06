import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.lib.text.normalize import normalize
from src.lib.text.tokenizer import tokenize
from src.lib.text.count_freq import count_freq
from src.lib.text.top_n import top_n

text = sys.stdin.read()

tokens = tokenize(normalize(text))
freq = count_freq(tokens)
top5 = top_n(freq, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

for w, c in top5:
    print(f"{w}:{c}")