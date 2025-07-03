from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()

driver.get('https://curso-web-scraping.pages.dev/#/exemplo/1')


name = driver.find_element(By.ID, 'user').get_property('value') 
print(f'name: {name}')

signo = driver.find_element(By.ID, 'zodiac').get_property('value') 
print(f'{signo=}')


genero = driver.find_element(By.NAME, 'genderOfBirth').get_property('value')
print(f'Gênero: {genero}')

