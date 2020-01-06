import xlwt

# INDO MAIS FUNDO (Digging deeper)

#substituindo celulas (Overwriting cells)

wbk = xlwt.Workbook()

#antes de criar a celula , tem que colocar o comando "cell_overwrite_ok = True)"
#pois assim nao da erro.
sheet = wbk.add_sheet('aula',cell_overwrite_ok = True)

sheet.write(0,0,'some text')#some text = algum texto
sheet.write(0,0,'this should overwrite')# this should overwrite= este deve substitir

wbk.save('aula2.ods')
# perceba que poss salvar com extensoes diferente :

#ods --> libreoffice calc
#xls --> microsolft excel