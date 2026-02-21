from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
driver.get("https://www.kozminski.edu.pl/pl")
driver.maximize_window()
sleep(5)

driver.quit()