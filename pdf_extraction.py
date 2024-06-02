# done i think

import fitz # pymupdf

def pdf_extractor(path): # extracts text from pdf

    doc = fitz.open(path, filetype = "pdf")
    text = ""

    for page in doc:
        text += page.get_text()
    
    return text

pdf_path = 'put path right here'
text = pdf_extractor(pdf_path)
print(text)

