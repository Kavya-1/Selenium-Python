import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/")
path = "E:\screenshots\homepage.png"
driver.save_screenshot(path)
path = "E:\screenshots\homepage1.jpg"
driver.get_screenshot_as_file(path)
driver.close()
