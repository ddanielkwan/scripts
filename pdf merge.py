from PIL import Image
from PIL import Image
from PyPDF2 import PdfFileMerger

pdfs = ['a.pdf', 't.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()