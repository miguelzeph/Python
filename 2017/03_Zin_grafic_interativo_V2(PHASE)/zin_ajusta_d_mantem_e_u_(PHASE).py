from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as si
from matplotlib.widgets import Slider, Button, RadioButtons
#from matplotlib.ticker import MultipleLocator
import os

#NESSE PROGRAMA EU VARIO APENAS A ESPESSURA D NA MEDIDA DE PLACA TEORICA... MANTENHO A PERMISSIVIDADE PERMEABILIDADE...
#ESSE METODO PARECE SER BOM  PARA ESTIMAR ESPESSURAS PROXIMAS...

#---------------LER ARQUIVO TXT NA PASTA-------------
TXT =[]

for arquivo in os.listdir('.'):
	if arquivo[len(arquivo)-4:] == '.txt':
		TXT.append(arquivo)
		
print '\nArquivo: ',TXT[0]	
	
arq = open(TXT[0],'r')
ler = arq.readlines()
arq.close()
#----------------------------------------------------

#-------------Ajuste da Referencia de L1 e L2---------
#Offset = 9.76mm
#L1, L2 e L = d....importante ser bem denifido

d = 1.56e-3 #[m] #Espessura da amostra (Livro chama de L)

L2 = 0e-3 #[m] #Plano de referencia porta 1
L1 = 9.76e-3 - d #[m]   #Plano de referencia porta 2

a =22.86e-3 #[m] #Dimensao maior do guia de onda (Banda-X)
#-------------------------------------------------------

#-------------------- CONSTANTES-----------------------------
c =2.998e8 #[m/s] #velocidade da Luz no vacuo

u0=4*np.pi*1e-7 # permeabilidade do vacuo

freq_corte = 6.56e9 # [Hz]

onda_cut= c/freq_corte #[m] #lambda de corte
#-------------------------------------------------------------





#-------------------------VETORES-1-------------------		
F=[] #frequencia [Hz] DE CALCULO
F_grafic=[] #FREQUENCIA PARA PLOTAR EM [GHz]

s11r=[] #real
s11i=[] #imag
s21r=[] #real
s21i=[] #imag

s11=[] # real + j imag
s21=[] # real + j imag

s11c=[] # real + j imag (Corrigido)
s21c=[] # real + j imag (Corrigido)





#---------------ORGANIZAR PARAMETROS-S em VETOR---------

ler1_col=1 #S11r
ler2_col=2 #S11i
ler3_col=5 #S21r #VNA PEDRO
ler4_col=6 #S21i #VNA PEDRO
#ler3_col=3 #S21r #VNA NEWTON
#ler4_col=4 #S21i #VNA NEWTON




for i in range(0,len(ler)):
	
	
	dados = ler[i].split(',')#VNA PEDRO
	#dados = ler[i].split('	')#VNA NEWTON
	
	#Ler frequencia
	f_colocar = float(dados[0]) #Hz
	F_grafic.append(f_colocar/1e9)
	
	F.append(f_colocar)
	
	#---------Alterei para ler modulo e fase----------- (contas basicas de polar para real e imaginario)
	#S11 modulo
	s11_mod = float(dados[ler1_col])
	#S11 Phase
	s11_ph = float(dados[ler2_col])*np.pi/180  #passar para rad
	
	#S21 modulo
	s21_mod = float(dados[ler3_col])
	#S21 Phase
	s21_ph = float(dados[ler4_col])*np.pi/180  #passar para rad
	
	s11r_new = np.cos(s11_ph)*(s11_mod)
	s11i_new = np.sin(s11_ph)*(s11_mod)
	
	
	s21r_new = np.cos(s21_ph)*(s21_mod)
	s21i_new = np.sin(s21_ph)*(s21_mod)
	
	#---------Organizar os PAR-S---------------------
	s11r.append(s11r_new)#real
	s11i.append(s11i_new)#imag
	s21r.append(s21r_new)#real
	s21i.append(s21i_new)#imag
	
	s11_colocar =s11r[i]+1j*s11i[i] # real + j imag
	s21_colocar =s21r[i]+1j*s21i[i] # real + j imag
	
	s11.append(s11_colocar) #add vetor s11
	s21.append(s21_colocar) #add vetor s21
	#--------------------------------------------------
	
	#----------------AJUSTAR PARAMETROS - S EXPERIMENTAIS-----------------------------------
	#lambda zero = comprimento de onda no vacuo
	onda = c/F[i] # [m]
	
	#Constante de propagacao da onda no espaco livre
	gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
	
	#Coeficiene para Ajustar os Planos de Referencia da porta 1 e 2
	R1 = np.exp(1*gama0*L1) #constantes
	R2 = np.exp(1*gama0*L2) #constantes
	
	#Ajustar S11 e S21
	s11c_colocar = R1*R1*s11_colocar
	s21c_colocar = R2*R1*s21_colocar
	
	'''
	#LEMBRE-SE DE ALTERAR QUANDO FOR USAR s12 e S22
	#s11c_colocar = R2*R2*s11_colocar #S22
	#s21c_colocar = R2*R1*s21_colocar #S12
	'''
	
	#Add S11 e S21 Corrigido
	s11c.append(s11c_colocar) #s11 novo
	s21c.append(s21c_colocar) #s21 novo
	#--------------------------------------------------------------
	

