#Abra dentro do Blender
import Blender
obj = Blender.Object.Get()
obj_name = obj[1].getName()
obj_loc = obj[1].getLocation()
obj_mod = obj[1].getDrawType()


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

print obj_mod_str