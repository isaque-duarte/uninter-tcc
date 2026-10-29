from functools import lru_cache

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.core.config import get_settings
from app.services.lexical_similarity import calculate_lexical_similarity
from app.utils.text_sections import split_into_sections


@lru_cache(maxsize=1)
def _load_model():
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(get_settings().semantic_model_name)


def _embeddings_for(sections: list[str]) -> np.ndarray:
    try:
        model = _load_model()
        return np.asarray(model.encode(sections, convert_to_numpy=True, show_progress_bar=False))
    except Exception:
        vectorizer = TfidfVectorizer().fit(sections)
        return vectorizer.transform(sections).toarray()


def _paired_embeddings(sections_a: list[str], sections_b: list[str]) -> tuple[np.ndarray, np.ndarray]:
    try:
        model = _load_model()
        embeddings = np.asarray(
            model.encode(sections_a + sections_b, convert_to_numpy=True, show_progress_bar=False)
        )
        return embeddings[: len(sections_a)], embeddings[len(sections_a) :]
    except Exception:
        vectorizer = TfidfVectorizer().fit(sections_a + sections_b)
        return vectorizer.transform(sections_a).toarray(), vectorizer.transform(sections_b).toarray()


def calculate_semantic_similarity(text_a: str, text_b: str) -> float:
    sections_a = split_into_sections(text_a)
    sections_b = split_into_sections(text_b)
    if not sections_a or not sections_b:
        return 0.0

    embeddings_a, embeddings_b = _paired_embeddings(sections_a, sections_b)
    matrix = cosine_similarity(embeddings_a, embeddings_b)

    best_a = matrix.max(axis=1) if matrix.size else np.array([0.0])
    best_b = matrix.max(axis=0) if matrix.size else np.array([0.0])
    score = ((best_a.mean() + best_b.mean()) / 2) * 100
    return round(float(score), 2)


def find_similar_sections(raw_text_a: str, raw_text_b: str, limit: int = 8) -> list[dict]:
    sections_a = split_into_sections(raw_text_a)
    sections_b = split_into_sections(raw_text_b)
    if not sections_a or not sections_b:
        return []

    embeddings_a, embeddings_b = _paired_embeddings(sections_a, sections_b)
    matrix = cosine_similarity(embeddings_a, embeddings_b)
    threshold = get_settings().section_similarity_threshold

    candidates = []
    for index_a, section_a in enumerate(sections_a):
        best_b_index = int(np.argmax(matrix[index_a]))
        semantic_score = float(matrix[index_a][best_b_index] * 100)
        if semantic_score < threshold:
            continue
        section_b = sections_b[best_b_index]
        lexical_score = calculate_lexical_similarity(section_a.lower(), section_b.lower())
        candidates.append(
            {
                "text_a_excerpt": section_a[:700],
                "text_b_excerpt": section_b[:700],
                "similarity": round(semantic_score, 2),
                "lexical_similarity": lexical_score,
            }
        )

    candidates.sort(key=lambda item: item["similarity"], reverse=True)
    return candidates[:limit]
