import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from table import genTable

url = 'https://datastudio.google.com/reporting/a6dc07e9-4161-4b5a-9f2a-6f9be486e8f9/page/2itOB'

options = Options()
options.headless = True
# Auto configuração de GeckoDriver
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)
time.sleep(20)

# Acesso ao
# <lego-table class='table'>
#   <div class='table'>
#    ...
#   </div>
# </lego-table>
element = driver.find_element_by_xpath(
    "//lego-table[@class='table']//div[@class='table']")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
headTable = soup.find('div', {'class': 'headerRow'})
bodyTable = soup.find('div', {'class': 'tableBody'})

# Pegar dados do HTML
header = []
body = []

# Acesso ao
# <div class='headCell'>
#   {{ item }}
#   ...
# </div>
#
# <div class='row'>
#   <div class='cell'>
#     {{ item }}
#   </div>
#    ...
# </div>
for i in headTable.find_all_next('div', {'class': 'headerCell'}):
    header.append(str(i.text))
for i in bodyTable.find_all_next('div', {'class': 'row'}):
    lista = []
    for j in i.find_all_next('div', {'class', 'cell'}, limit=7):
        lista.append(str(j.text).strip('.'))
    body.append(lista)

print(genTable(header, body))
driver.quit()
