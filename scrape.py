
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

#while True:

url = 'https://brandeis.sodexomyway.com/dining-near-me/open-now'

browser= webdriver.Chrome(executable_path=r'C:/Users/colin/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/webdriver/chrome')
browser.get(url)

html = browser.page_source

soup = BeautifulSoup(html, 'lxml')
stores = soup.find('div', class_='dining-halls-container')
print(store)
