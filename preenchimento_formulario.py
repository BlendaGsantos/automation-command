from selenium import webdriver
from selenium.webdriver.common.by import By 
import time


driver = webdriver.Chrome()

driver.get('https://curso-web-scraping.pages.dev/#/exemplo/2')

email = driver.find_element(By.NAME, 'email')
senha = driver.find_element(By.NAME, 'senha')
enviar = driver.find_element(By.CSS_SELECTOR, 'button[type=\'submit\']')

email.send_keys('estudo.teste@gmail.com')
senha.send_keys('estudo.123')
enviar.click()

#email.send_keys('estudo.teste@gmail.com')
#senha.send_keys('estudo.123')
#email.sumit()

#from selenium.webdriver.common.keys import keys

time.sleep(20)

