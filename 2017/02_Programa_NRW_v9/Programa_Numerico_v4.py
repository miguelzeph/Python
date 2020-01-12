#Esse programa:
#Chuta um valor para permissividade
#Fixa permebilidade
#Calcula um Par-S novo
#Compara estatisticamente com o Experimental
#Pega o valor da permissividade chutada que obteve o melhor ajusta e usa como sendo verdadeiro

#Versao 1 -> Faz as media para todas frequencias e so usa valor real da permissividade
#Versao 2 -> Foi introduzido a parte imaginaria tambem
#Versao 3 -> Cada frequencia ira receber uma variacao de permissividade... e cada frequencia tera seu melhor e' e e"...
#Logo a permissividade sera uma funcao
#Versao 4 -> Plota melhor S11 e S21 Teorico em funcao do e' e e" encontrado (FAZ MEDIA DOS DOIS MELHORES)

from __future__ import division
import os 
import numpy as np
import matplotlib.pyplot as plt



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

d = 1.5e-3 #[m] #Espessura da amostra (Livro chama de L)

L1 = 0e-3 #[m] #Plano de referencia porta 1
L2 = 9.76e-3 - d #[m]   #Plano de referencia porta 2

a =22.86e-3 #[m] #Dimensao maior do guia de onda (Banda-X)
#-------------------------------------------------------



#--------------Permissividade e Permeabilidade (Chute)------

#e_a = 2.04 - 0.0j #Analitico teflon
u_a = 1.0 - 0j    #Analitico teflon
#------------------------------------------------------------



#-------------------- CONSTANTES-----------------------------
c =2.998e8 #[m/s] #velocidade da Luz no vacuo

u0=4*np.pi*1e-7 # permeabilidade do vacuo

freq_corte = 6.56e9 # [Hz]

onda_cut= c/freq_corte #[m] #lambda de corte
#-------------------------------------------------------------








#---------------ORGANIZAR PARAMETROS-S em VETOR---------

ler1_col=1 #S11r
ler2_col=2 #S11i
ler3_col=3 #S21r
ler4_col=4 #S21i


#-------------- Modulo de S11 e S21 (Prova real) ---------------



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



s11c_teo=[] # real + j imag (Corrigido)
s21c_teo=[] # real + j imag (Corrigido)
	
	
	
s11c_mod=[] # real + j imag (Corrigido)
s21c_mod=[] # real + j imag (Corrigido)



s11c_teo_mod=[] # real + j imag (Corrigido)
s21c_teo_mod=[] # real + j imag (Corrigido)
	




	
X_por_f_er = [] #Melhor X por frequencia para permissividade real
X_por_f_ei = [] #Melhor X por frequencia para permissividade imaginaria



e1_x = np.arange(20,25,0.25)
e2_x = np.arange(-1,1,0.5)

e_x=[]

for i in range(0,len(e1_x)):
	
	for j in range(0,len(e2_x)):
		
		e_x.append(e1_x[i]+1j*e2_x[j])
		
		
