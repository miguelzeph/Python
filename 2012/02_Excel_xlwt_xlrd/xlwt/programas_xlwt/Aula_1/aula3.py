import xlwt


wbk = xlwt.Workbook()

sheet = wbk.add_sheet('aula3')

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True #bold = negrito

style.font = font

sheet.write(0, 0, 'some bold Times text', style)

wbk.save('aula3.ods')