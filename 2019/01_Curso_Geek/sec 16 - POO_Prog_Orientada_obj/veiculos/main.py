from veiculo import Veiculo
from carro import Carro


carro = Carro(cor = 'Azul', marca = "Ford", tanque = 10)


#print(carro.__dict__)
#print(carro.cor, carro.rodas, carro.marca, carro.tanque)

moto = Veiculo('rosa', 2, 'yamaha', 2)

carro.abastecer(10)
moto.abastecer(1)

print(carro.tanque) #Antes tinha 10L, coloquei mais 10L = 20L
print(moto.tanque) # 2+1=3L

carro.abastecer(20)

print(carro.tanque)

carro.abastecer(30)

print(carro.tanque)



