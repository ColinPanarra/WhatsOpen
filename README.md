# WhatsOpen

Scrape.py takes data once an hour from https://brandeis.sodexomyway.com/dining-near-me/open-now using the beautiful soup library and selenium webdriver.

It sends a list of the open dining halls to a google firebase after which the app WhatsOpen reads the firebase to display the open dining halls in a listView. 
