# coding: utf-8

#Neste programa voce podera optar por calcular S11 e S21 ou 
#S22 e  S12... Devem ser iguais os resultados

#Calcula Modulo Linear
#Calcula Modulo (dB)
#Calcula Fase
#Calcula Absorbancia
#Calcula Impedancia
#Calcula Indice de Refracao
#Calcula Coeficiente de Transmissao
#Calcula Coeficiente de Reflexao
#Calcula Permissividade
#Calcula Permeabilidade
#Calcula Zin (curto)
#Calcula coeficiente de Reflexao (curto)

from __future__ import division
import os 
import numpy as np
import matplotlib.pyplot as plt



#tamanho do plot
x = 6
y = 6
#fonte dos eixos x e y
fonte = 14

#pular pontos
skip_point = 30


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

d = 5.1e-3 #[m] #Espessura da amostra (Livro chama de L)

L1 = 0e-3 #[m] #Plano de referencia porta 1
L2 = 9.76e-3 - d #[m]   #Plano de referencia porta 2

a =22.86e-3 #[m] #Dimensao maior do guia de onda (Banda-X)
#-------------------------------------------------------



#--------------Permissividade e Permeabilidade (Chute)------

e_a = 2.04 - 0.0j #Analitico teflon
u_a = 1.0 - 0.0j    #Analitico teflon
#------------------------------------------------------------



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



s11c_teorico=[] # real + j imag (Corrigido)
s21c_teorico=[] # real + j imag (Corrigido)

#-----------------------------------------------------




#---------------ORGANIZAR PARAMETROS-S em VETOR---------

ler1_col=1 #S11r
ler2_col=2 #S11i
ler3_col=5 #S21r
ler4_col=6 #S21i

'''
#Caso eu queira usar o S12 e S22 tenho que alterar o:
#s11c_colocar = R2*R2*s11_colocar
#s21c_colocar = R2*R1*s21_colocar

ler1_col=7 #S22r
ler2_col=8 #S22i
ler3_col=3 #S12r
ler4_col=4 #S12i
'''

for i in range(0,len(ler)):
	
	
	dados = ler[i].split(',')
	
	#Ler frequencia
	f_colocar = float(dados[0]) #Hz
	
	F.append(f_colocar)
	
	
	#---------Organizar os PAR-S---------------------
	s11r.append(float(dados[ler1_col]))#real
	s11i.append(float(dados[ler2_col]))#imag
	s21r.append(float(dados[ler3_col]))#real
	s21i.append(float(dados[ler4_col]))#imag
	
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
	
	
	#----------------------Calcular Par-S Teorico------------------
	#Constante de propagacao da onda no material
	gamaX = (2j*np.pi/onda)*np.sqrt(e_a*u_a-(onda**2.0)/(onda_cut**2.0))
	
	#Impedancia Analitica do Vacuo
	z_a0= (1j*u0*2*np.pi*f_colocar)/(gama0)
	
	#Impedancia Analitica do MAterial (Normalizada)
	z_ma = ((1j*2*np.pi*f_colocar*u_a*u0)/(gamaX))/(z_a0) #z_a0 normliza
	
	#Coeiciente de Reflexao Analitico
	Ca = (z_ma-1)/(z_ma+1)
	
	#Coeficiente de transmissao Analitico
	ta = np.exp(-gamaX*d)
	
	#Calcular S11 e S21 Teorico e Corrigir
	s11c_colocar_teorico = R1*R1*((Ca*(1-ta**2))/(1-(Ca**2)*(ta**2)))
	s21c_colocar_teorico = R2*R1*((ta*(1-Ca**2))/(1-(Ca**2)*(ta**2)))
	
	'''
	#LEMBRE-SE DE ALTERAR QUANDO FOR USAR s12 e S22
	#s11c_colocar_teorico = R2*R2*((Ca*(1-ta**2))/(1-(Ca**2)*(ta**2))) #S22
	#s21c_colocar_teorico = R2*R1*((ta*(1-Ca**2))/(1-(Ca**2)*(ta**2))) #S12
	'''
	
	
	#Add S11 e S21 Teorico Corrigido
	s11c_teorico.append(s11c_colocar_teorico)
	s21c_teorico.append(s21c_colocar_teorico)

	
	F_grafic.append(f_colocar/1e9)
#--------------------------------------------------------------	
	
	
#-------------- Modulo de S11 e S21 (Prova real) ---------------