er_r = [] #permissividade real
er_i = [] #'''''''''''''' imag
ur_r = [] #permeabilidade real
ur_i = [] #'''''''''''''' imag

er_abs=[] #permissividade modulo
ur_abs=[] #permeabilidade modulo


#-------- CURTO TEORICO-----------------------------
Zin_a =[] #Zin Teorico com CURTO

Cvetor_curto_a =[] #Coeficiente de Reflexao com CURTO TEORICO


z_v=[] #[Ohm]

db_v =[] #[db]
	
s11_v =[] #[a.u]
	
refletividade_v=[] #[%]


EX = []
UX = []

for n in range(0,len(F)):
	#----------------------NRW PAR-S---------------------------------
	#OBS: SE EU USAR O s11c[n] e s21c[n] daqui pra baixo da problema!!!!
		
		
	#frequencia
	f = F[n]
		
		
	#lambda zero = comprimento de onda no vacuo
	onda = c/(f) # [m]
		
		
	#Constante de propagacao da onda no espaco livre
	gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
		
		
	#Constante de propagacao da onda no material(analitico) 
	#gamaX = (2j*np.pi/onda)*np.sqrt(e_a*u_a-(onda**2.0)/(onda_cut**2.0))
		
		
	#impedancia Analitica do Vacuo(za0)
	z_a0= (1j*u0*2*np.pi*f)/(gama0)
		
	#Z_a0.append(z_a0)
		
		
	#impedancia analitica do material (zma)
	#z_ma = ((1j*2*np.pi*f*u_a*u0)/(gamaX))/(z_a0) #z_a0 normliza
		
	#Z_ma.append(z_ma.real)
		
		
	#impedancia do material calculada  com par-S (zm)  #IGUAL DO NRW
	z_m = np.sqrt(((1+s11c[n])**(2)-s21c[n]**2)/((1-s11c[n])**(2)-s21c[n]**(2)))
		
	#Z_m.append(z_m.real)
		
		
	#coeficiente de transmissao Calculado 
	t = s21c[n]/(1-s11c[n]*((z_m-1)/(z_m+1)))
		
	#T.append(abs(t))
		
		
	#Coeficiente de transmissao Analitico
	#ta = np.exp(-gamaX*d)
		
	#T_a.append(abs(ta))
		
		
	#Valor K
	K = ((s11c[n])**(2.0)-(s21c[n])**(2.0)+1)/(2*s11c[n]) 
		
		
	#Coeficiente de reflexao Par-S
	#positivo
	C_p = K + np.sqrt(K**2-1)
	#negativo
	C_n = K - np.sqrt(K**2-1)
	#condicao para valor do sinal do coeficiente de reflexao
	if C_p < 1:
		sinal = 1
	elif C_n <= 1:
		sinal =-1
	#coeficiente de reflexao com sinal ok
	C = K+sinal*(np.sqrt(K**2-1))
		
	#Cvetor.append(abs(C))
		
	#velocidade da luz no guia
	c_lab = f/onda_cut
		
	#Coeficiente de refelxao Analitico 
	#C_analitico = ((gama0)/(u0)-(gamaX)/(u_a))/((gama0)/(u0)+(gamaX)/(u_a))
	#C_analitico = (((c)/(c_lab))*np.sqrt((u_a)/(e_a))-1)/(((c)/(c_lab))*np.sqrt((u_a)/(e_a))+1)
	#C_analitico = (z_ma-1)/(z_ma+1)
		
		
	#Cvetor_a.append(abs(C_analitico))
		
		
	#constante P
	P2=-((1.0)/(2*np.pi*d)*np.log(1.0/t))**2
	P=1.0/np.sqrt(P2)
		
		
	#constante Lamb
	lamb = np.sqrt((1.0)/(onda)**(2)-(1.0)/(onda_cut)**(2))
		
		
	#impedancia NRW (z_nrw) #IGUAL AO Z CALCULADO COM PAR-S (z_m)
	z_nrw = (1+C)/(1-C)
	#Z_nrw.append(z_nrw.real) #somente real
		
		
	#Permeabilidade NRW
	#ux = ux = z_nrw/(P*lamb)
	ux = z_m/(P*lamb) #poco melhor com z_m
	
	UX.append(ux)
		
	ur_r.append(ux.real)
	ur_i.append(ux.imag)
	ur_abs.append(abs(ux))
		
		
	#Permissividade NRW
	ex = ((onda)**(2)/ux)*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2)
	#ex = ((onda)**(2)/abs(ux))*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2) #abs(ux)
	
	ex = ex.real - 1j*ex.imag
	
	er_r.append(ex.real)
	er_i.append(ex.imag)
	er_abs.append(abs(ex))
	
	EX.append(ex)
		
		
	#----------Calculo do Coeficiente de Reflexao com Curto - TEORICO---------------------
		
		
	#---------Calcular Impedancia (Zin)---------------------------------------
	z = ((50)**(1.0/2.0))*np.tanh(1j*(2*np.pi*d/onda)*((ux*ex)**(1.0/2.0))) #acho que ta errado esse, mas bate experimental (art 118)
	z_v.append(z)
	#------------------------------------------------------------------------------------------
			
	#-------------Utilizar a impedancia para calcular dB (impedancia da linha 50 omg)------------------------
			
	#db= -20*np.log10(abs((z-1)/(z+1))) #dB #somente para voltagem
	db = -10*np.log10(abs((z-50)/(z+50))) #dB para potencia
	db_v.append(db)
	#---------------------------------------------------------------------------
			
			
	#-------Calcular S11 utilizando dB----------------------------------------
	s11 = (10.0**((db/10.0))) # a.u
	s11_v.append(s11)
			
	#-----------------------------------------------------------------------
			
			
	#---------------Reflectividade = s11 ao quadrado (PORCENTAGEM)--------------------------
	refletividade = (s11**2.0)*100
	refletividade_v.append(refletividade)
			
	#-----------------------------------------------------------------------



