from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_driver_path = "/Users/sohierelsafty/Downloads/chromedriver_mac64/chromedriver"
ser = Service(chrome_driver_path = "/Users/sohierelsafty/Downloads/chromedriver_mac64/chromedriver")
driver = webdriver.Chrome(service=ser, options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


UPGRADE_EVERY_SECONDS = 1
LIMIT_CURSOR = 5
LIMIT_GRANDMA = 10
LIMIT_FARM = 15
LIMIT_MINE = 20
LIMIT_FACTORY = 5
# current
cursor = 0
grandma = 0
farm = 0
mine = 0
factory = 0


def upgrade():
    """Click and purchase the most expensive upgrade available from Store."""
    global cursor, grandma, farm, mine, factory
    try:
        avail_upgrades = driver.find_elements(
            By.CSS_SELECTOR, '.product.unlocked.enabled')
        number_of_upgrades_avail = len(avail_upgrades)
        if number_of_upgrades_avail == 1 and cursor < LIMIT_CURSOR:
            action.move_to_element(
                avail_upgrades[0]).click().perform()
            cursor += 1
        elif number_of_upgrades_avail == 2 and grandma < LIMIT_GRANDMA:
            action.move_to_element(
                avail_upgrades[1]).click().perform()
            grandma += 1
        elif number_of_upgrades_avail == 3 and farm < LIMIT_FARM:
            action.move_to_element(
                avail_upgrades[2]).click().perform()
            farm += 1
        elif number_of_upgrades_avail == 4 and mine < LIMIT_MINE:
            action.move_to_element(
                avail_upgrades[3]).click().perform()
            mine += 1
        elif number_of_upgrades_avail == 5 and factory < LIMIT_FACTORY:
            action.move_to_element(
                avail_upgrades[4]).click().perform()
            factory += 1
        # else:
        #     most_expensive_upgrade_avail = avail_upgrades[-1]
        #     action.move_to_element(
        #         most_expensive_upgrade_avail).click().perform()
    except IndexError:
        pass

action = ActionChains(driver)
time.sleep(5)
driver.find_element(By.ID, "langSelect-EN").click()
time.sleep(5)
cookie_btn = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
start_time = time.time()
track_time = start_time

number_of_cookies = driver.find_element(By.XPATH, '//*[@id="cookies"]')

while track_time - start_time <= 1800:  # 30 minutes
    cookie_btn.click()
    current_time = time.time()

    if current_time - track_time >= UPGRADE_EVERY_SECONDS:
        upgrade()
        track_time = current_time
    

