import win32com.client
import time

#-------------TECLADO-----------
wsh = win32com.client.Dispatch("WScript.Shell")
def escrever():
	wsh.SendKeys("a")
	
escrever()