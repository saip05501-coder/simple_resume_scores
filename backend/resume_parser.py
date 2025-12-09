import PyPDF2
import docx
import os

# Extract text from PDF
def extract_from_pdf(path):
    text = ""
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            try:
                text += page.extract_text() + "\n"
            except:
                pass
    return text

# Extract text from DOCX
def extract_from_docx(path):
    doc = docx.Document(path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Auto detect file type and extract
def extract_resume_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_from_pdf(file_path)
    elif ext == ".docx":
        return extract_from_docx(file_path)
    else:
        return "Unsupported file type. Use PDF or DOCX."