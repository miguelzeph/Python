# -*- coding: utf-8 -*-

from pyPdf import PdfFileWriter, PdfFileReader

input = PdfFileReader(file("teste.pdf","rb"))

print "titulo = %s" %(input.getDocumentInfo().title)

print "document1.pdf has %s pages" %input.getNumPages()