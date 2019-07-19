import scrapy

class openStoreSpider(scrapy.spider):
    name: 'openStores'
    start_urls = [
        'https://brandeis.sodexomyway.com/dining-near-me/open-now',
    ]
    def parse(self,response):
        for store in rsep









import requests
url = "https://brandeis.sodexomyway.com/dining-near-me/open-now"
page = requests.get(url);

import bs4;
soup = bs4.BeautifulSoup(page.content,'lxml');
List = soup.find(name="div", attrs={'class': 'dining-halls-list'})
#<div data-timezone="US/Eastern" class="dining-halls-list dining-halls-won"></div>
result = pd.DataFrame({{}})


#//https://docs.scrapy.org/en/latest/intro/overview.html
###test comment for branch
