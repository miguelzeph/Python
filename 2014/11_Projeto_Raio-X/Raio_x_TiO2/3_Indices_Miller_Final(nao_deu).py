from __future__ import division



valores = [8,14,16,18,20,31,32,39,40,46]
a=4.5929
c=2.9591
						
planos = {}
for i in range(0,len(valores)):
	planos[i]=[]
	for l in range(0,10):
		
		for k in range(0,10):
			
			for h in range(0,10):
			#Mudei a ordem do loop h,k,l para deixar os valores hkl crescentes
			
				hkl= (h**2+k**2)/(a**2)+(l**2)/(c**2)
				
				if "%.0e"%(hkl) == "%.0e"%(valores[i]):
					planos[i].extend(["(%.0f,%.0f,%.0f)"%(h,k,l)])
arq = open('3_plano.txt','w')					
for i in range(0,len(valores)):
	try:
		escrever = "%s\n"%(planos[i][0])
		arq.write(escrever)
	except:
		escrever = "%s\n"%("Retirar Pico")
		arq.write(escrever)
arq.close()



	

	



	



