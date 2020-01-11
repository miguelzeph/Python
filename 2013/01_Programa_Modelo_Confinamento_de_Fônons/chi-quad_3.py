CHI=[]

chi = 0
for i in range(0,len(IT)):
	
	chi= chi + ((I_TOTAL[i]-IR[i])**2)/IR[i]
		
grau = chi/len(IR)	
CHI.append(grau)


for i in range(0,len(CHI)):

	if CHI[i] == min(CHI):
		
		print ('chi-quad TOTAL='+str('%.6f')+' Total')%(CHI[i])
		
		ch='%.5f'%(CHI[i])
		
		fig_text.set_text('chi-q ='+ch)
		