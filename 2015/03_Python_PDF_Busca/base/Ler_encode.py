#fonte: http://victorwyee.com/python/convert-pdf-to-text-pypdf-pdfminer-first-impression/
import os
import glob
import pyPdf
 

filename = "teste.pdf"
 
def getPDFContent(filename):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(filename, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "/n"
    # Collapse whitespace
    content = " ".join(content.replace(u"/xa0", " ").strip().split())
    return content
 
# print getPDFContent(filename).encode("ascii", "ignore")
print getPDFContent(filename).encode("ascii", "xmlcharrefreplace")