S11_mod_c=[] #Experimental Corrigido
S21_mod_c=[] #Experimental Corrigido 

S11_mod=[] # Experimental sem corrigir
S21_mod=[] # Experimental sem corrigir

S11_mod_c_teorico =[] #Teorico Corrigido
S21_mod_c_teorico =[] #Teorico Corrigido

		

for i in range(0,len(s11)):
	
	S11_mod_c.append(abs(s11c[i]))# Exp Corrigido
	S21_mod_c.append(abs(s21c[i]))# Exp Corrigido
	
	S11_mod.append(abs(s11[i])) #Exp sem corrigir
	S21_mod.append(abs(s21[i])) #Exp sem corrigir
	
	S11_mod_c_teorico.append(abs(s11c_teorico[i])) #Teorico Corrigido
	S21_mod_c_teorico.append(abs(s21c_teorico[i])) #Teorico Corrigido

	
#-------PLOTE LINEAR MAG: TEORICO X EXP (AMBOS AJUSTADOS)---------
fig=plt.figure(num=1,figsize=(x,y))


plt.plot(F_grafic,S11_mod_c,'go',label ="s11_linear_Exp",alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,S21_mod_c,'bo',label="s21_linear_Exp",alpha=0.5,markevery=skip_point)

plt.plot(F_grafic,S11_mod_c_teorico,'c-', linewidth=2,label ="s11_Theoric")
plt.plot(F_grafic,S21_mod_c_teorico,'r-', linewidth=2,label="s21__Theoric")

plt.xlim(8.2,12.4)
plt.ylim(0,1.4)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("S11,S21 Linear(a.u)",fontsize = fonte)

#plt.legend(loc ='center right').get_frame().set_facecolor('0.95')
plt.legend(loc =1).get_frame().set_facecolor('0.95')
#plt.title("LINEAR MAG")
plt.savefig(u'Grafico_1.jpg')
plt.show()
#--------------------------------------------------------------


#-----------------------------VETORES-2---------------------
s11_ph =[] #EXP Fase CORRIGIDA
s21_ph =[] #EXP Fase CORRIGIDA

s11_ph_t =[] #TEO Fase CORRIGIDA
s21_ph_t =[] #TEO Fase CORRIGIDA


s11_db =[] #S11 EXP em dB CORRIGIDO
s21_db =[] #S21 EXP em dB CORRIGIDO

s11_db_t =[] #S11 TEO em dB CORRIGIDO
s21_db_t=[] #S21 TEO em dB CORRIGIDO

s11_db_t =[] #S11 TEO em dB CORRIGIDO
s21_db_t =[] #S21 TEO em dB CORRIGIDO

sum = [] # somatorio -> sum = |s11|**2 + |s21|**2
A =[] #absorbance
R = [] #reflectance
TRANS = [] #Transmtance


Z_a0 =[] #impedancia analitica vacuo
Z_ma = [] #impedancia analitica do material
Z_m = [] #impedancia calculada do material
Z_nrw =[] #impedancia NRW

T =[] #coeficiente de transmissao dos Par-S
T_a =[] #coef de Transmissao analitico

Cvetor =[] #coeficiente de reflexao dos Par-S
Cvetor_a = [] #coeficiente de reflexao analitico



er_r = [] #permissividade real
er_i = [] #'''''''''''''' imag
ur_r = [] #permeabilidade real
ur_i = [] #'''''''''''''' imag

er_abs=[] #permissividade modulo
ur_abs=[] #permeabilidade modulo

# ANALITICO------------------------
er_ra = [] #permissividade real
er_ia = [] #'''''''''''''' imag
ur_ra = [] #permeabilidade real
ur_ia = [] #'''''''''''''' imag

er_absa=[] #permissividade modulo
ur_absa=[] #permeabilidade modulo
#-----------------------------------


#-------- CURTO TEORICO-----------------------------
Zin_a =[] #Zin Teorico com CURTO

Cvetor_curto_a =[] #Coeficiente de Reflexao com CURTO TEORICO


z_v=[]

db_v =[]
	
s11_v =[]
	
refletividade_v=[]



#-------- CURTO EXPERIMENTAL S11 e S21-----------------------------
Zin =[] #Zin EXPERIMENTAL com CURTO

Cvetor_curto =[] #Coeficiente de Reflexao com CURTO EXPERIMENTAL

