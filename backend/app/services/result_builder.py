from app.core.config import get_settings
from app.models.schemas import (
    ComparisonResult,
    DuplicatedOrParaphrasedContent,
    SimilarSection,
)


def classify_score(score: float) -> str:
    if score >= 70.0:
        return "high"
    if score >= 40.0:
        return "medium"
    return "low"


def build_score_explanation(final_score: float, lexical_score: float, semantic_score: float) -> str:
    level = classify_score(final_score)
    if level == "high":
        return (
            "The score is high because the texts share important vocabulary and present "
            "semantically similar ideas across relevant sections."
        )
    if level == "medium":
        return (
            "The score is medium because the texts overlap in some terms or ideas, but "
            "also contain meaningful differences in wording or content."
        )
    return (
        "The score is low because the texts have limited shared vocabulary and few "
        "sections with close semantic meaning."
    )


def identify_duplicated_or_paraphrased_content(similar_sections: list[dict]) -> list[DuplicatedOrParaphrasedContent]:
    settings = get_settings()
    results: list[DuplicatedOrParaphrasedContent] = []
    has_duplicate = any(
        section["similarity"] >= settings.duplicated_threshold
        and section.get("lexical_similarity", 0) >= settings.duplicated_threshold
        for section in similar_sections
    )
    has_paraphrase = any(
        section["similarity"] >= settings.paraphrased_threshold
        and section.get("lexical_similarity", 100) < settings.duplicated_threshold
        for section in similar_sections
    )

    if has_duplicate:
        results.append(
            DuplicatedOrParaphrasedContent(
                type="duplicated",
                description="Some sections appear to use very similar wording in both texts.",
            )
        )
    if has_paraphrase:
        results.append(
            DuplicatedOrParaphrasedContent(
                type="paraphrased",
                description="Some sections express similar ideas using different wording.",
            )
        )
    return results


def build_comparison_result(
    lexical_similarity: float,
    semantic_similarity: float,
    similar_sections: list[dict],
    common_keywords: list[str],
) -> ComparisonResult:
    final_correlation = round((lexical_similarity * 0.40) + (semantic_similarity * 0.60), 2)
    formatted_sections = [
        SimilarSection(
            text_a_excerpt=section["text_a_excerpt"],
            text_b_excerpt=section["text_b_excerpt"],
            similarity=section["similarity"],
        )
        for section in similar_sections
    ]

    return ComparisonResult(
        final_correlation=final_correlation,
        lexical_similarity=round(lexical_similarity, 2),
        semantic_similarity=round(semantic_similarity, 2),
        similar_sections=formatted_sections,
        common_keywords=common_keywords,
        duplicated_or_paraphrased_content=identify_duplicated_or_paraphrased_content(similar_sections),
        score_explanation=build_score_explanation(final_correlation, lexical_similarity, semantic_similarity),
    )

