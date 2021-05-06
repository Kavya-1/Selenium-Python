import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
# Open url
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

assert "Frames & windows" in driver.title

driver.implicitly_wait(5)

element = driver.find_element_by_xpath("//ul/li[2]")
element.click()

driver.close()

