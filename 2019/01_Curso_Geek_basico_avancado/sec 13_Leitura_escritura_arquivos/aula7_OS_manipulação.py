
import os

#os.path.exists('nome...') -> descobrir se um arquivo ou diretório existe

#true = existe , False = não existe

print(os.path.exists('./Meses'))

print(os.path.exists('./Meses/01_janeiro'))

print(os.path.exists('arquivo.py'))

#os.mknod('./nome.extensao') -> Criando arquivo

#os.scandir("./Meses") -> Scanear diretório

#os.rename('antigo','novo')

#os.remove('nome') #remove arquivo

#os.rmdir("nome") #remove diretorio (VAZIOS)

#os.removedirs("./Meses") # remove diretorio (Idem...somente VAZIOS)


#Removendo arquivo de um diretório------
for arquivo in os.scandir('./Meses'):

    if arquivo.is_file():
        print("deleta arquivo")
        #os.remove(arquivo.path)

    if not arquivo.is_file():
        print("deleta pasta")
        #os.rmdir(arquivo.path)
        #os.removedirs(arquivo.path)
#----------------------------------------