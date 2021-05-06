from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()

# driver = webdriver.Ie(executable_path="E:\Drivers\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
# driver.get("https://www.google.com")
# print(driver.title)
# driver.close()