import time

def calcular_duracao(funcao):
	def wrapper():
		ti = time.time()
		funcao()
		tf = time.time()
		print(f'{funcao.__name__} Tempo total é {tf-ti}')
	return wrapper#TEM QUE RETORNAR e Não PODE USAR wrapper()

@calcular_duracao
def main():
	for n in range(0,100):
		pass

main()
