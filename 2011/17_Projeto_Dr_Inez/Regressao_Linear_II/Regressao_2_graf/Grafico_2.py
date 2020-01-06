

os.chdir('./entrada_2')
vetor = os.listdir('.')

if vetor[0] == 'foF2.txt':
	
	
	
	
	arq=open('./'+vetor[0],'r')
	ler=arq.readlines()
	arq.close()
	
	
	t=[]
	
	
	
		
	for i in range(0,len(ler)):
			
		foF2=ler[i][24:30]
			
		if foF2 == '------' or foF2 == 'n__tem':
				
			t.append(None)
			
		else:
			t.append(float(foF2))

	
if vetor[1] == 'solar.txt':
	#Restrincao
	arq=open('./'+vetor[1],'r')
	ler=arq.readlines()
	arq.close()
	
	a=0
	b=365
	
	w=[]
	t1=[]
	
	#for i in range(0,len(ler)):
	for i in range(a,b):
		
		
		foF2=t[i]
		flux=ler[i][17:21]
		
		
		
		if (int(flux) < 660 or int(flux) > 780):
			continue
		elif foF2 == None:
			continue
		
		else:
			w.append(int(flux)/10.0)
			t1.append(foF2)

		
		
		
#for j in range(0,365):
#	print x[j],y[j]




C=[]
D=[]

for i in range (0,len(x)):
	
	#if ((x[i] == None )or (y[i] == None)):
	#	continue
	
	#else:
	
	b= ((w[i]-np.mean(w))*(t1[i]-np.mean(t1)))/(w[i]-np.mean(w))**2
	a = np.mean(t1) - b*np.mean(w)
		
	C.append(b)
	D.append(a)

#print B
#print A		
#raw_input()

c = np.mean(C)
d = np.mean(D)

h = np.arange(66,78,1)

u = d + c*h


plt.figure(num=1,figsize=(20,10))


plt.rcParams["xtick.major.size"]=10
plt.rcParams["xtick.minor.size"]=5
plt.rcParams["ytick.major.size"]=10
plt.rcParams["ytick.minor.size"]=5
		
sub1=plt.subplot(1,1,1)

x_maior=2
x_menor=1
y_maior=1
y_menor=0.5
		
sub1.xaxis.set_major_locator(MultipleLocator(x_maior))
sub1.xaxis.set_minor_locator(MultipleLocator(x_menor))
		
sub1.yaxis.set_major_locator(MultipleLocator(y_maior))
sub1.yaxis.set_minor_locator(MultipleLocator(y_menor))



plt.xlabel('Fluxo Solar')
plt.ylabel('foF2(MHz)')
plt.title('Grafico_Teste')


plt.plot(x,y1,'ro',lw=2,label=u"Fev 1996 - Jan 1997")
plt.plot(Q,s,'r-',lw=2,label=u'Regressão Linear 1996')

plt.plot(w,t1,'bo',lw=2,label=u"Jan 2009 - Dez 2009")
plt.plot(h,u,'b-',lw=2,label=u'Regressão Linear 2009')


plt.legend().get_frame().set_facecolor('0.95')
plt.ylim(3.5,13.5)
plt.xlim(66,78)
plt.grid(True)
plt.show()
#plt.savefig('./grafico_teste.png')	
