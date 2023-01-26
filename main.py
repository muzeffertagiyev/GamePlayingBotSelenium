from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint 



chrome_driver_path = "/Users/muzeffertagiyev/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# https://www.python.org/
# https://www.amazon.com/2022-Apple-MacBook-Laptop-chip/dp/B0B3C57XLR/ref=sr_1_1?crid=23N9O9X33V0JH&keywords=macbook+pro+13+inch&qid=1661880574&sprefix=macbook+pro+13+inch%2Caps%2C234&sr=8-1
driver.get('https://www.python.org/')


# getting events

# event_dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# events= {}

# for n in range(len(event_names)):
#     events[n] = {
#         "time":event_dates[n].text,
#         "name":event_names[n].text
#     }
# pprint(events)


# using css selector

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=('.documentation-widget p a'))
# print(documentation_link.text)


# using XPATH(we will copy Xpath from website in inspect)

# submit_website_bug = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_website_bug.text)


# for getting product's price from amazon

# class_name = driver.find_element(By.CLASS_NAME, value='a-price')
# price_symbol = class_name.find_element(By.CLASS_NAME, value='a-price-symbol')
# price_fraction = class_name.find_element(By.CLASS_NAME, value="a-price-fraction")
# price = class_name.find_element(By.CLASS_NAME, value="a-price-whole")
# print(f"{price_symbol.text} {price.text}.{price_fraction.text}")

# it only close above mentioned website
# driver.close()

# it quit from chrome with all websites
# driver.quit()