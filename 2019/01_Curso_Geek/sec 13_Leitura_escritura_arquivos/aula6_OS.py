"""
Sistema de Arquivos e Navegação

os -> Operating System (Sistema operacional)



import os

#getcwd() -> pega atual diretorio

print(os.getcwd())

#Mudar Diretorio - chdir()

os.chdir('..') #voltar
print(os.getcwd())

# checar se um Dir é relativo
#ou absoluto...

print(os.path.isabs('/home')) #Está na Raiz
print(os.path.isabs('home')) #n está na raiz (linux / é o root)



"""

#Aplicação Legal...

import os

#Fiz isso para evitar o erro... Mas descobri que a funcao os.mkdirs() tem um
#parâmetro que não devolve o erro...
# assim...  os.mkdirs("nome",exist_ok = True) = se existir, ele ignora
if os.path.exists('./Meses') == True:

    print("Diretório já existe...")

else:

    caminho = os.getcwd()

    #cria pasta
    os.makedirs("Meses")

    caminho_pasta = caminho+'/Meses'
    #muda de diretorio
    os.chdir(caminho_pasta)


    meses = ['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

    c = 1

    for i in range(0,len(meses)):

        if i < 10:
            #cria pasta mês com zero na frente
            os.makedirs('0'+str(c)+'_'+meses[i])

            #mudar para diretorio
            os.chdir('0'+str(c)+'_'+meses[i])
        else:
            # cria pasta mês
            os.makedirs(str(c) + '_' + meses[i])

            # mudar para diretorio
            os.chdir(str(c) + '_' + meses[i])

        c +=1


        for j in range(1,11):

            open('arquivo_' + str(j) + '.txt', 'w').close()

            #arq = open('arquivo_'+str(j)+'.txt','w')
            #arq.close()

        # mudar para diretorio anterior (pasta meses)
        os.chdir('..')