from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_css_selector("input#txtUsername").send_keys("Admin")
driver.find_element_by_css_selector("input#txtPassword").send_keys("admin123")
driver.find_element_by_css_selector("input#btnLogin").submit()

admin = driver.find_element_by_css_selector("a#menu_admin_viewAdminModule")
userManagement = driver.find_element_by_css_selector("a#menu_admin_UserManagement")
users = driver.find_element_by_css_selector("a#menu_admin_viewSystemUsers")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click(users).perform()


driver.close()