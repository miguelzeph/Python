import win32api

def get_cords():
	x,y = win32api.GetCursorPos()
	print x, y

get_cords()

raw_input()