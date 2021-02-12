import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

pdfs = list_files(dir_path, "pdf")

##############################################      add titles to footer
for pdf in pdfs:
    print("starting " +str(pdf))
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 8) #choose your font type and font size
    can.drawString(10, 5, str(pdf)[:-4])
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF

    file = open(pdf, "rb")
    existing_pdf = PdfFileReader(file)
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    i=0
    while i != None:
        print(str(i))
        try:
            page = existing_pdf.getPage(i)
            page.compressContentStreams()
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)
            i = i+1
        except:
            #print("while done")
            i = None
        
    # finally, write "output" to a real file
    outputStream = open("destination.pdf", "wb+")
    output.write(outputStream)
    outputStream.close()
    file.close()
    os.replace('destination.pdf', pdf)

############################################# footer over

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
