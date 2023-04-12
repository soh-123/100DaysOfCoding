from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/sohierelsafty/Downloads/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

dictionary = {i: {"time": driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/'
                                                                  f'div[2]/div[2]/div/ul/li[{i + 1}]/time').text,
                  "name": driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[2]'
                                                                  f'/div[2]/div/ul/li[{i + 1}]/a').text
                  } for i in range(5)
              }
print(dictionary)

driver.quit()