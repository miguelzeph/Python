import xlrd

def read(arquivo):

    xls = xlrd.open_workbook(arquivo)

    plan = xls.sheets()[0]

    linha = plan.row_values(0)

    print linha



read('./teste.xls')

raw_input()

#obs: podia ser em extesao "ods" para calc em ver de 'xls' para excel

