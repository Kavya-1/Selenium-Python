import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.google.com/")

driver.find_element_by_css_selector("input[name='q']").send_keys("puppies"+Keys.ENTER)

# scroll by the pixels
# driver.execute_script("window.scrollBy(0,1000)","")

# scroll till element
# india = driver.find_element_by_xpath("//td[text()='India']")
# driver.execute_script("arguments[0].scrollIntoView();", india)

# scroll to the end of the page
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

driver.close()