#Web Scraper Project

#URL = https://realpython.com/beautiful-soup-web-scraper-python/
import requests

URL = 'https://www.google.com/'
page = requests.get(URL)

print(page)
