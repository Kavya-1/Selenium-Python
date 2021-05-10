import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)
print("Parent window title = ", driver.title)

handles = driver.window_handles
time.sleep(2)
driver.switch_to.window(handles.__getitem__(1))
print("First window after switching=", driver.title)
time.sleep(2)

driver.find_element_by_link_text("Downloads").click()

driver.switch_to.window(handles.__getitem__(0))
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(2)

handles = driver.window_handles
driver.switch_to.window(handles.__getitem__(2))
print("Second window=", driver.title)

time.sleep(3)

driver.quit()