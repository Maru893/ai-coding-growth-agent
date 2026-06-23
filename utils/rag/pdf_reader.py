from pathlib import Path

from pypdf import PdfReader


def extract_pdf_pages(pdf_path: Path) -> list[dict]:
    reader = PdfReader(str(pdf_path))
    pages = []

    for page_index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append(
            {
                "source": pdf_path.name,
                "page": page_index,
                "text": text.strip()
            }
        )

    return pages


def load_all_pdf_pages(knowledge_base_dir: Path) -> list[dict]:
    all_pages = []

    for pdf_path in knowledge_base_dir.glob("*.pdf"):
        all_pages.extend(extract_pdf_pages(pdf_path))

    return all_pages