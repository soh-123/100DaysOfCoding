from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import encrypted_data

URL = "https://www.jashanmal.com/collections/cookers/products/electrolux-60x60-cm-gas-cooker"
HEADER = {"My header"
}

my_email = "my_email"
my_password = "my_password"
reciever_email = "reciever_email"
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