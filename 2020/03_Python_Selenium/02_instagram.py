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


        #-----Curtir todos da Página escolhida-------
        #self.curtir_fotos('https://www.instagram.com/explore/locations/280640861/faculdade-de-medicina-de-taubate/')

        #-----Verificar Seguidores-------
        self.follow()


    def follow(self):
        driver = self.driver

        #Acessar meu perfil
        driver.get('https://www.instagram.com/datastorm29/')

        time.sleep(2)

        #----Seguidores -----

        seguidores_button = driver.find_element(By.XPATH,"//a[@href ='/datastorm29/followers/']")
        seguidores_button.click()

        time.sleep(1.5)

        #Rolar para baixo a barra de Seguidores
        for i in range(0,5):
            fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(1)

        hrefs_seguidores = driver.find_elements(By.XPATH,'//a[@class = "FPmhX notranslate  _0imsa "]')
        pic_hrefs_seguidores = [elem.get_attribute('href') for elem in hrefs_seguidores]


        #Voltar pro meu perfil
        driver.get('https://www.instagram.com/datastorm29/')


        #-----Seguindo----

        seguindo_button = driver.find_element(By.XPATH,"//a[@href ='/datastorm29/following/']")
        seguindo_button.click()

        time.sleep(2)

        #Rolar para baixo a barra de seguindo
        for i in range(0,30):
            fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(3)

        hrefs_seguindo = driver.find_elements(By.XPATH,'//a[@class = "FPmhX notranslate  _0imsa "]')
        pic_hrefs_seguindo = [elem.get_attribute('href') for elem in hrefs_seguindo]

        nao_me_segue = list(set(pic_hrefs_seguindo)-set(pic_hrefs_seguidores))

        print('Seu seguidores: ',len(pic_hrefs_seguidores))
        print('Quem você segue: ',len(pic_hrefs_seguindo))
        print('Quem não te segue:',len(nao_me_segue))

        #xx = list(set(pic_hrefs_seguidores)-set(pic_hrefs_seguindo))
        #print(xx)

        for deletar in nao_me_segue:
            time.sleep(6)

            driver.get(deletar)

            time.sleep(3)

            button_seguir = driver.find_element(By.XPATH,"//span[@class ='vBF20 _1OSdk']")
            button_seguir.click()

            time.sleep(3)

            try:
                confirmar = driver.find_element(By.XPATH,"//button[@class ='aOOlW -Cab_   ']")
                confirmar.click()
                print('deletado')
            except:
                print('Ele te segue,  e você não o segue, logo foi adicionado')
            
        
    def curtir_fotos(self, url):
        driver = self.driver
        
        driver.get(url)
   
        #Tive que fazer isso, pois ai eu vou rolando para baixo e ao mesmo tempo
        #pegando as Imagens.
        total_pic_hrefs =[] 
        # Se você rolar com tudo para baixo, ele não armazena as imagens anteriores.


        #Rolar para baixo página
        for i in range(0,1):
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

        

            
            
                 

miguel = InstagramBot('xxx','xxx')
miguel.login()