#------------------------------------------------------------


#----------Indice de Refracao----------
N =[]#Calculado
Na=[]#analitico


for n in range(0,len(F)):

	
	#------------------- dB EXP------------------------
	#Transformar S11  S21 para dB
	s11_db_calc = 20*np.log10(abs(s11c[n]))
	s21_db_calc = 20*np.log10(abs(s21c[n]))
	
	#add no vetor DB
	s11_db.append(s11_db_calc)
	s21_db.append(s21_db_calc)
	#-------------------------------------------------
	
	
	#------------------- dB TEO------------------------
	#Transformar S11  S21 para dB
	s11_db_calc = 20*np.log10(abs(s11c_teorico[n]))
	s21_db_calc = 20*np.log10(abs(s21c_teorico[n]))
	
	#add no vetor DB
	s11_db_t.append(s11_db_calc)
	s21_db_t.append(s21_db_calc)
	#-------------------------------------------------
	
	
	
	
	
	#----------------FASE EXP-------------------------
	#Calcular fase em radianos (conta basica de vetor)
	
	#Essa Funcao e usada em numeros reais imaginarios continuos.... (DICA BARROSO)
	s11_ph_calc = np.arctan2(s11c[n].imag,s11c[n].real) # Para numeros complexos usar a sintaxe np.tan2(imag,real)
	s21_ph_calc = np.arctan2(s21c[n].imag,s21c[n].real) # Para numeros complexos usar a sintaxe np.tan2(imag,real)
	
	# Essa funcao e usada para numeros REAIS (ISOLADAS) 
	# s11_ph_calc = np.arctan(s11c[n].imag/s11c[n].real) 
	#s21_ph_calc = np.arctan(s21c[n].imag/s21c[n].real)
	
	#Converter rad para graus
	s11_ph_calc_grau = 360.0*s11_ph_calc/(2.0*np.pi) 
	s21_ph_calc_grau = 360.0*s21_ph_calc/(2.0*np.pi) 
	
	#add no vetor da phase
	s11_ph.append(s11_ph_calc_grau)
	s21_ph.append(s21_ph_calc_grau)
	#-----------------------------------------
	
	'''
	#NAO BATE...
	#----------------FASE TEO-------------------------
	#Calcular fase em radianos (conta basica de vetor)
	
	#Essa Funcao e usada em numeros reais imaginarios continuos.... (DICA BARROSO)
	s11_ph_calc_t = np.arctan2(s11c_teorico[n].imag,s11c_teorico[n].real) # Para numeros complexos usar a sintaxe np.tan2(imag,real)
	s21_ph_calc_t = np.arctan2(s21c_teorico[n].imag,s21c_teorico[n].real) # Para numeros complexos usar a sintaxe np.tan2(imag,real)
	
	# Essa funcao e usada para numeros REAIS (ISOLADAS) 
	# s11_ph_calc = np.arctan(s11c[n].imag/s11c[n].real) 
	#s21_ph_calc = np.arctan(s21c[n].imag/s21c[n].real)
	
	#Converter rad para graus
	s11_ph_calc_grau_t = 360.0*s11_ph_calc_t/(2.0*np.pi) 
	s21_ph_calc_grau_t = 360.0*s21_ph_calc_t/(2.0*np.pi) 
	
	#add no vetor da phase
	s11_ph_t.append(s11_ph_calc_grau_t)
	s21_ph_t.append(s21_ph_calc_grau_t)
	#-----------------------------------------
	'''
	

	
	#------------- ABSORBANCE =1 - TRANSMITANCE - REFLECTANCE---
	reflectance = abs(s11c[n])**2
	transmitance = abs(s21c[n])**2
	absorvance = 1.0 - reflectance - transmitance
	
	#add vetor A,TRANS and R
	A.append(absorvance)
	TRANS.append(transmitance)
	R.append(reflectance)
	#-----------------------------------------------------------
	
	
	#--------------SUM-----------------------------------------
	#Isso mostra as perdas
	soma = reflectance + transmitance
	
	#add vetor sum
	sum.append(soma)
	#----------------------------------------------------------

	
	
	#----------------------NRW PAR-S---------------------------------
	#OBS: SE EU USAR O s11c[n] e s21c[n] daqui pra baixo da problema!!!!
	
	
	#frequencia
	f = F[n]
	
	
	#lambda zero = comprimento de onda no vacuo
	onda = c/(f) # [m]
	
	
	#Constante de propagacao da onda no espaco livre
	gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
	
	
	#Constante de propagacao da onda no material(analitico) 
	gamaX = (2j*np.pi/onda)*np.sqrt(e_a*u_a-(onda**2.0)/(onda_cut**2.0))
	
	
	#impedancia Analitica do Vacuo(za0)
	z_a0= (1j*u0*2*np.pi*f)/(gama0)
	
	Z_a0.append(z_a0)
	
	
	#impedancia analitica do material (zma)
	z_ma = ((1j*2*np.pi*f*u_a*u0)/(gamaX))/(z_a0) #z_a0 normliza
	
	Z_ma.append(z_ma.real)
	
	
	#impedancia do material calculada  com par-S (zm)  #IGUAL DO NRW
	z_m = np.sqrt(((1+s11c[n])**(2)-s21c[n]**2)/((1-s11c[n])**(2)-s21c[n]**(2)))
	
	Z_m.append(z_m.real)
	
	
	#coeficiente de transmissao Calculado 
	t = s21c[n]/(1-s11c[n]*((z_m-1)/(z_m+1)))
	
	T.append(abs(t))
	
	
	#Coeficiente de transmissao Analitico
	ta = np.exp(-gamaX*d)
	
	T_a.append(abs(ta))
	
	
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
	
	Cvetor.append(abs(C))
	
	#velocidade da luz no guia
	c_lab = f/onda_cut
	
	#Coeficiente de refelxao Analitico 
	#C_analitico = ((gama0)/(u0)-(gamaX)/(u_a))/((gama0)/(u0)+(gamaX)/(u_a))
	#C_analitico = (((c)/(c_lab))*np.sqrt((u_a)/(e_a))-1)/(((c)/(c_lab))*np.sqrt((u_a)/(e_a))+1)
	C_analitico = (z_ma-1)/(z_ma+1)
	
	
	Cvetor_a.append(abs(C_analitico))
	
	
	#constante P
	P2=-((1.0)/(2*np.pi*d)*np.log(1.0/t))**2
	P=1.0/np.sqrt(P2)
	
	
	#constante Lamb
	lamb = np.sqrt((1.0)/(onda)**(2)-(1.0)/(onda_cut)**(2))
	
	
	#impedancia NRW (z_nrw) #IGUAL AO Z CALCULADO COM PAR-S (z_m)
	z_nrw = (1+C)/(1-C)
	Z_nrw.append(z_nrw.real) #somente real
	
	
	#Permeabilidade NRW
	#ux = ux = z_nrw/(P*lamb)
	ux = z_m/(P*lamb) #poco melhor com z_m
	
	ur_r.append(ux.real)
	ur_i.append(ux.imag)
	ur_abs.append(abs(ux))
	
	
	#Permissividade NRW
	ex = ((onda)**(2)/ux)*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2)
	#ex = ((onda)**(2)/abs(ux))*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/t))**2) #abs(ux)
	
	#ex = ex.real - 1j*ex.imag
	
	
	er_r.append(ex.real)
	#er_i.append(ex.imag)
	er_i.append(-1*ex.imag)
	er_abs.append(abs(ex))
	#------------------------------------------------------
	
	#------------------NRW - Analitico----------------------
	
	#constante P (ANALITICO
	P2_a=-((1.0)/(2*np.pi*d)*np.log(1.0/ta))**2
	P_a=1.0/np.sqrt(P2_a)
	
	#Permeabilidade NRW sem par-S
	ux_a = z_ma/(P_a*lamb)
	
	ur_ra.append(ux_a.real)
	ur_ia.append(-1*ux_a.imag)
	ur_absa.append(abs(ux_a))
	
	#Permissividade NRW sem par-S
	ex_a = ((onda)**(2)/ux_a)*((1.0)/(onda_cut)**2-((1)/(2*np.pi*d)*np.log(1.0/ta))**2)
	er_ra.append(ex_a.real)
	er_ia.append(-1*ex_a.imag)
	er_absa.append(abs(ex_a))
	
	
	
	#----------Calculo do Coeficiente de Reflexao com Curto - TEORICO---------------------
	
	
	#---------Calcular Impedancia (Zin)---------------------------------------
	z = ((50)**(1.0/2.0))*np.tanh(1j*(2*np.pi*d/onda)*((ux*ex)**(1.0/2.0))) #acho que ta errado esse, mas bate experimental (art 118)
	z_v.append(z)
	#------------------------------------------------------------------------------------------
		
	#-------------Utilizar a impedancia para calcular dB (impedancia da linha 50 omg)------------------------
		
	#db= -20*np.log10(abs((z-1)/(z+1))) #dB #somente para voltagem
	db = 10*np.log10(abs((z-50)/(z+50))) #dB para potencia
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
	
	
	
	#----------Calculo do Coeficiente de Reflexao com Curto - EXPERIMENTAL (S11 e S21)---------------------
	#Precisa calcular o NRW e obter o e and mu experimental
	# Zin teorico com curto
	zin = (1j*(ux/ex)**(1.0/2.0))*np.tan((2*np.pi*d/onda)*((ux*ex)**(1.0/2.0)))
	
	Zin.append(abs(zin))
	
	#Coeficiente de Reflexao com curto
	C_curto = (zin-1)/(zin+1)
		
	Cvetor_curto.append(abs(C_curto))
	
	
	
	
	#---------- Indice de Refracao calculado-------------
	inv_onda = ((1j)/(2*np.pi*d))*np.log(t)
	
	n_calc = inv_onda * onda
	
	
	
	N.append(n_calc.real)
	
	#-------------Indice de Refecao Analitico
	
	#na = np.sqrt(ex*ux) #Para vacuo
	na = np.sqrt(e_a*u_a-((onda)/(onda_cut))**2) #guiado
	
	
	Na.append(na.real)
	
	
	
