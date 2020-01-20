"""
Dunder = D + under = Double Under... __x__


Dunder Name -> __name__ = se ele for = __main__ (executou diretamente), se ele for
= NomeArquivoPython (você importou o arquivo)

Dunder Main -> __main__ = quando você executa o programa diretamente

Em Python são utilizados Dunder para criar, funções, atributos, propriedades e etc...
utilizando Dunder para não gerar conflito.



# Na linguagem C - (SEM ISSO NÃO EXISTE PROGRAMA EM C...)

int main() {
    return 0;
}


# No Java

public static void main(String[] args){

}


# Em Python ...

Você coloca o código direto na linha de comando... o Próprio Python atribuirá à
variável __name__ o valor de __main__


OBS: if __name__ == "__main": ... é muito utilizado quando você cria uma biblioteca de
importe, mas quando você executa diretamente o arquivo, ele faz coisas diferentes para
você!!! e não faz quando você importa.

__name__ -> executando diretamente ele é igual __name__ = main
__name__ -> executando por importe, ele será igual __name__ = NomeArquivoPython (sem .py)


"""

import primeiro,segundo

primeiro.funcao1()

segundo.funcao2()
