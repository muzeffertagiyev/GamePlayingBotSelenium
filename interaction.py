from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "/Users/muzeffertagiyev/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, value="cookie")
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
needed_items = items[0:-1]
item_ids = [item.get_attribute("id") for item in needed_items]

shopping_time = time.time() + 5

stop = time.time() + 300

while True:
    cookie.click()

    if time.time()>shopping_time:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_price = price.text
            if element_price != "":
                cost = int(element_price.split('-')[1].replace(',',""))
                item_prices.append(cost)

        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(',',"")
        cookie_count = int(money_element)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        affordable_upgrades = {}
        for cost,id in cookie_upgrades.items():
            if cookie_count>cost:
                affordable_upgrades[cost]=id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, value=to_purchase_id).click()

        shopping_time = time.time() + 5

    if time.time()>stop:
        per_s = driver.find_element(By.ID, value="cps")
        print(per_s.text)
        break





