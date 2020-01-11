# -*- coding: utf-8 -*-

from pyPdf import PdfFileReader
import os
import glob


filename= "facil.pdf"

input = PdfFileReader(file(filename,"rb"))

for page in input.pages:

	print page.extractText()
