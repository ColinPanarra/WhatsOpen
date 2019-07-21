
import requests
from bs4 import BeautifulSoup
import time
#from selenium import webdriver

while True:
    url = 'https://brandeis.sodexomyway.com/dining-near-me/open-now'
    r=requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')




    #gets all divs in the div class dining halls list...
    dining_halls = soup.select('div.dining-halls-container')

    #stores = soup.find_all()"div[class='ad_item']")

    #dining_halls = soup.find_all(lambda tag: tag.name == 'div' and
    #                                   tag.get('class') == ['dining-halls-container'])


    stores = soup.select("div[class='dining-halls-container']")





    print(stores)

    #checks it once an hr
    time.sleep(60*60)
    #https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/



"""def save_html(html,path):
    with open(path,'wb') as f:
        f.write(html)

save_html(r.content, 'https://brandeis.sodexomyway.com/dining-near-me/open-now')



def open_html(path):
    with open(path,'rb') as f:
        return f.read()|

html = open_html('https://brandeis.sodexomyway.com/dining-near-me/open-now')
"""
