"""

'r' (default) - leitura
'w' - escrita, se o arquivo existir, ele escreve por cima
'x' - abre para escrita, somente se o arquivo não existir... se existir, ele dá erro...
'a' - ele cria o arquivo se não existir, e ele existir, ele adiciona o conteúdo ...
mas adiciona sempre no FIM (default)
'+' exemplo: 'r+' - abre para o modo de atualização de leitura ou escrita...




"""
#Vamos testar o 'x'
try:
    with open('novo.txt', 'x') as arquivo:
        arquivo.write('Hello World kkkk')

except:
    print('O arquivo já existe...')


#Vamos testar o 'a'
arquivo = open('novo.txt','a')

arquivo.write('Mais um\n') #Por padrão adiciona no fim do arquivo

#quero adicionar no início... use o Seek lembra?
arquivo.seek(0)
arquivo.write('No início agora \n')

arquivo.close()


arq = open('new.txt','w')
arq.write('oi \ntchau \n')
arq.seek(0)
arq.close()

arq = open('new.txt','a')
arq.write("agora eu escrevi no inicio \n")
arq.close()