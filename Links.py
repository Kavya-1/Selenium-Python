from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present", len(links))

for link in links:
    print("Link is = ", link.get_attribute("href"))
    print("Link text is = ", link.get_attribute("innerText"))

driver.find_element_by_link_text("Gmail").click()
print(driver.title)

driver.back()

driver.find_element_by_partial_link_text("history").click()

print("History page ", driver.title)
driver.close()
