# Selenium Tutorial #2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Gives us access to the Enter, Esc, Delete and other keys... Use Keys.Return for enter
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ser = Service(r"C:\Selenium\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.techwithtim.net")
print(driver.title)

# ================ Search Bar with sleep and explicit wait ================
# search_bar = driver.find_element_by_name("s")
search_bar = driver.find_element(By.NAME, "s")
# HTML name attribute should be unique the same way as IDs
search_bar.send_keys("test" + Keys.RETURN)
# Instead using separate send_keys - I combined them.
# search_bar.send_keys(Keys.RETURN)  # Hit the Enter/Return button

# time.sleep(5)  # instead of this it's better to use explicit waits, see below

# Explicit Wait:
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # print(main)
    # Use the * before the By. -> This asterisk is a standard Python thing that will expand tuples into positional arguments that can be passed into methods.
    articles = main.find_elements(*(By.TAG_NAME, "article"))
    for article in articles:
        header = article.find_element(*(By.CLASS_NAME, "entry-summary"))

        print(header.text)

finally:
    driver.quit()  # Always use quit

#  ================ Search Bar with sleep and explicit wait ================

driver.quit()  # Always use quit
