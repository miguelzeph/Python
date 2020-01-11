CHI=[]

chi = 0
for i in range(0,len(IT)):
	
	chi= chi + ((IT[i]-IR[i])**2)/IR[i]
		
		
		
	
CHI.append(chi)


for i in range(0,len(CHI)):

	if CHI[i] == min(CHI):
		
		print ('L='+str('%.2f')+'nm '+'Ga='+str(' %.2f')+' '+'wo='+str('%.2f')+'chi-quad='+str('%.6f')+' Parte Cristalina')%(L*0.54,Gama,wo,CHI[i])
#nao me interessa o Chi da parte amorfa...		