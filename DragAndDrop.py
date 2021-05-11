import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.maximize_window()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

action = ActionChains(driver)
capital = driver.find_element_by_css_selector("div#box6")
country = driver.find_element_by_css_selector("div#countries div#box106")
# action.context_click(capital).move_to_element(country).release().perform()
action.drag_and_drop(capital, country).perform()
time.sleep(2)

driver.close()