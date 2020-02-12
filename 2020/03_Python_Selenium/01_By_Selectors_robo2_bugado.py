# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Tem que colocar caminho do driver (neste caso Chrome)
driver = webdriver.Chrome('./driver_Chrome79/chromedriver')

# Abrir a página do Python Club
driver.get('http://google.com')

#Escreve na barra
barra = driver.find_element_by_name('q')
barra.send_keys("ABC")

#Clica na página para "desclicar" da barra
pagina = driver.find_element_by_id("lga")
pagina.click()

#Clica no botão... problema está aqui, já tentei de várias maneiras
#, como por exemplo, por ID... NAME... não vai
button = driver.find_element(By.CLASS_NAME,"gNO89b")
button.click()



#Só para ver 
print(pagina)
print(barra)
print(button)
