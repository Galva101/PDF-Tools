# PDF-Tools
This is a set of Python Scripts that provide some useful functionality in regards to editing/formatting.
The modules used in these scripts are *PyPDF2* and *Reportlab*, so make sure to have those installed when launching them.

## Crop Margins
This script generates a list of all PDF documents in a folder and calls the [*pdfCropMargins*](https://pypi.org/project/pdfCropMargins/) module on each, so make sure you have it installed. The layout has been preset to crop all pages in a document to the same uniform dimensions, if needed this could of course be changed in the call itself.

## Remove Metadata
This script can be used to strip all PDF documents in the same folder as the file off of their Author, Title, Subject, and Producer etc.
This information will be replaced by empty strings.

## Format
This script reformats every PDFs separately in the same Folder by taking its pages and aligning them to a specified grid on a new page, e.g. onto a 2x2 Grid. The new page size is calculated based on the PDFs own page size, and the
amount of horizontal and vertical cells can easily be changed in the script. The main use is to provide lossless reformatting, since many "Print to PDF" options compress fonts and vector based graphics.

## Merge
This script takes all PDFs in a folder and appends them together, and making their document titles bookmarks in the new document.

## Merge Titles
This script does the same thing as merge, but it will also overlay the original document title on the bottom left of each page in the concatenated document, so the user can easily
see which PDF a page originally belonged to.
