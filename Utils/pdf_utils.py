import pdfplumber

def extract_text_from_pdf(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() + '\n'
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF: {str(e)}"
