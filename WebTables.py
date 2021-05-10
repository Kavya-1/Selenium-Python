from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro")
driver.switch_to.frame("iframeResult")
rows = driver.find_elements_by_css_selector("table tbody tr")
print("Total number of rows is = ", len(rows))
for row in rows:
    columns = row.find_elements_by_css_selector("td")
    for column in columns:
        print(column.text, end ='               ')
    print()

driver.close()
