# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Fonte Youtube:https://www.youtube.com/watch?v=PqSXxrVNpLA&list=PLK7KNOA7vbPOK1Ih3SXyaM1VnWut5Tn17&index=4


driver = webdriver.Chrome('./driver_Chrome79/chromedriver')
driver.get('http://google.com')


barra = driver.find_element(By.XPATH,"//input[@name = 'q']") 
barra.send_keys('Hello')
barra.send_keys(Keys.ENTER)

#AGORA FUNCIONOU O CLICK
driver.find_element(By.XPATH, "//a[@class = 'gb_4 gb_5 gb_ce gb_Wc']").click()



