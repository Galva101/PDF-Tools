import PyPDF2 as P
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

pdfs = list_files(dir_path, "pdf")

for pdf in pdfs:
    reader = P.PdfFileReader(open(pdf,'rb'))
    pagecount = reader.getNumPages()

    print("Pdf: "+str(pdf) +"\tPages: " +str(pagecount))

    page0 = reader.getPage(0)
    h = page0.mediaBox.getHeight()
    w = page0.mediaBox.getWidth()
    
    horizontalCells = 3
    verticalCells = 2
    
    newHeight = h*verticalCells
    newWidth = w*horizontalCells

    print("Dimensions:\t"+str(w)+" "+str(h))
    writer = P.PdfFileWriter()

    for j in range(0,pagecount,verticalCells*horizontalCells): #process all original pages that will go on one new page
        widePage = P.pdf.PageObject.createBlankPage(None, newWidth, newHeight) #new larger-sized pdf page
        
        for i in range(j,j+verticalCells*horizontalCells):
            if(i<pagecount):
                try:
                    print("Processing Page "+str(i+1)+" of "+str(pagecount))     
                    x = i%horizontalCells
                    y = i//horizontalCells
                    y=y%verticalCells #to prevent the y coordinate from getting larger than the new page
                    #print(str(y))
                    #print(str(x))
                    
                    page = reader.getPage(i)
                    widePage.mergeScaledTranslatedPage(page, 1, x*newWidth/horizontalCells, newHeight - (y*newHeight/verticalCells + h),True)
                    #here we insert a new page, because x starts at the left, we can simply take the coordinate of the new page and
                    #multiply the fraction of one pagewidth by it. For Y, because it would start from the bottom, we have to take the new Height
                    #of the large page, subtract the fraction of one pageheight, and also subtract one old pageheight again, to have the first page
                    #be in frame, since the bottom left corner is where the coordinates are anchored.
                except:
                    print("error at page "+ str(i+1) +"\t - skipping")
        widePage.compressContentStreams()
        writer.addPage(widePage)

    with open(pdf[:-4]+"_formatted.pdf", 'wb') as f:
        writer.write(f)
