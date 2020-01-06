import xlwt

w = xlwt.Workbook()

sheet = w.add_sheet("sheet 1")

sheet.write(0,5,'test text')

w.save('aula.xls')
