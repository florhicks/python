from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def lang_select():
    try:
        time.sleep(10)
        # In this case, I chose my language, feel free to change it!
        ES = driver.find_element(by=By.ID, value="langSelect-ES")
        ES.click()
    except:
        pass

def cookie_click():
    cookie = driver.find_element(by=By.ID, value="bigCookie")
    cookie.click()

def golden_cookie_click():
    try:
        golden_cookie = driver.find_element(by=By.XPATH, value='//*[@id="shimmers"]/div')
        golden_cookie.click()
    except:
        pass


def buy_products():
    try:
        product_price = driver.find_elements(by=By.CSS_SELECTOR,
                                             value="div.product.unlocked.enabled div.content span.price")
        prices_list = [int(price.text.replace(",", "")) for price in product_price]
        products = driver.find_elements(by=By.CSS_SELECTOR, value="div.product.unlocked.enabled")
        max_price = prices_list.index(max(prices_list))

        products[max_price].click()
    except:
        pass


def buy_upgrade():
    try:
        upgrade = driver.find_element(by=By.XPATH, value='//*[@id="upgrade0"]')
        upgrade.click()
    except:
        pass


def close_alert():
    try:
        close_achievement = driver.find_element(by=By.CLASS_NAME, value="close")
        close_achievement.click()
    except:
        pass


minutes = int(input("How many minutes do you want to run the bot? "))
auto_click = input("Do you want auto click on the big cookie? (yes/no): ".lower()) == "yes"
auto_click_golden = input("Do you want auto click on golden cookies? (yes/no): ".lower()) == "yes"
auto_click_upgrades = input("Do you want auto click on upgrades? (yes/no): ".lower()) == "yes"
auto_click_buildings = input("Do you want auto click on buildings? (yes/no): ").lower() == "yes"
first_time = input("Is this your first time playing the game? (yes/no): ").lower() == "yes"

driver_service = webdriver.ChromeService(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

lang_select()
print("Starting...")
time.sleep(10)


timeout = time.time() + 5
time_to_stop = time.time() + 60 * minutes
print("Ready!")
while time.time() < time_to_stop:
    if auto_click:
        cookie_click()
    if auto_click_golden:
        golden_cookie_click()
    if time.time() > timeout:
        if auto_click_buildings:
            buy_products()
        if auto_click_upgrades:
            buy_upgrade()
        close_alert()


        timeout = time.time() + 5
print("The time you specified for the bot has run out. ")
input("Press ENTER to close. ")
driver.quit()