#----------------------PLOTES----------------------------	



#Plot Modulo em DB
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,s11_db,'ob',label ='s11_experimental',alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,s21_db,"or",label = 's21_experimental',alpha=0.5,markevery=skip_point)

plt.plot(F_grafic,s11_db_t,'c-', linewidth=2,label ="s11_Theoric")
plt.plot(F_grafic,s21_db_t,'r-', linewidth=2,label="s21_Theoric")

plt.ylim(-30,2)
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("S11,S21 (dB)",fontsize = fonte)
#plt.title("S11 e S21 em dB")
#plt.legend().get_frame().set_facecolor('0.95')
#"upper left"
plt.legend(loc ='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_2.jpg')
plt.show()
	


#Plot Phase em Grau
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,s11_ph,'g-',label ='s11_phase')
plt.plot(F_grafic,s21_ph,'b-',label='s21_phase')

#plt.plot(F_grafic,s11_ph_t,'c-', linewidth=2,label ="s11_Phase_Teorico")
#plt.plot(F_grafic,s21_ph_t,'r-', linewidth=2,label="s21_Phase_Teorico")

plt.xlim(8.2,12.4)
plt.ylim(-200,200)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("Fase(Graus)",fontsize = fonte)
plt.legend(loc='best').get_frame().set_facecolor('0.95')
#plt.title("FASE")
plt.savefig(u'Grafico_3.jpg')
plt.show()




