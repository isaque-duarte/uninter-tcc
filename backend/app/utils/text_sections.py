import re


def split_into_sections(text: str, max_chars: int = 900) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n+", text) if part.strip()]
    sections = paragraphs if len(paragraphs) > 1 else split_into_sentences(text)

    cleaned: list[str] = []
    for section in sections:
        normalized = re.sub(r"\s+", " ", section).strip()
        if not normalized:
            continue
        cleaned.extend(_chunk_section(normalized, max_chars=max_chars))

    return cleaned


def split_into_sentences(text: str) -> list[str]:
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def _chunk_section(section: str, max_chars: int) -> list[str]:
    if len(section) <= max_chars:
        return [section]

    sentences = split_into_sentences(section)
    chunks: list[str] = []
    current = ""

    for sentence in sentences:
        next_chunk = f"{current} {sentence}".strip()
        if len(next_chunk) > max_chars and current:
            chunks.append(current)
            current = sentence
        else:
            current = next_chunk

    if current:
        chunks.append(current)

    return chunks

