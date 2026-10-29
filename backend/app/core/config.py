from functools import lru_cache

from pydantic import BaseModel


class Settings(BaseModel):
    allowed_origins: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
    max_upload_size_bytes: int = 10 * 1024 * 1024
    semantic_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    duplicated_threshold: float = 92.0
    paraphrased_threshold: float = 78.0
    section_similarity_threshold: float = 70.0


@lru_cache
def get_settings() -> Settings:
    return Settings()

