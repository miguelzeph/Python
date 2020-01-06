from visual import *



ball=sphere(pos=(0,10,0),radius=0.5,color=color.red)
ground=box(pos=(0,-1,0),size=(10,1,10))

gravity=9.8
seconds=0
dt= 0.01

altura=10+0*seconds-0.5*9.8*(seconds)**2

#-------------Subida---------------------
def sob():
	#perceba que tive que achar v0 que ele volta , e ai sim ir diminuindo a velo com a altitude...
	seconds=0
	dt=0.01
	altura=0+14.112*seconds-0.5*9.8*(seconds)**2
	if altura <10:
		while altura <10:
			altura=0+14.112*seconds-0.5*9.8*(seconds)**2
			rate(100)
			seconds=seconds+dt
			ball.pos=(0,altura,0)
	altura=10
	return des()

#-----------------Descida--------------------
def des():
	seconds=0
	dt= 0.01
	altura=10+0*seconds-0.5*9.8*(seconds)**2
	if altura > 0:
		while altura > 0:	
			altura=10+0*seconds-0.5*9.8*(seconds)**2
			rate(100)
			seconds=seconds+dt
			ball.pos=(0,altura,0)
	altura=0
	#print seconds
	return sob()
#--------------------------------------------

#----------------Chamar as func---------------
des()



