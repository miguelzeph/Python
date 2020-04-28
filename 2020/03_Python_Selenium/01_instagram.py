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
        #Entrar no Site do instagram
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
        #Clicar no Botão login
        driver.find_element(By.XPATH, "//div[@class = '                   Igw0E     IwRSH      eGOV_         _4EzTm    bkEs3                          CovQj                  jKUp7          DhRcB                                                    ']").click()
        #CLicar para não aceitar notificação
        time.sleep(5)
        driver.find_element(By.XPATH,"//button[@class = 'aOOlW   HoLwm ']").click()
        time.sleep(2)
        #Curtir todos da Página escolhida
        self.curtir_fotos_tag('datascientist')

    def curtir_fotos_tag(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/tags/'+hashtag+'/')
        time.sleep(5)

        #Rolar para baixo página
        for i in range(0,6):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    
        #Pegar as imagens com a tag 'a'
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

        
        for pic_href in pic_hrefs:
            #/p/ são imagens, o restante são páginas etc...
            if pic_href[25:28] == '/p/':
                
                #Vai para página da imagem
                driver.get(pic_href)
                time.sleep(2*np.random.randint(1,4))

                #Verificar se foi curtida
                verificar = driver.find_element_by_css_selector('svg').get_attribute("aria-label")
                
                #pegar botao de curtir
                curtir = driver.find_element(By.XPATH,"//span[@class ='fr66n']")
                
                if verificar == "Curtir":
                    #curtir
                    curtir.click()
                    print('Curtiu')
                else:
                    #Já foi curtida
                    print('Já estava curtida')
                    time.sleep(2*np.random.randint(1,4))
                
                time.sleep(15*np.random.randint(1,2))     

miguel = InstagramBot('xxxx','xxx')
miguel.login()

