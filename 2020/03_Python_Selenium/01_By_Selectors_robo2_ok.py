# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#Fonte: https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text


# Tem que colocar caminho do driver (neste caso Chrome)
driver = webdriver.Chrome('./driver_Chrome79/chromedriver')

# Abrir a página do Python Club
driver.get('http://google.com')

barra = driver.find_element_by_name('q') # ou pelo By... driver.find_element(By.NAME,'q')
barra.send_keys("ABC")

#Clica na página para tirar o cursor da barra
#pagina = driver.find_element_by_id("lga")
#pagina.click()


#button = driver.find_element(By.CLASS_NAME,"gNO89b")
#button.click()
barra.send_keys(Keys.ENTER)

time.sleep(2)


#driver.find_element(By.LINK_TEXT,"ABC Home Page - ABC.com").click() #Não funcionou.... tive que fazer por classe
ABC_page= driver.find_element(By.CLASS_NAME,"LC20lb")
ABC_page.click()



