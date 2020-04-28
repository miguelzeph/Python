# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import numpy as np

import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./driver_Chrome79/chromedriver')

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        
        # Username
        user_element =  driver.find_element(By.XPATH,"//input[@name = 'username']")
        user_element.clear()
        user_element.send_keys(self.username)
        #Senha
        password_element =  driver.find_element(By.XPATH,"//input[@name = 'password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(1)
        #Clicar no Botão
        driver.find_element(By.XPATH, "//div[@class = '                   Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ']").click()
        #CLicar para não aceitar notificação
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@class = 'aOOlW   HoLwm ']").click()
        """
        #Rolar pra baixo
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(1)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(1)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        """

        #driver.get('https://www.instagram.com/python.coding/')
        #time.sleep(1)
        #Clicar curtir
        #driver.find_element(By.XPATH,"//svg[@aria-label = 'Curtir']").click()
        #driver.find_element(By.XPATH,"//button[@class = 'wpO6b ']")
        #curtir = driver.find_element_by_class_name("//button[@class = 'wpO6b ']")
        #print(curtir)
        time.sleep(2)
        self.curtir_fotos('pythoncode')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/tags/'+hashtag+'/')
        time.sleep(5)

        for i in range(0,2):
            #Descer a Página
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs ]

        print(len(pic_hrefs))
        
        for pic_href in pic_hrefs:
            
            #/p/ são imagens
            if pic_href[25:28] == '/p/':

                driver.get(pic_href)
                time.sleep(2*np.random.randint(1,4))


                #verificar_botao = driver.find_element(By.XPATH,"//svg[@aria-label='Curtir']")
                #verificar = driver.find_element(By.XPATH, "//span[./button[./svg[@aria-label='Curtir']]]")
                
                verificar = driver.find_element_by_css_selector('svg').get_attribute("aria-label")
                curtir = driver.find_element(By.XPATH,"//span[@class ='fr66n']")
                
                if verificar == "Curtir":

                    curtir.click()
                    print('Curtiu')
                else:
                    print('Já estava curtida')
                    time.sleep(2*np.random.randint(1,4))
                
                time.sleep(15*np.random.randint(1,2))
                

                
            

miguel = InstagramBot('xxxxx','xxxxx')
miguel.login()

