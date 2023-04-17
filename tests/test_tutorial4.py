# Selenium Tutorial #4
'''
The goal of this tutorial is to click and update the game inside the CookieClicker application
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Web-driver Call:
ser = Service(r"C:\Selenium\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# 1. Open the Home Page - https://www.orteil.dashnet.org/cookieclicker/
driver.get("https://orteil.dashnet.org/cookieclicker/")

# 2. Click on the web-cookie button and the English button
driver.implicitly_wait(10)

consent_btn = driver.find_element(By.CLASS_NAME, "fc-cta-consent")
consent_btn.click()

english_btn = driver.find_element(By.ID, "langSelect-EN")
english_btn.click()

driver.implicitly_wait(30)

# 2. Get the cookie buttons
cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

# 2. ActionChains
actions = ActionChains(driver)

for i in range(5000):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])

    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

# The actions will be performed only when the action.perform() is used.

