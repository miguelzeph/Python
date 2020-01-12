
#Calcula Impedancia
#Calcula Indice de Refracao
#Calcula Coeficiente de Transmissao
#Calcula Coeficiente de Reflexao
#PLOTA Permissividade
#PLOTA Permeabilidade
#Calcula Zin (curto)
#Calcula coeficiente de Reflexao (curto)

from __future__ import division
import os 
import numpy as np
import matplotlib.pyplot as plt



#---------------LER ARQUIVO TXT NA PASTA-------------
TXT =[]

for arquivo in os.listdir('.'):
	if (arquivo[len(arquivo)-4:] == '.txt' and arquivo[0] == "_" ):
		TXT.append(arquivo)
		
print '\nArquivo: ',TXT[0]	
	
arq = open(TXT[0],'r')
ler = arq.readlines()
arq.close()
#----------------------------------------------------


#-------------Ajuste da Referencia de L1 e L2---------
#Offset = 9.76mm
#L1, L2 e L = d....importante ser bem denifido

d = 1.5e-3 #[m] #Espessura da amostra (Livro chama de L)



a =22.86e-3 #[m] #Dimensao maior do guia de onda (Banda-X)
#-------------------------------------------------------



#--------------Permissividade e Permeabilidade (Chute)------

#e_a = 2.04 - 0.0j #Analitico teflon
#u_a = 1.0 - 0j    #Analitico teflon
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

er=[] #real
ei=[] #imag
ur=[] #real
ui=[] #imag

e=[] # real + j imag
u=[] # real + j imag



#-----------------------------------------------------


Z_a0 =[] #impedancia analitica vacuo
Z_ma = [] #impedancia analitica do material
Z_m = [] #impedancia calculada do material
Z_nrw =[] #impedancia NRW

T =[] #coeficiente de transmissao dos Par-S
T_a =[] #coef de Transmissao analitico

Cvetor =[] #coeficiente de reflexao dos Par-S
Cvetor_a = [] #coeficiente de reflexao analitico


#-------- CURTO TEORICO-----------------------------
Zin_a =[] #Zin Teorico com CURTO

Cvetor_curto_a =[] #Coeficiente de Reflexao com CURTO TEORICO


#-------- CURTO EXPERIMENTAL S11 e S21-----------------------------
Zin =[] #Zin EXPERIMENTAL com CURTO

Cvetor_curto =[] #Coeficiente de Reflexao com CURTO EXPERIMENTAL


#------------------------------------------------------------


#----------Indice de Refracao----------
N =[]#Calculado
Na=[]#analitico




#---------------ORGANIZAR PARAMETROS-S em VETOR---------

ler1_col=1 #S11r
ler2_col=2 #S11i
ler3_col=3 #S21r
ler4_col=4 #S21i


for i in range(0,len(ler)):
	
	
	dados = ler[i].split('	')
	
	#Ler frequencia
	f_colocar = float(dados[0]) #Hz
	
	F.append(f_colocar)
	
	
	#---------Organizar os PAR-S---------------------
	er.append(float(dados[ler1_col]))#real
	ei.append(float(dados[ler2_col]))#imag
	ur.append(float(dados[ler3_col]))#real
	ui.append(float(dados[ler4_col]))#imag
	
	e_colocar =er[i]-1j*ei[i] # real + j imag
	u_colocar =ur[i]-1j*ui[i] # real + j imag
	
	e.append(e_colocar) #add vetor s11
	u.append(u_colocar) #add vetor s21
	#--------------------------------------------------




