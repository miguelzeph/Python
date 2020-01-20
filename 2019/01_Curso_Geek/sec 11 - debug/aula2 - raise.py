# Raise - serve para você colocar as explicações dos
# tipos de erros nas funções suas!!!

#NADA É EXECUTADO APÓS O RAISE!!!! ELA FINALIZA O PROGRAMA



#Modelo: raise TipoDoErro("zé mané, você errou")

#Exemplo: raise ValueError("Errouuuuuu kkk")


#Exemplo mais real:


def txt_num(txt,num):

    if type(txt) is not str:

        raise TypeError("Tem que ser uma string")

    if type(num) is not int:

        raise TypeError("Tem que ser um número INTEIRO")

    permitido = [1,3,5,7,9]

    if num not in permitido:

        raise ValueError("O número tem que ser ímpar de 0 - 10")

    print("Tudo ok, você usou Texto e Numero Inteiro corretamente")

txt_num('oi',9)


