import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
print("Title of page is = ", driver.title)

driver.find_element_by_xpath("//h2[text()='Alert']/parent::div/div/button").click()

wait = WebDriverWait(driver, 10)
wait.until(ec.alert_is_present())

time.sleep(2)
alert = driver.switch_to.alert

time.sleep(2)
alert.accept()
# alert.dismiss()
# alert.send_keys()

driver.close()

