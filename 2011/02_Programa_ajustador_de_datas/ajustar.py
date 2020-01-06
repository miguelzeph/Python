# -*- coding: utf-8 -*-

entrada=open('./saida/gama.txt','r')
dados=entrada.readlines()
entrada.close()

saida=open('./saida.txt','w')

ab=[31,29,31,30,31,30,31,31,30,31,30,31]
an=[31,28,31,30,31,30,31,31,30,31,30,31]

c=0
for a in range(10,11):
	for m in range(12,13):
		if  ((a % 4) == 0):
			dmax=ab[m-1]+1
		else:
			dmax=an[m-1]+1
		
		for d in range(20,24):
			for h in range(0,24):
				for mi in range(0,60):
					#if (c >= len(dados)):
					#	break
					
					f_a=int(dados[c][0:2])
					f_m=int(dados[c][2:4])
					f_d=int(dados[c][4:6])
					f_h=int(dados[c][6:8])
					f_mi=int(dados[c][8:10])
					
					if ((a == f_a) and (m == f_m) and (d == f_d) and (h == f_h) and (mi == f_mi)):
						saida.write(dados[c])
						c=c+1
						print 'ok'
					else:
						linha='%02d%02d%02d%02d%02d%02d         ---\n' %(a,m,d,h,mi,0)
						saida.write(linha)
saida.close()
