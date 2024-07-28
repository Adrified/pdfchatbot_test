from PyPDF2 import PdfReader
import os
import stat
from model import completion

my_path = 'enter path here'

def grant_access(path):
    if os.path.exists(path):
        try:
            os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH )
            print(f"Access granted to {path}")
        except Exception as e:
            print(f"Unable to grant access to {path}: {e}")

if os.path.exists(my_path):
    if os.access(my_path, os.R_OK):
        reader = PdfReader(my_path)
        page = reader.pages[0]
        extracted_page = page.extract_text()
        print(extracted_page)
    else:
        grant_access(my_path)
