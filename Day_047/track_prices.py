from bs4 import BeautifulSoup
import requests
import smtplib
import Day_047.encrypted_data as encrypted_data
import os

URL = "https://www.jashanmal.com/collections/cookers/products/electrolux-60x60-cm-gas-cooker"
HEADER = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br"
}

my_email = os.environ["my_email"]
my_password = os.environ["Namlah_password"]
reciever_email = os.environ["reciever_email"]
#--------------------------------------WEB SCRAPPING--------------------------------------------#

response = requests.get(url=URL,headers=HEADER).text

soup = BeautifulSoup(response, "lxml")
# print(soup.prettify())
find_price = soup.find(class_="product__price on-sale").get_text()
product_title = soup.find(class_="h2 product-single__title").get_text().strip()
price_without_currency = find_price.split("AED")[1]
the_price = float(price_without_currency.strip().replace(",",""))

#--------------------------------------SEND EMAIL NOTIFICATION--------------------------------------------#

if the_price < 1000.0:
    with smtplib.SMTP("smtp.gmail.com", timeout=60, port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=reciever_email, msg=f"Subject:Price change alert\n\n{product_title} is now:\n AED {the_price}\n{URL}")