#LER CADA FREQUENCIA
for i in range(0,len(ler)):
	
	
	X_s11= [] #chi_quadrado S11
	X_s21= [] #chi_quadrado S21
		
	dados = ler[i].split('	')
	
	#Ler frequencia
	f_colocar = float(dados[0]) #Hz
		
	F.append(f_colocar)
	F_grafic.append(f_colocar/1e9) #Ajusta unidade
		
		
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
		
	#Ajustar S11 e S21 (EXPERIMENTAL)
	s11c_colocar = R1*R1*s11_colocar
	s21c_colocar = R2*R1*s21_colocar
		
	
	#Add S11 e S21 Corrigido (EXPERIMENTAL)
	s11c.append(s11c_colocar) #s11 novo
	s21c.append(s21c_colocar) #s21 novo
	#--------------------------------------------------------------
		
	s11c_mod.append(abs(s11c[i]))
	s21c_mod.append(abs(s21c[i]))
	
	
	#VARIAR PERMISSIVIDADE
	for w in range(0,len(e_x)):
	
		e_a = e_x[w]
		
		
		#chi = (exp-teo)**2/exp
		
		
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
			
		#Calcular S11 e S21 Teorico e Corrigir (TEORICO)
		s11c_colocar_teorico = R1*R1*((Ca*(1-ta**2))/(1-(Ca**2)*(ta**2)))
		s21c_colocar_teorico = R2*R1*((ta*(1-Ca**2))/(1-(Ca**2)*(ta**2)))
			
		
		
		
		
		#Chi Quadrado S11 
		chi_quad_s11 = (abs(s11c_colocar_teorico)- abs(s11c[i]))**(2.0)/abs(s11c[i])
		#Chi Quadrado S21
		chi_quad_s21 = (abs(s21c_colocar_teorico)- abs(s21c[i]))**(2.0)/abs(s21c[i])
		
		X_s11.append(chi_quad_s11/len(ler))
		X_s21.append(chi_quad_s21/len(ler))
		
		#print chi_quad_s11,e_x[w]
		
		
	
	
	for n in range(0,len(X_s11)):
		
		
			
		x_s11_normalizado = X_s11[n]/min(X_s11)
		x_s21_normalizado = X_s21[n]/min(X_s21)
		
		#print x_s11_normalizado
		#raw_input()
		
		
		if (x_s11_normalizado == 1.0):
			
			X_por_f_er_s11 = e_x[n].real #Grava o melhor er pelo S11
			X_por_f_ei_s11 = e_x[n].imag #Grava o melhor ei pelo S11
			
			#X_por_f_er.append(e_x[n].real)
			#X_por_f_ei.append(e_x[n].imag)
			
			
			e_a = e_x[n]
			
			
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
				
			#Calcular S11 e S21 Teorico e Corrigir (TEORICO)
			s11c_colocar_teorico = R1*R1*((Ca*(1-ta**2))/(1-(Ca**2)*(ta**2)))
			#s21c_colocar_teorico = R2*R1*((ta*(1-Ca**2))/(1-(Ca**2)*(ta**2)))
				
				
			s11c_teo_mod.append(abs(s11c_colocar_teorico))
			#s21c_teo_mod.append(abs(s21c_colocar_teorico))
			
			
			
		if (x_s21_normalizado == 1.0):
			
			#X_por_f_er.append(e_x[n].real)
			#X_por_f_ei.append(e_x[n].imag)
			
			X_por_f_er_s21 = e_x[n].real #Grava o melhor er pelo S11
			X_por_f_ei_s21 = e_x[n].imag #Grava o melhor er pelo S21
			
			e_a = e_x[n]
			
			
			
			
			
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
				
			#Calcular S11 e S21 Teorico e Corrigir (TEORICO)
			s11c_colocar_teorico = R1*R1*((Ca*(1-ta**2))/(1-(Ca**2)*(ta**2)))
			s21c_colocar_teorico = R2*R1*((ta*(1-Ca**2))/(1-(Ca**2)*(ta**2)))
				
				
			
			#s11c_teo_mod.append(abs(s11c_colocar_teorico))
			s21c_teo_mod.append(abs(s21c_colocar_teorico))
			
	#Faza Media dos dois valores de S11 e S21
	X_er = (X_por_f_er_s11+X_por_f_er_s21)/2
	X_ei = (X_por_f_ei_s11+X_por_f_ei_s21)/2
		
	X_por_f_er.append(X_er)
	X_por_f_ei.append(X_ei)
		
		
			
			
print len(s11c_teo_mod),len(s21c_teo_mod)		
		
		
plt.plot(F_grafic,X_por_f_er,'g-',label ="er",alpha=1)
plt.plot(F_grafic,X_por_f_ei,'b-',label="ei",alpha=1)
plt.xlim(8.2,12.4)
plt.ylim(-0.25,2.5)
plt.xlabel("Freq(GHz)")
plt.ylabel("S11,S21(a.u)")
plt.legend().get_frame().set_facecolor('0.95')
plt.show()



#-------PLOTE LINEAR MAG: TEORICO X EXP (AMBOS AJUSTADOS)---------
plt.plot(F_grafic,s11c_mod,'g.',label ="s11_linear_Exp",alpha=0.5)
plt.plot(F_grafic,s21c_mod,'b.',label="s21_linear_Exp",alpha=0.5)

plt.plot(F_grafic,s11c_teo_mod,'g-',label ="s11_linear_teo",alpha=1)
plt.plot(F_grafic,s21c_teo_mod,'b-',label="s21_linear_teo",alpha=1)

plt.xlim(8.2,12.4)
plt.ylim(0,1.4)
plt.xlabel("Freq(GHz)")
plt.ylabel("S11,S21(a.u)")
plt.legend().get_frame().set_facecolor('0.95')
plt.title("LINEAR MAG")
plt.savefig(u'Grafico_1.jpg')
plt.show()
#--------------------------------------------------------------

#--------------------------------------------------------------	
	

#Normalizar CHI	-------------------

	


'''
#-------PLOTE LINEAR MAG: TEORICO X EXP (AMBOS AJUSTADOS)---------
plt.plot(F_grafic,S11_mod_c,'g.',label ="s11_linear_Exp",alpha=0.5)
plt.plot(F_grafic,S21_mod_c,'b.',label="s21_linear_Exp",alpha=0.5)

plt.plot(F_grafic,S11_mod_c_teo,'c-', linewidth=2,label ="s11_linear_Teorico")
plt.plot(F_grafic,S21_mod_c_teo,'r-', linewidth=2,label="s21_linear_Teorico")

plt.xlim(8.2,12.4)
plt.ylim(0,1.4)
plt.xlabel("Freq(GHz)")
plt.ylabel("S11,S21(a.u)")
plt.legend().get_frame().set_facecolor('0.95')
plt.title("LINEAR MAG")
plt.savefig(u'Grafico_1.jpg')
plt.show()
#--------------------------------------------------------------
'''


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