for n in range(0,len(F)):

	
	#frequencia
	f = F[n]
	F_grafic.append(f/1e9)
	
	
	#lambda zero = comprimento de onda no vacuo
	onda = c/(f) # [m]
	
	
	#Constante de propagacao da onda no espaco livre
	gama0 = (2j*np.pi)*np.sqrt((1.0)/(onda**(2.0))-(1.0)/(onda_cut**(2.0)))
	
	
	#Constante de propagacao da onda no material(analitico) 
	gamaX = (2j*np.pi/onda)*np.sqrt(e[n]*u[n]-(onda**2.0)/(onda_cut**2.0))
	
	
	#impedancia Analitica do Vacuo(za0)
	z_a0= (1j*u0*2*np.pi*f)/(gama0)
	
	Z_a0.append(z_a0)
	
	
	#impedancia analitica do material (zma)
	z_ma = ((1j*2*np.pi*f*u[n]*u0)/(gamaX))/(z_a0) #z_a0 normliza
	
	Z_ma.append(z_ma.real)
	
	
	
	
	#Coeficiente de transmissao Analitico
	ta = np.exp(-gamaX*d)
	
	T_a.append(abs(ta))
	
	
	#velocidade da luz no guia
	c_lab = f/onda_cut
	
	#Coeficiente de refelxao Analitico 
	#C_analitico = ((gama0)/(u0)-(gamaX)/(u_a))/((gama0)/(u0)+(gamaX)/(u_a))
	#C_analitico = (((c)/(c_lab))*np.sqrt((u_a)/(e_a))-1)/(((c)/(c_lab))*np.sqrt((u_a)/(e_a))+1)
	C_analitico = (z_ma-1)/(z_ma+1)
	
	
	Cvetor_a.append(abs(C_analitico))
	
	
	
	
	#----------Calculo do Coeficiente de Reflexao com Curto - TEORICO---------------------
	
	np.seterr(divide='ignore', invalid='ignore')
	# Zin teorico com curto
	zin_a = (1j*(u[n]/e[n])**(1.0/2.0))*np.tan((2*np.pi*d/onda)*((u[n]*e[n])**(1.0/2.0)))
	
	Zin_a.append(abs(zin_a))
	
	#Coeficiente de Reflexao com curto
	C_curto_a = (zin_a-1)/(zin_a+1)
	
		
	Cvetor_curto_a.append(abs(C_curto_a))
	
	
	
	#-------------Indice de Refecao Analitico
	
	#na = np.sqrt(ex*ux) #Para vacuo
	na = np.sqrt(e[n]*u[n]-((onda)/(onda_cut))**2) #guiado
	
	Na.append(na.real)
	
	#---------- Indice de Refracao calculado-------------
	#inv_onda = ((1j)/(2*np.pi*d))*np.log(ta)
	
	#n_calc = inv_onda * onda
	
	#N.append(n_calc.real)
	
	
	
#----------------------PLOTES----------------------------	


#Plot Impedancia
#plt.plot(F_grafic,Z_a0,'-b',label ='z_vacuo')
plt.plot(F_grafic,Z_ma,'-g',label ='z_material_Teorico')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
#plt.savefig(u'Grafico_6.jpg')
plt.show()



#Plot Indice de Refecao
plt.plot(F_grafic,Na,'-r',label ='n_analitico') 
#plt.plot(F_grafic,N,'b*',label ='n_calculado')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
#plt.savefig(u'Grafico_7.jpg')
plt.show()




#Plot Coeficiente de Transmissao
plt.plot(F_grafic,T_a,'-r',label ='T_analitico')
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
#plt.savefig(u'Grafico_8.jpg')
plt.show()


#Plot Coeficiente de Reflexao
plt.plot(F_grafic,Cvetor_a,'-r',label ='Coef_Reflex_analitico')
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
#plt.savefig(u'Grafico_9.jpg')
plt.show()


#plot e 
plt.plot(F_grafic,er,'-',label="er'")
plt.plot(F_grafic,ei,'-',label='ei"')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
#plt.savefig(u'Grafico_10.jpg')
plt.show()


#plot u 
plt.plot(F_grafic,ur,'-',label="ur'")
plt.plot(F_grafic,ui,'-',label='ui"')
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
#plt.savefig(u'Grafico_10.jpg')
plt.show()





#plot Zin Teorico Curto
plt.plot(F_grafic,Zin_a,'-',label="Zin_curto_TEORICO")
plt.xlim(8.2,12.4)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
plt.savefig(u'Grafico_13.jpg')
plt.show()


#plot Coeficiente de Reflexao Teorico Curto
plt.plot(F_grafic,Cvetor_curto_a,'-',label="Reflexao_curto_TEORICO")
plt.xlim(8.2,12.4)
plt.ylim(0,1.2)
plt.xlabel("Freq(GHz)")
plt.legend().get_frame().set_facecolor('0.95')
#plt.savefig(u'Grafico_14.jpg')
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