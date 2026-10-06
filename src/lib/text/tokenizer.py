import re

def tokenize(text: str) -> list[str]:
    pattern = r"\w+(?:-\w+)*"
    return re.findall(pattern, text)
