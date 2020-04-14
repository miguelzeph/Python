def decorator(funcao):
	def check(a,b):
		if b == 0:
			print('Não é possível dividir')
			
		else:
			print(f'divisão deu {a/b}')
			return funcao(a,b)

	return check

@decorator
def dividir(a,b):
	return a/b

a = 1
b = 0

dividir(a,b) 

