# -*- coding: utf-8 -*-

from pyPdf import PdfFileWriter, PdfFileReader

pdf = PdfFileReader(file("teste.pdf","rb"))

info = pdf.getDocumentInfo()

pdf_author= info.author
pdf_title= info.title


#linha
#print pdf_author+'\n\n'
#print pdf_title+'\n\n' Unicode error
#print info
#print pdf.getNumPages()
print pdf.pages(0).extractText()