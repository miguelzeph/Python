import os

#-------- ENCONTRAR ARQUIVO TXT NO DIRETORIO-------

lista = os.listdir('.')
txts = []

for i in range(0,len(lista)):
	if (lista[i].find('.txt') == -1):#find quando n tem ele retorna -1
		continue
	else:
		txts.append(lista[i])
	#-------------------------------------------------

	#----------------- LER LINHAS E GRAVAR -----------

	
	
for n in range(0,len(txts)):

        final=open('./'+txts[n][:-4]+'_saida'+'.DAT','w')
		
		
	arq_entrada=open('./'+txts[n],'r')
	arq_dados=arq_entrada.readlines()
	arq_entrada.close()
			
	for i in range(4,len(arq_dados)):
				
		b=arq_dados[i].split('	')
		try:
			escrever=  '%s %s\n'%(str(b[1]),str(b[2]))
			#print escrever
			final.write(escrever)
		except IndexError:
			continue
final.close()
