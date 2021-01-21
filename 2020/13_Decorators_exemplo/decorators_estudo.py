
#Decorator Simples

def velho_ou_novo(func):#Decorator
	def wrap(*args,**kwargs):
		age = func(*args,**kwargs)
		if age <= 15:
			print('novo')
		elif age <= 30:
			print('adulto')
		else:
			print('velho')
	return wrap

@velho_ou_novo
def idade(x):
	return x

idade(25)
############################################################################
############################################################################
# Decorator com parâmetro
def bonus(func):
	def warp(*args,**kwargs):
		resto = func(*args,**kwargs)
		if  resto <= 1500:
			print('pagar bonus de 350')
		elif resto > 1500:
			print("não tem bonus, você ganha 1500 ou mais")
	return warp

@bonus
def salario(pagar, desconto):
	resto = pagar - desconto
	return resto

salario(1600,100)
############################################################################
############################################################################
# Decorator com parâmetro
def se_for(chato = []):
	def decorator(view_func):
		def warp(*args,**kwargs):
			nome = view_func()
			if nome in chato:
				print(f"Esse tal de {nome} é chato")
			else:
				print(f"o {nome} é legal, chato são {chato}")
		return warp	
	return decorator


@se_for(chato = ['Ana', 'Priscila'])
def quem_e():
	nome = 'Miguel'
	return nome

quem_e()
	

