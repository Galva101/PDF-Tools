from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

pdfs = list_files(dir_path, "pdf")

merger = PdfFileMerger()

for pdf in pdfs:
    bookmark = os.path.basename(pdf[:-4])
    print(str(bookmark))
    merger.append(open(pdf, 'rb'), bookmark)

with open('result.pdf', 'wb+') as fout:
    merger.write(fout)
    fout.close()
    os.rename('result.pdf', 'merged.pdf')