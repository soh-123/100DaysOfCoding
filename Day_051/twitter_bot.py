from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/sohierelsafty/Downloads/chromedriver_mac64/chromedriver"
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]


class InternetSpeedTwitterBot():
    def __init__(self, driver_path) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.ser = Service(chrome_driver_path = driver_path)
        self.driver = webdriver.Chrome(service=self.ser, options=self.options)
        self.up = 0
        self.down = 0
        
    
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        
        time.sleep(5)
        go_btn = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_btn.click()
        time.sleep(60)

        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        print(f"down: {self.down}\nup: {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/")

        time.sleep(5)
        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div/span/span')
        login.click()

        time.sleep(5)
        emai_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label')
        emai_field.click()
        emai_field.send_keys(EMAIL)
        emai_field.send_keys(Keys.ENTER)

        time.sleep(5)
        username_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username_field.click()
        username_field.send_keys(USERNAME)
        username_field.send_keys(Keys.ENTER)

        time.sleep(5)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_field.click()
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)
        post = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        post.click()
        post.send_keys(f"Hello Twitter, \nThis is a bot created using python, the internet speed is:\nUpload:{self.up}\nDownload:{self.down}")
        tweet = self.driver.find_element(By.XPATH,'//div[@data-testid="tweetButtonInline"]')
        tweet.click()
        time.sleep(10)
        self.driver.quit()
        



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