#### GRAFICO 1
ax1=plt.subplot(121)
plt.subplots_adjust(left=0.1, bottom=0.3)
k, =plt.plot(F_grafic,refletividade_v,'r-',linewidth=4,label="Theoretical Atenuation")

#k, =plt.plot(F_grafic,db_v,'r-',linewidth=4,label="Theoretical $\epsilon$'")


#copy;;;;
plt.xlabel('Frequency(GHz)')
plt.ylabel("Atenuation (%)")
plt.ylim(0,100)
plt.xlim(8.2,12.4)
	
#plt.title(str(TXT[arquivo][:TXT(txts[arquivo])-4]))

plt.legend()
plt.grid(True)
	

	
### Grafico 2


	
#-------GRAFICO2 - V ----------------------------------------
ax2=plt.subplot(122)

e1, =plt.plot(F_grafic,er_r)
e2, =plt.plot(F_grafic,er_i)

u1, =plt.plot(F_grafic,ur_r)
u2, =plt.plot(F_grafic,ur_i)


plt.xlabel('Frequency(GHz)')
plt.ylabel('Relative $\epsilon$" and $\epsilon$"')
#plt.ylim(-1,3)
plt.xlim(8.2,12.4)

#plt.legend()
plt.grid(True)
	

#---------------------------------------programa interacao----------------------------------------------
axcolor=(0.5,0.7,0.7)

di = 0e-3
df = 9.8e-3

d_ = plt.axes([0.25, 0.05, 0.65, 0.03], axisbg=axcolor)#(pos(x da barra),pos(y da barra),comprimento,largura)
dbar= Slider(d_, 'espessura', di, df, valinit=d, valfmt='%.2e')

#-------------------------------------------------------------------------------------------------------


