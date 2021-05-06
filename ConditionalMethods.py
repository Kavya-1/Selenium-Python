import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
# Open url
driver.get("http://demo.automationtesting.in/Windows.html")

element = driver.find_element_by_xpath("//ul/li[2]")

if element.is_displayed():
    print("Element is displayed ")
else:
    print("Element is not displayed")

if element.is_enabled():
    print("Element is enabled ")
    element.click()
    print(driver.title)
else:
    print("Element is not displayed")

radioButton = driver.find_element_by_xpath("//input[@name='radiooptions']")
if radioButton.is_selected():
    print("Radio button is selected")
else:
    print("Radio button is not selected")
    radioButton.click()
    if radioButton.is_selected():
        print("Radio button is selected")

driver.close()

