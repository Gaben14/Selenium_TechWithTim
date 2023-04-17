# Selenium Tutorial #3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Web-driver Call:
ser = Service(r"C:\Selenium\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# 1. Open the Home Page - https://www.techwithtim.net
driver.get("https://www.techwithtim.net")

# 2. Find and Click on the Python Programming link on the Home Page
link = driver.find_element(*(By.LINK_TEXT, "Python Programming"))
link.click()

# 3. Once the page /tutorials/python-programming page loads I want click on the "Python Beginner Tutorials" link
# Implement the explicit wait
try:
    beginner_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    beginner_link.click()

    # 4. After the tutorial page has been opened, I want to click on the "Get Started" button.

    get_started_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    get_started_btn.click()

    # 5. Go back to the home page
    for n in range(3):
        driver.back()

    for k in range(2):
        driver.forward()
except:
    # 6. Quit the WebDriver
    driver.quit()
