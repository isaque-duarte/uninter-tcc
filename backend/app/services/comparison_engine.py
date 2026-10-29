from app.models.schemas import ComparisonResult
from app.services.lexical_similarity import calculate_lexical_similarity, extract_common_keywords
from app.services.pdf_extractor import extract_text_from_pdf
from app.services.preprocessor import preprocess_text
from app.services.result_builder import build_comparison_result
from app.services.semantic_similarity import calculate_semantic_similarity, find_similar_sections


def compare_pdfs(text_a_pdf: bytes, text_b_pdf: bytes) -> ComparisonResult:
    raw_text_a = extract_text_from_pdf(text_a_pdf)
    raw_text_b = extract_text_from_pdf(text_b_pdf)

    preprocessed_a = preprocess_text(raw_text_a)
    preprocessed_b = preprocess_text(raw_text_b)

    lexical_similarity = calculate_lexical_similarity(preprocessed_a, preprocessed_b)
    semantic_similarity = calculate_semantic_similarity(raw_text_a, raw_text_b)
    similar_sections = find_similar_sections(raw_text_a, raw_text_b)
    common_keywords = extract_common_keywords(preprocessed_a, preprocessed_b)

    return build_comparison_result(
        lexical_similarity=lexical_similarity,
        semantic_similarity=semantic_similarity,
        similar_sections=similar_sections,
        common_keywords=common_keywords,
    )

