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
        self.curtir_fotos()
        
    def curtir_fotos(self, tag_hashtag =''):
        driver = self.driver

        if tag_hashtag != '':
            driver.get('https://www.instagram.com/'+tag_hashtag)

        else:
            driver.get('https://www.instagram.com/')

            
        #Tive que fazer isso, pois ai eu vou rolando para baixo e ao mesmo tempo
        #pegando as Imagens.
        total_pic_hrefs =[] 
        # Se você rolar com tudo para baixo, ele não armazena as imagens anteriores.


        #Rolar para baixo página
        for i in range(0,3):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(2)

            #Pegar as imagens com a tag 'a'
            hrefs = driver.find_elements_by_tag_name('a')
            pic_hrefs = [elem.get_attribute('href') for elem in hrefs]

            for i in range(0,len(pic_hrefs)):
                if pic_hrefs[i] in total_pic_hrefs:
                    continue
                elif pic_hrefs[i][25:28] == '/p/': # Aproveitei e já coloquei aqui
                    total_pic_hrefs.append(pic_hrefs[i])
                else:
                    continue
        
        print (len(total_pic_hrefs)) 

        for pic_href in total_pic_hrefs:
                
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

