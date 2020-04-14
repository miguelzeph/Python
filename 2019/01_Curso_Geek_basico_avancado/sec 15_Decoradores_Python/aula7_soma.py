def decorator(funcao):
	def check(a,b):
		if a == b:
			print('A é igual a B')
		elif a > b:
			print('A maior que B')
		else:
			print('A menor que B')

		return funcao(a,b)# SE não fizer,ele não retorna número, só None

	return check

@decorator
def somar(a,b):
	return a+b

a = 1
b = 2
soma =somar(a,b) + 10
print(soma)
