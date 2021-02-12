from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os
import glob

filelist = glob.glob("*.pdf")  # Get a list of files in the current directory
filelist.sort()

for pdf in filelist:
    print("found "+ str(pdf)) 

for pdf in filelist:
    try:
        #opening the pdf and reading the metadata
        file_in = open(pdf, 'rb+')
        pdf_reader = PdfFileReader(file_in)
        metadata = pdf_reader.getDocumentInfo()

        #creating a new file, appending the pdf and adding custom metadata
        pdf_merger = PdfFileMerger()
        pdf_merger.append(file_in)
        pdf_merger.addMetadata({
            '/Author': "",
            '/Title': "",
            '/Subject' : "",
            '/Producer' : "",
            '/Creator' : "",
            '/Keywords' : "",
        })
        #writing the the new pdf document to a new file
        file_out = open('new.pdf', 'wb+')
        pdf_merger.write(file_out)

        file_in.close()
        file_out.close()
        #replacing the original file with the new one under the same name
        name = str(pdf)
        os.replace('new.pdf', name)

        print("done with " + str(pdf))
    except:
        print("error at "+ str(pdf))