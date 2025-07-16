from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time

driver = webdriver.Chrome()

driver.get('https://curso-web-scraping.pages.dev/#/desafio/1')


email = driver.find_element(By.NAME, 'email')

senha = driver.find_element(By.NAME, 'senha')



select = Select(driver.find_element(By.NAME, 'dia'))
select.select_by_index(11)

select = Select(driver.find_element(By.NAME, 'mes'))
select.select_by_index(5)


select = Select(driver.find_element(By.NAME, 'ano'))
select.select_by_index(28)

email.send_keys('estudo.teste@gmail.com')
senha.send_keys('estudemais')

notifica = driver.find_element(By.ID, 'airplane-mode')
notifica.click()

enviar = driver.find_element(By.CSS_SELECTOR, 'button[type=\'submit\']')
enviar.click()














time.sleep(10)