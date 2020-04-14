class uppercase(object):
	def __init__(self,f):
		self.f=f
	def __call__(self,*args):
		self.f(args[0].upper())


@uppercase
def nome(nome):
	print("Nome %s"%nome)


nome('Miguel')
