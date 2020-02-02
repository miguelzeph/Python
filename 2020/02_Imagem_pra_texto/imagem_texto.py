import base64

#Ler a imagem como texto
with open("./lorentz.png",'r') as imageFile:
	str_var = base64.b64encode(imageFile.read())
	print(str_var[0:100])
	print(len(str_var))
	imageFile.close()
#Ler o texto e transformar em img
with open('./lorentz_novo.png','w') as imageFile2:
	#imageFile2.write(str_var.decode('base64')) #Copia a imag inteira
	imageFile2.write(str_var[:100000].decode('base64'))#Copia uma parte apenas
	imageFile2.close()
	
