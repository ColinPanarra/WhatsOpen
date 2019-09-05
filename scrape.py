
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

url = 'https://brandeis.sodexomyway.com/dining-near-me/open-now'

browser= webdriver.Chrome(executable_path='C:/Users/colin/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
browser.get(url)

html = browser.page_source

soup = BeautifulSoup(html, 'lxml')

#need to create a lambda function so that it finds specific dining-hall-container WITHOUT 'hide'
result = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['dining-halls-container'])
stores=[]
for h2 in result:
    h2tag = h2.find_all('div', class_='dining-halls-block')

    texts = h2.find_all(text=True)
    for str in texts:
        if(len(str)>1):
            stores.append(str)
            break

print(stores)
