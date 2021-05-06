import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

elements = driver.find_elements_by_css_selector("input[type='text']")

elements.__getitem__(1).send_keys("Kavya")
elements.__getitem__(2).send_keys("A S")
elements.__getitem__(3).send_keys("9876543210")
elements.__getitem__(4).send_keys("India")
elements.__getitem__(5).send_keys("Bengaluru")
driver.find_element_by_css_selector("input[type='email']").send_keys("askavya19@gmail.com")


gender = driver.find_element_by_css_selector("input[id=RESULT_RadioButton-7_1]")

driver.execute_script("arguments[0].click();", gender)
# gender.click()

time.sleep(2)
if driver.find_element_by_xpath("//tr[1]/td/input[@type='checkbox']").is_selected():
    print("Already selected")
else:
    day = driver.find_element_by_xpath("//tr[1]/td/input[@type='checkbox']")
    driver.execute_script("arguments[0].click();", day)

select = Select(driver.find_element_by_id("RESULT_RadioButton-9"))
select.select_by_visible_text("Morning")
options = select.options
print(len(options))

for option in options:
    print(option.text)

driver.find_element_by_css_selector("input#RESULT_FileUpload-10").send_keys("C://Users//Kavya//Pictures//Capture.PNG")

driver.find_element_by_css_selector("input[name='Submit']").submit()

time.sleep(5)

driver.close()