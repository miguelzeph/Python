import os

#-------- ENCONTRAR ARQUIVO NO DIRETORIO-------

lista = os.listdir('.')
txts = []

for i in range(0,len(lista)):
	if (lista[i].find('.txt') == -1):#find quando n tem ele retorna -1
		continue
	else:
		txts.append(lista[i])
#print txts
#---------------------------------------------


# ---------LER LINHAS-------------------------
for n in range(0,len(txts)):
	
	#retirar depois....------
	if txts[n] == 'fatura.txt':
	#---------------------------
		arq_entrada=open('./'+txts[n],'r')
		arq_dados=arq_entrada.readlines()
		arq_entrada.close()
		
		#print arq_dados[1]
		
		palavra=[]
		
		numero_palavras = []
		
		for i in range(0,len(arq_dados)):
			
			b=arq_dados[i].split('	')#vetor, contendo as palavras
			
			#print 'linha numero: ',(i+1),'\n'
			#print b,'antes'
			
			#------Remover Espaco e \t ----------------------
			#for j in range(0,len(b)):
			#	if b[j] == '':
			#		print b[j]
			#		raw_input('ok')
				
			for j in range(0,len(b)):	
				
				try:
			
					while True:
					
						if (b[j] == ''):
							b.remove('')
							#raw_input("removeu '' ")
							#print b
						
						#-------- NAO REMOVER -------
						#if (b[j] == '\n'):
						#	b.remove('\n')
							#raw_input("removeu '' ")
							#print b
						#----------------------------
						
						
						else:
						
							#while True:
							
							#	if (b[j] == '\n'):
							#		b.remove('\n')
									#raw_input("removeu 'n' ")
									#print b
						
							#	else:
							#		break
							
							break
						
				except IndexError:
				
					break
			#-----remover \n do final da frase---
			
			#for j in range(0,len(b)):
			
			#	print b[j]
				
			#	for k in range(0,len(b[j])):
				
			#		try:
			#			print b[j][k]+b[j][k+1]
			#			if (b[j][k]+b[j][k+1]) == '\n':
							
			#				print b[j]
			#		except IndexError:
					
			#			continue
			#=----------------------------------
			
			#print b,'depois'
			
			palavra.extend(b)
			
			numero_palavras.append(len(b))
			
			
			
			#raw_input("pause\n")

final=open('./arquivo_fumachi.txt','w')


telefone = []
posicao_VEJA = []

for w in range(0,len(palavra)):

	if palavra[w] == 'VEJA':
		
		valor_inicial = w#numero do vetor, onde esta o VEJA
		posicao_VEJA.append(w)
		#print w#posicao que o VEJA esta no meu vetor
		print palavra[w+6] #numeros do telefone (final da linha do veja)
		telefone.append(palavra[w+6])

			
#---------------------------------------------------------------------------------
# AQUI ESTA A LOGICA DO PROGRAMINHA QUE SIMULEI NA PASTA... APAGAR TUDO ENTRE "VEJA"(5) ATE SUBTOTAL (10)
		
for t in range(0,len(palavra)):	
	

	k=0
	while True:
		try :
		
			if palavra[k] == 'Data':
				
				q = k
				
				while (palavra[q] != 'Subtotal'):
				
					palavra[q] = None
					
					q = q+1
				
				k = q
				
				
			
			#raw_input()
			k=k+1
			
		except IndexError:
			break
#-----------------------------------FINAL-----------------------------------------------------------	


for k in range(posicao_VEJA[0],len(palavra)):
	
	#if k == 0:
	#	escrever = palavra[k]+' '
	#	final.write(escrever)
		
	#else:
	#print palavra[k]
	#raw_input()
	
	
	if palavra[k] == None:
		continue
	else:
		# Fiz isso para arrumar o Espacamento...-----------
		if palavra[k] == '\n':
			escrever = palavra[k]
			final.write(escrever)
			
		else:
			escrever = palavra[k]+' '
			final.write(escrever)
		#---------------------------------------------------
final.close()
#print telefone
#print numero_palavras