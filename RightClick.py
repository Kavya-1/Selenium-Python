import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.maximize_window()

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_css_selector("span[class='context-menu-one btn btn-neutral']")

action = ActionChains(driver)
time.sleep(2)
action.context_click(button).perform()

time.sleep(2)

driver.find_element_by_css_selector("li[class='context-menu-item context-menu-icon context-menu-icon-copy']").click()

time.sleep(2)
driver.switch_to.alert.accept()

driver.close()