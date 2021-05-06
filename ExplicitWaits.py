from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

print(driver.title)

# Click on flights button
driver.find_element_by_css_selector("ul[id='uitk-tabs-button-container'] li:nth-child(2)").click()

# Enter leaving from city
driver.find_element_by_css_selector("button[aria-label='Leaving from']").click()
driver.find_element_by_id("location-field-leg1-origin").send_keys("Bengaluru" + Keys.ENTER)

# Enter destination city
driver.find_element_by_css_selector("button[aria-label='Going to']").click()
driver.find_element_by_id("location-field-leg1-destination").send_keys("Mumbai" + Keys.ENTER)

# Click on search button
searchElement = driver.find_element_by_xpath("//button[@data-testid='submit-button']")
searchElement.submit()

stops0 = driver.find_element_by_css_selector("input[id='stops-0']")

wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable, stops0)

stops0.click()

driver.close()
