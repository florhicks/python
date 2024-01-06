import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

SMTP_ADDRESS = ""
EMAIL = ""
PASSWORD = ""


BUY_PRICE = 300

product_URL = ""

headers = {"User-Agent": "",
           "Accept-Language":"" }

response = requests.get(url=product_URL,headers=headers)
soup = BeautifulSoup(response.content, "lxml")
price = float(soup.find(class_="a-offscreen").getText().split("$")[1])

if price < BUY_PRICE:
    message = f"{soup.find(id="productTitle").get_text().strip()} is now {price}"
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{product_URL}".encode("utf-8")
        )