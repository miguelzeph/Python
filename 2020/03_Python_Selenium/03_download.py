# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

#Fonte Youtube: https://www.youtube.com/watch?v=e5xwLr3xYiI&list=PLK7KNOA7vbPOK1Ih3SXyaM1VnWut5Tn17&index=12


options = webdriver.ChromeOptions()

preferences = {"download.default_directory": "/home/miguel/Apps/Python_Git/2020/03_Python_Selenium"}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome('./driver_Chrome79/chromedriver',options = options)
driver.get("https://www.whatsapp.com/download/")


driver.find_element(By.XPATH, "//a[@href='https://web.whatsapp.com/desktop/windows/release/x64/WhatsAppSetup.exe']").click()

