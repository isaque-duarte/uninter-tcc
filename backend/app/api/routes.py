from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.config import get_settings
from app.models.schemas import ComparisonResult
from app.services.comparison_engine import compare_pdfs
from app.services.pdf_extractor import PdfExtractionError

router = APIRouter()


def _is_pdf(file: UploadFile) -> bool:
    filename = file.filename or ""
    return filename.lower().endswith(".pdf") and file.content_type in {
        "application/pdf",
        "application/x-pdf",
        "application/octet-stream",
    }


@router.post("/compare", response_model=ComparisonResult)
async def compare_endpoint(
    text_a_pdf: Annotated[UploadFile | None, File()] = None,
    text_b_pdf: Annotated[UploadFile | None, File()] = None,
) -> ComparisonResult:
    if text_a_pdf is None or text_b_pdf is None:
        raise HTTPException(status_code=400, detail="Both PDF files are required.")

    if not _is_pdf(text_a_pdf) or not _is_pdf(text_b_pdf):
        raise HTTPException(status_code=400, detail="Both uploaded files must be PDFs.")

    text_a_bytes = await text_a_pdf.read()
    text_b_bytes = await text_b_pdf.read()
    max_size = get_settings().max_upload_size_bytes
    if len(text_a_bytes) > max_size or len(text_b_bytes) > max_size:
        raise HTTPException(status_code=400, detail="PDF files exceed the maximum allowed size.")

    try:
        return compare_pdfs(text_a_bytes, text_b_bytes)
    except PdfExtractionError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Comparison failed unexpectedly.") from exc
