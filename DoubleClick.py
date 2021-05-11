import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")

clickMe = driver.find_element_by_css_selector("button[ondblclick]")
action = ActionChains(driver)
time.sleep(2)
action.double_click(clickMe).perform()
time.sleep(2)

assert driver.find_element_by_css_selector("input#field2").text in "Hello World!"

driver.close()
