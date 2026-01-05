from pathlib import Path
from PyPDF2 import PdfReader

pdf_path = Path(__file__).parent / "sample.pdf"
print("Using file:", pdf_path)

reader = PdfReader(pdf_path)
page = reader.pages[0]
print(page.extract_text())
