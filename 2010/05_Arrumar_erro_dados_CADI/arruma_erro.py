import os
for i in range(1,32):
	if os.path.exists('./entrada/CE103'+str(i)+'.dat'):
		
		os.path.exists('./entrada/CE103'+str(i)+'.dat')
		velho=open('./entrada/CE103'+str(i)+'.dat','r')
		antigo=velho.readlines()
		velho.close()
		total=len(antigo)
		
		novo=open('./saida/CE103'+str(i)+'.txt','w')
		novo.write(antigo[0])	
		for f in range(0,total):
			if ((f % 2) == 0):
				continue
			else:
				novo.write(antigo[f])
		novo.close()