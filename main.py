from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://automationpractice.techwithjatin.com/")
driver.maximize_window()
sleep(5)

driver.quit()