#Abra dentro do Blender
import Blender
# Coleta dados
obj = Blender.Object.Get()[1]
obj_name = obj.getName()
obj_loc = obj.getLocation()
obj_loc_str = str(obj_loc)
obj_mod = obj.getDrawType()
if obj_mod == 1:
	obj_mod_str = "Bounding box"
elif obj_mod == 2:
	obj_mod_str = "Wire"
elif obj_mod == 3:
	obj_mod_str = "Solid"
elif obj_mod == 4:
	obj_mod_str = "Shaded"
elif obj_mod == 5:
	obj_mod_str = "Textured"
# Escreve dados num arquivo de texto
arquivo = file('./arquivo_dados.txt', 'w')
arquivo.write(str(obj_name)+'\n')
arquivo.write(str(obj_loc_str)+'\n')
arquivo.write(str(obj_mod_str)+'\n')
arquivo.close()
