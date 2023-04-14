# Selenium Tutorial #1.b

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# PATH = "C:\Selenium\chromedriver.exe"
# Alternate approach to be used instead of direct path (which is deprecated):
ser = Service(r"C:\Selenium\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.techwithtim.net")
print(driver.title)
driver.quit()  # Always use quit