def update(val):#este val nao tem nada a ver com ...
						#
	#d = dbar.val #este val...
	d = dbar.val
	
	'''
	L1 = 0e-3 #[m] #Plano de referencia porta 1
	L2 = 9.76e-3 - d  #[m]   #Plano de referencia porta 2
	
	
	s11c =[]
	s21c =[]
	
	#----------------------------------ARRUMA NOVAMENTE OS PAR-S com novo d----------------------------------
	for i in range(0,len(ler)):
	
		s11_colocar =s11r[i]+1j*s11i[i] # real + j imag
		s21_colocar =s21r[i]+1j*s21i[i] # real + j imag
		
		#s11.append(s11_colocar) #add vetor s11
		#s21.append(s21_colocar) #add vetor s21
		#--------------------------------------------------
		
		#----------------AJUSTAR PARAMETROS - S EXPERIMENTAIS-----------------------------------
		#lambda zero = comprimento de onda no vacuo
		onda = c/F[i] # [m]
		
		#Constante de propagacao da onda no espaco livre
		gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
		
		#Coeficiene para Ajustar os Planos de Referencia da porta 1 e 2
		R1 = np.exp(1*gama0*L1) #constantes
		R2 = np.exp(1*gama0*L2) #constantes
		
		#Ajustar S11 e S21
		s11c_colocar = R1*R1*s11_colocar
		s21c_colocar = R2*R1*s21_colocar
		
		
		
		#Add S11 e S21 Corrigido
		s11c.append(s11c_colocar) #s11 novo
		s21c.append(s21c_colocar) #s21 novo
	#--------------------------------------------------------------------------------------
	
	
	
	
	
	
	#--------------------------------Calcular o NRW E O ZIN NOVAMENTE--------------------------------
	
	
	
	
	er_r = [] #permissividade real
	er_i = [] #'''''''''''''' imag
	ur_r = [] #permeabilidade real
	ur_i = [] #'''''''''''''' imag

	er_abs=[] #permissividade modulo
	ur_abs=[] #permeabilidade modulo
	'''
	
	#-------- CURTO TEORICO-----------------------------
	Zin_a =[] #Zin Teorico com CURTO

	Cvetor_curto_a =[] #Coeficiente de Reflexao com CURTO TEORICO


	z_v=[] #[Ohm]

	db_v =[] #[db]
		
	s11_v =[] #[a.u]
		
	refletividade_v=[] #[%]
	
	
	for n in range(0,len(F)):
		#----------------------NRW PAR-S---------------------------------
		#OBS: SE EU USAR O s11c[n] e s21c[n] daqui pra baixo da problema!!!!
		
		
		#frequencia
		f = F[n]
		
		
		#lambda zero = comprimento de onda no vacuo
		onda = c/(f) # [m]
		
		'''
		#Constante de propagacao da onda no espaco livre
		gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
		
		
		#Constante de propagacao da onda no material(analitico) 
		#gamaX = (2j*np.pi/onda)*np.sqrt(e_a*u_a-(onda**2.0)/(onda_cut**2.0))
		
		
		#impedancia Analitica do Vacuo(za0)
		z_a0= (1j*u0*2*np.pi*f)/(gama0)
		
		#Z_a0.append(z_a0)
		
		
		#impedancia analitica do material (zma)
		#z_ma = ((1j*2*np.pi*f*u_a*u0)/(gamaX))/(z_a0) #z_a0 normliza
		
		#Z_ma.append(z_ma.real)
		
		
		#impedancia do material calculada  com par-S (zm)  #IGUAL DO NRW
		z_m = np.sqrt(((1+s11c[n])**(2)-s21c[n]**2)/((1-s11c[n])**(2)-s21c[n]**(2)))
		
		#Z_m.append(z_m.real)
		
		
		#coeficiente de transmissao Calculado 
		t = s21c[n]/(1-s11c[n]*((z_m-1)/(z_m+1)))
		
		#T.append(abs(t))
		
		
		#Coeficiente de transmissao Analitico
		#ta = np.exp(-gamaX*d)
		
		#T_a.append(abs(ta))
		
		
		#Valor K
		K = ((s11c[n])**(2.0)-(s21c[n])**(2.0)+1)/(2*s11c[n]) 
		
		
		#Coeficiente de reflexao Par-S
		#positivo
		C_p = K + np.sqrt(K**2-1)
		#negativo
		C_n = K - np.sqrt(K**2-1)
		#condicao para valor do sinal do coeficiente de reflexao
		if C_p < 1:
			sinal = 1
		elif C_n <= 1:
			sinal =-1
		#coeficiente de reflexao com sinal ok
		C = K+sinal*(np.sqrt(K**2-1))
		
		#Cvetor.append(abs(C))
		
		#velocidade da luz no guia
		c_lab = f/onda_cut
		
		#Coeficiente de refelxao Analitico 
		#C_analitico = ((gama0)/(u0)-(gamaX)/(u_a))/((gama0)/(u0)+(gamaX)/(u_a))
		#C_analitico = (((c)/(c_lab))*np.sqrt((u_a)/(e_a))-1)/(((c)/(c_lab))*np.sqrt((u_a)/(e_a))+1)
		#C_analitico = (z_ma-1)/(z_ma+1)
		
		
		#Cvetor_a.append(abs(C_analitico))
		
		
		#constante P
		P2=-((1.0)/(2*np.pi*d)*np.log(1.0/t))**2
		P=1.0/np.sqrt(P2)
		
		
		#constante Lamb
		lamb = np.sqrt((1.0)/(onda)**(2)-(1.0)/(onda_cut)**(2))
		
		
		#impedancia NRW (z_nrw) #IGUAL AO Z CALCULADO COM PAR-S (z_m)
		z_nrw = (1+C)/(1-C)
		#Z_nrw.append(z_nrw.real) #somente real
		
		
		#Permeabilidade NRW
		#ux = ux = z_nrw/(P*lamb)
		ux = z_m/(P*lamb) #poco melhor com z_m
		#ux = ux.real -1j*ux.imag
		
		#ux= ux.real-1j*ux.imag
		
		ur_r.append(ux.real)
		ur_i.append(ux.imag)
		ur_abs.append(abs(ux))
		
		
		#Permissividade NRW
		ex = ((onda)**(2)/ux)*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2)
		ex= ex.real-1j*ex.imag
		#ex = ((onda)**(2)/abs(ux))*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2) #abs(ux)
		
		er_r.append(ex.real)
		#er_i.append(-1*ex.imag)
		er_i.append(ex.imag)
		er_abs.append(abs(ex))
		
		
		
		#ux = ur_r[n]+1j*ur_i[n]
		#ex = er_r[n]+1j*er_i[n]
		#----------Calculo do Coeficiente de Reflexao com Curto - TEORICO---------------------
		
		'''
		
		#ESTOU USANDO O MSM VALOR DA PERMESSIVIDADE CALCULADA LA EM CIMA
		#MAS AGORA VARIO APENAS O D...
		
		#---------Calcular Impedancia (Zin)---------------------------------------
		z = ((50)**(1.0/2.0))*np.tanh(1j*(2*np.pi*d/onda)*((UX[n]*EX[n])**(1.0/2.0))) #acho que ta errado esse, mas bate experimental (art 118)
		z_v.append(z)
		#------------------------------------------------------------------------------------------
			
		#-------------Utilizar a impedancia para calcular dB (impedancia da linha 50 omg)------------------------
			
		#db= -20*np.log10(abs((z-1)/(z+1))) #dB #somente para voltagem
		db = -10*np.log10(abs((z-50)/(z+50))) #dB para potencia
		db_v.append(db)
		#---------------------------------------------------------------------------
			
			
		#-------Calcular S11 utilizando dB----------------------------------------
		s11 = (10.0**((db/10.0))) # a.u
		s11_v.append(s11)
			
		#-----------------------------------------------------------------------
			
			
		#---------------Reflectividade = s11 ao quadrado (PORCENTAGEM)--------------------------
		refletividade = (s11**2.0)*100
		refletividade_v.append(refletividade)
			
		#-----------------------------------------------------------------------
	
	k.set_ydata(refletividade_v)
	
	e1.set_ydata(er_r)
	e2.set_ydata(er_i)
	u1.set_ydata(ur_r)
	u2.set_ydata(ur_i)
	
	
	#k.set_ydata(db_v)
	
	plt.draw()
	

dbar.on_changed(update)

'''
#Reset....
resetax = plt.axes([0.8, 0.2, 0.1, 0.04]) #posicao do botao...
button1 = Button(resetax, 'Reset', color=axcolor, hovercolor='0.5')
def reset(event):
	lbar.reset()#volta pARA O VALINIT
	gamabar.reset()
	wobar.reset()
	#lbar.val=15
	#l.bar.on_changed=15
	
button1.on_clicked(reset) #precisa de um click
#programa interacao****************************-----------------------))))))))))))))-------------------
'''

plt.show()