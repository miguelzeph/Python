from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Tem que colocar caminho do driver (neste caso Chrome)
driver = webdriver.Chrome('./driver_Chrome79/chromedriver')

# Abrir a página do Python Club
driver.get('http://google.com')

barra = driver.find_element_by_name('q')
barra.send_keys("ABC")

pagina = driver.find_element_by_id("lga")
pagina.click()


button = driver.find_element(By.CLASS_NAME,"gNO89b")
button.click()


print(pagina)
print(barra)