#Plot aborbance, refletance and transmitance
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,A,'-b',label ='Absorbance')
plt.plot(F_grafic,TRANS,'-r',label ='Transmitance')
plt.plot(F_grafic,R,'-g',label ='Reflectance')
plt.ylim(-0.1,1.2)
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("A,R,T(a.u)",fontsize = fonte)
#plt.title("Absorbance, Reflectance and Transmitance")
plt.legend(loc='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_4.jpg')
plt.show()		

'''
#Plot Sum
plt.plot(F_grafic,sum,'-b',label ='SOMA DE S11 e S21')
plt.ylim(0,1.2)
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.ylabel("(a.u)")
plt.legend().get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_5.jpg')
plt.show()
'''

#Plot Impedancia
fig=plt.figure(num=1,figsize=(x,y))

#plt.plot(F_grafic,Z_a0,'-b',label ='z_vacuo')
plt.plot(F_grafic,Z_m,'ro',label ='Z_Calc',alpha=0.5,markevery=skip_point) #Igual (MAS E MELHOR)
plt.plot(F_grafic,Z_ma,'-g',label ='Z_Teo',linewidth=2)

#plt.plot(F_grafic,Z_nrw,'-y',label ='z_nrw') #igual
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("Z(a.u)",fontsize = fonte)
#plt.title("Impedance")
plt.legend(loc='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_6.jpg')
plt.show()



