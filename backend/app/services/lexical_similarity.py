from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_lexical_similarity(text_a: str, text_b: str) -> float:
    if not text_a.strip() or not text_b.strip():
        return 0.0

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform([text_a, text_b])
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100
    return round(float(score), 2)


def extract_common_keywords(text_a: str, text_b: str, limit: int = 20) -> list[str]:
    if not text_a.strip() or not text_b.strip():
        return []

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 1))
    matrix = vectorizer.fit_transform([text_a, text_b])
    feature_names = vectorizer.get_feature_names_out()

    weights_a = matrix[0].toarray()[0]
    weights_b = matrix[1].toarray()[0]
    common = []

    for index, keyword in enumerate(feature_names):
        if keyword in ENGLISH_STOP_WORDS:
            continue
        if weights_a[index] > 0 and weights_b[index] > 0:
            common.append((keyword, weights_a[index] + weights_b[index]))

    common.sort(key=lambda item: item[1], reverse=True)
    return [keyword for keyword, _ in common[:limit]]

