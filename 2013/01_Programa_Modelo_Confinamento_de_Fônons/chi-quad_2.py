CHI=[]

chi = 0
for i in range(0,len(IT)):
	
	chi= chi + ((Gamorfo_I[i]-IR[i])**2)/IR[i]
		
	
CHI.append(chi)


for i in range(0,len(CHI)):

	if CHI[i] == min(CHI):
		
		print ('A='+str('%.2f')+'nm '+'Ga='+str(' %.2f')+' '+'wo='+str('%.2f')+'chi-quad='+str('%.6f')+' Parte Amorfa')%(A,gamaa,wa,CHI[i])
		