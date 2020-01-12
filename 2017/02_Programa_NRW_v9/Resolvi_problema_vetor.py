#Resolvi o problema do e and u com numeros diferentes..

#Solucao foi criar um vetor com dois vetores reservando os valores de cada um com relacao ao C

a = [1,3,3,4,1]

b = [1,2]

c = []

a_b = []

chi =0
for i in range(0,len(b)):
	for j in range(0,len(a)):
	
		chi= a[j]+b[i]
		c.append(chi)
		a_b.append([a[j],b[i]])


print c

for w in range(0,len(c)):
	
	c_min = c[w]/min(c)
	
	if c_min ==1.0:
		
		print w
		a_melhor = a_b[w][0]
		b_melhor = a_b[w][1]
		
		break
print a_melhor,b_melhor
	
	
	