import os

os.chdir('./entrada')

arquivo=open('./horas.txt','w')

arquivo.write('Horas Decimal\n')

for i in range(0,50):

	hh=int(10)
	MM=float(0.10*i)
	mm=float(0.05*i)
	HH= float(hh+MM+mm)
	arquivo.write("   "+str(HH)+"\n")
arquivo.close()