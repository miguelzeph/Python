import subprocess
import time

for i in range(0,10):
	
	time.sleep(0.5)
	subprocess.Popen(["python27.exe","./mouse.py"])
	time.sleep(0.5)
	subprocess.Popen(["python27.exe","./teclado.py"])
	
# Poderia usar o execfile(...), porem, fiz isso para aplicar
# a biblioteca subprocess
