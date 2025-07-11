from selenium import webdriver
from selenium.webdriver.common.by import By 


driver = webdriver.Chrome()

driver.get('https://curso-web-scraping.pages.dev/#/exemplo/1')

redes_sociais = driver.find_element(By.ID, 'social').find_elements(By.TAG_NAME, 'span')

for rede_social in redes_sociais:
    valor = rede_social.text
    print(valor)


driver.find_elements(By.LINK_TEXT, 'Instagram')
driver.find_elements(By.PARTIAL_LINK_TEXT, 'gram')
driver.find_elements(By.CSS_SELECTOR, '#role')

driver.find_elements(By.CSS_SELECTOR, 'div.main-container input.opcional-info')






