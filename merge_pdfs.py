# pdf_merging.py

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = sys.argv[1:]
    merge_pdfs(paths, output='Article_with_SI.pdf')


