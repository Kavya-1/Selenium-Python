import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(executable_path="E:\Drivers\chromedriver_win32 (2)\chromedriver.exe")
# Open url
driver.get("https://www.amazon.in")
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print("============================")
#     for item in cookie:
#         print("Key=", item, "Value=", cookie[item])

# Add new cookie

driver.add_cookie({'name':'myCookie', 'value':'7685959'})
driver.add_cookie({'name':'myANothercookie', 'value':'879689'})
cookies = driver.get_cookies()
print(len(cookies))
# for cookie in cookies:
#     print("============================")
#     for item in cookie:
#         print("Key=", item, "Value=", cookie[item])
driver.delete_cookie(name='myCookie')
time.sleep(2)
print("After deleting")
cookies = driver.get_cookies()
for cookie in cookies:
    print("============================")
    for item in cookie:
        print("Key=", item, "Value=", cookie[item])
print(len(cookies))

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))

driver.close()