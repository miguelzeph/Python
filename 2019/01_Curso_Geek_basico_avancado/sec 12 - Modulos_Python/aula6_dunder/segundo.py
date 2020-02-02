import primeiro

def funcao2():

    primeiro.funcao1()


#Serve para saber de onde está sendo executado o programa...
if __name__ == "__main__":

    print('segundo.py executado diretamente')

else:
    #print(__name__) #nome do meu __name__ = segundo
    print('segundo.py foi importado')