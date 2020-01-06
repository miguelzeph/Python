import xlrd

def read(arquivo):

    xls = xlrd.open_workbook(arquivo)

    plan = xls.sheets()[0]

    plan.row_values(0)

    for i in range(0,plan.nrows):

        linha = plan.row_values(i)

        #print '\ncoluna '+str(i)
        #print '\ncoluna ',i
        print '\ncoluna %s'%(i)
        
        raw_input()
        
        for l in range (0,len(linha)):

            
            print linha[l]



read('./teste.xls')


