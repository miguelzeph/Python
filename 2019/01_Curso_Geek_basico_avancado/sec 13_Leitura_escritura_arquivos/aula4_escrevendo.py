
#Se abrir para ler, não pode escrever...  open('novo.txt','r')
#Se abrir para escrever, não pode ler...  open('novo.txt','w')

# modo = 'w'
arquivo = open('novo.txt','w')
arquivo.close()

#dica:

#help(open) #leia, em caso de dúvida dos parâmetros...


#Podemos usar operadores

arquivo = open('novo.txt','w')
arquivo.write("Gol"*10)
arquivo.close()

