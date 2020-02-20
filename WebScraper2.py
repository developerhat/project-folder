#WebScraper 2.0

from bs4 import BeautifulSoup
import requests

#Works but it's not my code, idk what it does 
URL = "https://www.amazon.it/gp/product/B072BG9Z8W/"
MY_PRICE = 80

actual_price = check_price()
if actual_price <= MY_PRICE:
    send_email(actual_price)



def check_price() -> int:
    # get HTML page
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    headers = {"user-agent": user_agent}
    req = requests.get(URL, headers=headers)

    # get price
    soup = BeautifulSoup(req.text, "html.parser")
    span = soup.find("span", {"id": "priceblock_ourprice"}) # <span id="priceblock_ourprice">...</span>
    price = span.text   # XY,ZW €

    return int(price[:2])
