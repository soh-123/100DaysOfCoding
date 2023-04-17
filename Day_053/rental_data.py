from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ZILLO_URL = f"https://www.zillow.com/NY/rentals/"
HEADER = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br"
}
#------------------------------------SELENIUM INITIALIZATION---------------------------------------#

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
ser = Service(chrome_driver_path = "/Users/sohierelsafty/Downloads/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=ser, options=options)

#------------------------------------SCRAPPING ZILLO---------------------------------------#

response = requests.get(url=ZILLO_URL,headers=HEADER).text
soup = BeautifulSoup(response, "html.parser")


test = soup.findAll("script", attrs={"type": "application/json"})
rent_data = test[1].text
rent_data = rent_data.replace("<!--", "")
rent_data = rent_data.replace("-->", "")

rent_data = json.loads(rent_data)

all_prices = []
all_addresses = []
all_links = []
for x in rent_data["cat1"]["searchResults"]["listResults"]:
    try:
        all_prices.append(x["price"])
    except KeyError:
        all_prices.append(x["units"][0]["price"])
    
    all_addresses.append(x["address"])

    all_links.append(x["detailUrl"])
    for i in range(len(all_links)):
        if not all_links[i].startswith("https"):
            all_links[i] = "https://www.zillow.com" + all_links[i]
    

#------------------------------------POSTING TO GOOGLE FORM---------------------------------------#
for i in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScRaJa9wXDU7PYpbF9Azt80Ht5EMjD2iV_bIR04S6sXruW43w/viewform?usp=sf_link")
        
    time.sleep(1)
    adrress = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')[0]
    adrress.click()
    adrress.send_keys(all_addresses[i])
    time.sleep(1)
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')[1]
    price.click()
    price.send_keys(all_prices[i])
    time.sleep(1)
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')[2]
    link.click()
    link.send_keys(all_links[i])
    time.sleep(1)
    submit_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_form.click()

driver.quit()