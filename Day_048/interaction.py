from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = "/Users/sohierelsafty/Downloads/chromedriver_mac64/chromedriver"
ser = Service(chrome_driver_path = "/Users/sohierelsafty/Downloads/chromedriver_mac64/chromedriver"
)
driver = webdriver.Chrome(service=ser, options=options)


driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

# articles_number = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# # articles_number.click()

# all_portals = driver.find_element(by=By.LINK_TEXT, value="View source")
# # all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CSS_SELECTOR, ".btn-block")

first_name.send_keys("Sohier")
last_name.send_keys("Lotfy")
email.send_keys("engsoh6@gmail.com")
email.submit()
