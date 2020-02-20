#Web Scraper Project

#URL = https://realpython.com/beautiful-soup-web-scraper-python/
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

URL = 'https://www.google.com/'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.find(id='ResultsContainer')
soup.findAll('a')

print(page)
print(results) #Returns None, why?
