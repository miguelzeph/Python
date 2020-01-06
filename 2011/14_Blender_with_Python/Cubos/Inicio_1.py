import Blender

nome=["Cube","Cube.001","Cube.002"]

#Todos Objetos da cena
all=Blender.Object.Get()

print "todos Objetos da Cena",all,"\n"

#Variaveis minhas ...
obj0=Blender.Object.Get(nome[0])
obj1=Blender.Object.Get(nome[1])
obj2=Blender.Object.Get(nome[2])

#posicao 

pos0=obj0.loc
pos1=obj1.loc
pos2=obj2.loc

#posicao eixo x , idem para eixo y/z.

pos0x=obj0.LocX
pos1x=obj1.LocX
pos2x=obj2.LocX


	
for j in [pos0x,pos1x,pos2x]:
	print "Posicao do eixo X =",j,"\n"
			
		

