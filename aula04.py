from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://curso-web-scraping.pages.dev/#/exemplo/3')

select = Select(driver.find_element(By.NAME, 'regiao'))

for opt in select.options:
    print(f"Valor: {opt.get_attribute('value')} | Texto: {opt.text}")

select.select_by_index(3)
print(select.first_selected_option.text)

select.select_by_visible_text('Mato Grosso')
print(select.first_selected_option.text)

select.select_by_value('0')
print(select.first_selected_option.text)

multi = Select(driver.find_element(By.CSS_SELECTOR, '#multi-select select'))

multi.select_by_visible_text('Python')
multi.select_by_visible_text('Selenium')
multi.select_by_visible_text('Scrapy')

for option in multi.all_selected_options:
    print(option.text)

time.sleep(10)
driver.quit()
