#Dica: Teste os comandos no IDLE
import win32com.client

wsh = win32com.client.Dispatch("WScript.Shell")

#--------Escrever------------
#Escreve "a"
wsh.SendKeys("a")

#Escreve "Miguel"
wsh.SendKeys("Miguel")

#------Apertar TECLAS-------

#Aperta tecla ENTER
wsh.SendKeys("{ENTER}")

#Aperta tecla LEFT
wsh.SendKeys("{LEFT}")

#Aperta tecla BACKSPACE
wsh.SendKeys("{BACKSPACE}")

#Aperta 2 vezes tecla ENTER
wsh.SendKeys("{ENTER}{ENTER}")

#Aperta ENTER e BACKSPACE
wsh.SendKeys("{ENTER}{BACKSPACE}")

#DICA !!! Utilize a combinacao de str com numero
wsh.SendKeys("{ENTER}"*5)

#-------Combinar--------------

#Resultado "Migu"
wsh.SendKeys("Miguel""{BACKSPACE}{BACKSPACE}")

#Resultado nada...
wsh.SendKeys("A""{BACKSPACE}")









