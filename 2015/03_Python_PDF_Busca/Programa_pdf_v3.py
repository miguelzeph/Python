#fonte: http://victorwyee.com/python/convert-pdf-to-text-pypdf-pdfminer-first-impression/
import os
import glob
import pyPdf
 

 

#Gravar nome do arquivo em vetor txts-----------------------------------
lista=os.listdir('.')
txts=[]

for i in range(0,len(lista)):
	if (lista[i].find('.pdf') == -1):#find quando n tem ele retorna -1
		continue
	else:
		txts.append(lista[i]) 
#-----------------------------------------------------------------------

 
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
 
for filename in txts:
	
	escrever = getPDFContent(filename).encode("ascii", "xmlcharrefreplace")
	vetor = escrever.split(' ')
	
	for j in range(0,len(vetor)):
		
		if vetor[j] == 'Raman':
			print filename
			break
		else:
			continue
			
			
		
	
	
	
	