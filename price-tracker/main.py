from bs4 import BeautifulSoup
from config import *
import requests
import smtplib

PRODUCT_URL = "https://www.amazon.com.br/PlayStation-CFI-1214A01X-Console-5/dp/B0BNSR3MW9/ref=sr_1_5?keywords=playstation+5&sr=8-5&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
TARGET_PRICE = 4200

header = {
    "Accept-Language": "pt-BR,pt;q=0.8",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

response = requests.get(PRODUCT_URL, headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

price_tag = soup.find_all(name="span", class_="a-offscreen")[0]
price = float(price_tag.getText().replace(".","").replace(",",".").split("$")[1])

product_name_tag = soup.find(name="span", id="productTitle")
product_name = product_name_tag.getText().strip()

if TARGET_PRICE > price:
    message = f"{product_name} has reached R${price}"
    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=F"Subject: Amazon price Alert!\n\n{message}\n{PRODUCT_URL}"
        )
        
        print("sent email")
