import os
for f in range(1,5):
	if os.path.exists("./entrada/erro"+str(f)+".txt"):
		velho=open("./entrada/erro"+str(f)+".txt",'r')
		antigo=velho.readlines()
		velho.close()
		total=len(antigo) #retorna a quantidade de linhas
		#---------------------------------------------------
		novo=open("./saida/ajustar"+str(f)+".txt",'w')
		novo.write(antigo[0])
		
		for i in range(0,total):
			if ((i % 2) == 0): #% resto....
				continue #pular primeira linha
			else:
				novo.write(antigo[i])
		
		novo.close()
