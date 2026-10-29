import re
import string


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def remove_page_numbers(text: str) -> str:
    lines = text.splitlines()
    filtered = [
        line
        for line in lines
        if not re.fullmatch(r"\s*(\[?\s*page\s*)?\d+\s*\]?\s*", line, flags=re.I)
    ]
    return "\n".join(filtered)


def remove_punctuation(text: str) -> str:
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)


def preprocess_text(text: str) -> str:
    text = text.lower()
    text = remove_page_numbers(text)
    text = remove_punctuation(text)
    return normalize_whitespace(text)
