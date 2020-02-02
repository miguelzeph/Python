from veiculo import Veiculo


class Carro(Veiculo):#herdei as caracteristicas

    def __init__(self, cor, marca, tanque):

        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litros): #vai sobrepor da Classe "Veiculo"(Pai)

        if self.tanque+litros > 50:
            print(f"Tanque suporta apenas 50 Litros... "
                  f"você colocou {self.tanque + litros - 50} Litros a mais"
                  f"... não posso abastecer")

        else:
            self.tanque = self.tanque + litros

