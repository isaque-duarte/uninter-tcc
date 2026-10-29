from pydantic import BaseModel, Field


class SimilarSection(BaseModel):
    text_a_excerpt: str
    text_b_excerpt: str
    similarity: float = Field(ge=0.0, le=100.0)


class DuplicatedOrParaphrasedContent(BaseModel):
    type: str
    description: str


class ComparisonResult(BaseModel):
    final_correlation: float = Field(ge=0.0, le=100.0)
    lexical_similarity: float = Field(ge=0.0, le=100.0)
    semantic_similarity: float = Field(ge=0.0, le=100.0)
    similar_sections: list[SimilarSection]
    common_keywords: list[str]
    duplicated_or_paraphrased_content: list[DuplicatedOrParaphrasedContent]
    score_explanation: str

