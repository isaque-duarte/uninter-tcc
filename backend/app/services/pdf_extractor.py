import fitz


class PdfExtractionError(ValueError):
    pass


def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        with fitz.open(stream=file_bytes, filetype="pdf") as document:
            page_texts = []
            for page_number, page in enumerate(document, start=1):
                text = page.get_text("text").strip()
                if text:
                    page_texts.append(f"\n\n[Page {page_number}]\n{text}")
    except Exception as exc:
        raise PdfExtractionError("The uploaded PDF could not be read.") from exc

    raw_text = "\n".join(page_texts).strip()
    if not raw_text:
        raise PdfExtractionError("The uploaded PDF does not contain extractable text.")
    return raw_text

