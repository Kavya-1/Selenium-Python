import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\\Documents"})

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe", chrome_options = chromeOptions)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")
textbox = driver.find_element_by_id("pdfbox")
driver.execute_script("arguments[0].scrollIntoView();", textbox)
textbox.send_keys("Sample selenium code")
driver.find_element_by_id("createPdf").click()
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_css_selector("a#pdf-link-to-download")).click().perform()
time.sleep(5)

# driver.close()
