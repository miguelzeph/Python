def funcao1():

    print('Hello World')



#Serve para saber de onde está sendo executado o programa...
if __name__ == '__main__':

    funcao1()

    print('primeiro.py está sendo executado diretamente')

else:

    #print(__name__) #Nome do meu __name__ = primeiro
    print('primeiro.py foi importado')