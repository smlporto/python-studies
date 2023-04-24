from bs4 import BeautifulSoup
import requests

PRODUCT_URL = "https://www.amazon.com.br/PlayStation-CFI-1214A01X-Console-5/dp/B0BNSR3MW9/ref=sr_1_5?keywords=playstation+5&sr=8-5&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"

headers = {
    "Accept-Language": "pt-BR,pt;q=0.8",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

response = requests.get(PRODUCT_URL, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

price_tag = soup.find_all(name="span", class_="a-offscreen")[0]
price = price_tag.getText().split("$")[1]

print(price)