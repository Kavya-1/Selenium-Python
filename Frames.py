import time

from selenium import webdriver

driver = webdriver.Chrome("E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/overview-summary.html")
driver.find_element_by_css_selector("div[class='subNav'] ul[class='navList'] li").click()

time.sleep(2)

# switch to first frame
driver.switch_to.frame("packageListFrame")

time.sleep(3)
driver.find_element_by_css_selector("ul[title='Packages'] li a[target='packageFrame']").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame(1)
time.sleep(3)
driver.find_element_by_css_selector("ul[title='Interfaces'] li a").click()
time.sleep(3)

driver.switch_to.default_content()

driver.close()