#Plot Indice de Refecao
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,N,'ro',label ='$\eta$_Calc',alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,Na,'-g',label ='$\eta$_Teo',linewidth=2) 
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("$\eta$ (a.u)",fontsize = fonte)
#plt.title("Refraction Indice")
plt.legend(loc='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_7.jpg')
plt.show()




#Plot Coeficiente de Transmissao
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,T,'ro',label ='T_Calc',alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,T_a,'-g',label ='T_Teo',linewidth=2)
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("T(a.u)",fontsize = fonte)
#plt.title("Transmission Coeficiente")
plt.legend().get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_8.jpg')
plt.show()


#Plot Coeficiente de Reflexao
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,Cvetor,'ro',label ='$\Gamma$_Calc',alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,Cvetor_a,'-g',label ='$\Gamma$_Teo',linewidth=2)
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel("$\Gamma$(a.u)",fontsize = fonte)
#plt.title("Refletion Coeficiente")
plt.legend(loc='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_9.jpg')
plt.show()


#plot e
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,er_r,'o',label="$\epsilon_{r}$'_Calc",alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,er_i,'o',label='$\epsilon_{r}$"_Calc',alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,er_ra,'-',label="$\epsilon_{r}$'_Teo",linewidth=2)
plt.plot(F_grafic,er_ia,'-',label='$\epsilon_{r}$"_Teo',linewidth=2)
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel('$\epsilon_{r}$"'+",$\epsilon_{r}$' (a.u)",fontsize = fonte)
#plt.title("Permissivity")
plt.legend(loc='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_10.jpg')
plt.show()

#plot u
fig=plt.figure(num=1,figsize=(x,y))

plt.plot(F_grafic,ur_r,'o',label = "$\mu_{r}$'_Calc",alpha=0.5,markevery=skip_point )
plt.plot(F_grafic,ur_i,'o',label ='$\mu_{r}$"_Calc',alpha=0.5,markevery=skip_point)
plt.plot(F_grafic,ur_ra,'-',label = "$\mu_{r}$'_Teo",linewidth=2)
plt.plot(F_grafic,ur_ia,'-',label ='$\mu_{r}$"_Teo',linewidth=2)
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.ylabel('$\mu_{r}$"'+",$\mu_{r}$' (a.u)",fontsize = fonte)
#plt.title("Permeability")
plt.legend(loc='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_11.jpg')
plt.show()

'''
#plot e and u modulo
plt.plot(F_grafic,ur_abs,'-',label="ur_abs")
plt.plot(F_grafic,er_abs,'-',label='er_abs')
plt.plot(F_grafic,ur_absa,'-',label="ur_abs_TEORICO")
plt.plot(F_grafic,er_absa,'-',label='er_abs_TEORICO')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")

plt.legend().get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_12.jpg')
plt.show()

#plot Zin Teorico Curto
plt.plot(F_grafic,Zin_a,'-',label="Zin_curto_TEORICO")
plt.plot(F_grafic,Zin,'-',label="Zin_curto_EXPERIMENTAL")
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_13.jpg')
plt.show()
'''

#plot Coeficiente de Reflexao Teorico Curto
fig=plt.figure(num=1,figsize=(x,y))

#plt.plot(F_grafic,Cvetor_curto_a,'-',label="Reflexao_curto_TEORICO")
plt.plot(F_grafic,refletividade_v,'-b',label = "Reflexao_Curto_Zin")
#plt.plot(F_grafic,Cvetor_c,'-',label="Reflexao_curto_EXPERIMENTAL S11")
plt.xlim(8.2,12.4)
plt.ylim(0,100)
plt.ylabel("Refletividade(a.u)",fontsize = fonte)
#plt.title("Refletivity")
plt.xlabel("Freq(GHz)",fontsize = fonte)
plt.legend(loc='best').get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_14.jpg')
plt.show()

#--------------------------------------------------------

'''
#---------------------Gravar Dados TXT---------------------

arqnew= open("./_Dados.txt",'w')

arqnew.write("Fre(Hz)  	er	ei	ur	ui\n")

for n in range(0,len(F)):

	escrever = "%.4f	%.4f	%.4f	%.4f	%.4f\n"%(F[n],er_r[n],er_i[n],ur_r[n],ur_i[n])
	#escrever = "%.4f\n"%(F[n])
	
	arqnew.write(escrever)



arqnew.close()
'''
