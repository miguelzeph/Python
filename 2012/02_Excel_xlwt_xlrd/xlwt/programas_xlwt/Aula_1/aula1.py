import xlwt

w = xlwt.Workbook()

sheet = w.add_sheet("folha 1")

for i in range (0,10):
	for j in range (0,10):
		sheet.write(i,j,'texto_teste')

w.save('aula1.xls')
