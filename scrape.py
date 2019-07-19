
import requests
from bs4 import BeautifulSoup


url = 'https://brandeis.sodexomyway.com/dining-near-me/open-now'
r=requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')




#gets all divs in the div class dining halls list...
dining_halls = soup.select('.dining-halls-container')
stores = soup.find('h2', {'class' : 'dining-halls-container'})




print(dining_halls)


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
