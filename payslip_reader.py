from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
from pathlib import Path
from typing import Union
import logging


class PaySlipReader:
    def __init__(self):
        pass

    def read_file(self):
        pass



def read_page(page_dict: dict):
    page_number = page_dict['page_number']
    page_text = page_dict['text']
    for line in page_text.split('\n'):
        print(line)

def read_one_document(document_path: Union[str, Path]):
    document_path = str(document_path)
    logging.info(f'Reading {document_path}')
    pdf_document = Document(
        document_path=document_path,
        language='heb'
    )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    for page in content:
        read_page(page)


def main():
    p = Path('data')
    for pdf_file_path in p.iterdir():
        read_one_document(pdf_file_path)
        break

if __name__ == "__main__":
    main()