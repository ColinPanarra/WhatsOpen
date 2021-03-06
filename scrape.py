import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyrebase


#########################
#  Scrapes open stores #
#########################

#grabs the url and turns it into lmxl for bs4 to read
url = 'https://brandeis.sodexomyway.com/dining-near-me/open-now'
browser= webdriver.Chrome(executable_path='C:/Users/colin/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
#need to create a lambda function so that it finds specific dining-hall-container WITHOUT 'hide'
result = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['dining-halls-container'])


stores=[]
#loops throough all the open stores to get the headers
#since some headers have empty text or just a space we search for
#a header with more than one character to get the actual name of the store
for h2 in result:
    h2tag = h2.find_all('div', class_='dining-halls-block')
    texts = h2.find_all(text=True)
    for str in texts:
        if(len(str)>1):
            stores.append(str)
            break



#################################
#  Writes Stores to the Firebase #
#################################
#information to give to the firebase
config = {
  "apiKey": "api key",
  "authDomain": "whatsopen-6eacf.firebaseapp.com",
  "databaseURL": "https://whatsopen-6eacf.firebaseio.com",
  "storageBucket": "gs://whatsopen-6eacf.appspot.com",
  "projectId": "whatsopen-6eacf",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("@genericemail", "password")



db = firebase.database();
#sets stores from the scraping in the db and uploads them
db.child("stores").set(stores, user['idToken'])
openStores = db.child("stores").get(user['idToken']).val();
