import xlrd

def read(arquivo):

    xls = xlrd.open_workbook(arquivo)

    plan = xls.sheets()[0]

    plan.row_values(0)

    for i in range(0,plan.nrows):

        linha = plan.row_values(i)

        print linha



read('./teste.xls')


