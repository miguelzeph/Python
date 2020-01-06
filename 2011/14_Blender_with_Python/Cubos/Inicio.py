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
	

for i in [obj0,obj1,obj2]:
	print "Objeto =",i,"\n"
	
for j in [pos0,pos1,pos2]:
	print "Posicao",j,"\n"
			
		


