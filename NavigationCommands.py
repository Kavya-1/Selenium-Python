import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
# Open url
driver.get("http://newtours.demoaut.com/")
print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")

print(driver.title)

driver.back() # navigate back
print(driver.title)

driver.forward() # navigate forward
print(driver.title)

driver.forward()
print(driver.title)

driver.back()
print(driver.title)

driver.close()