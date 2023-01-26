'''
When performing API testing we manily work on the cookies and determine 
So simple things around the cookies are demonstrate which are manily used by QA/Developer during building the website

(i)     driver.get_cookies() ---------------------------------------------------->  Get all the cookies properities
(ii)    driver.get_cookie("name") ----------------------------------------------->  Get individual cookies 
(iii)   driver.add_cookie({"name":"string_value", "value": "string_value"})------>  Injecting the cookies in current driver from coding point of view
(iv)    driver.delete_all_cookies() --------------------------------------------->  Deleting all the cookies
(v)     driver.delete_cookie(name)----------------------------------------------->  Deleting individual cookie

'''



from selenium import webdriver
from selenium.webdriver.common.by   import By
import time
driver =webdriver.Chrome(executable_path="chromeDriver.exe")
driver.get("https://www.linkedin.com/in/mohit-peshwani/")
cookies = driver.get_cookies()
# get all the cookies
# print(cookies)  --------------------> print all the cookies with list not looks good uncomment it for better understanding while performing
driver.add_cookie({"name":"python","value":"mohit"})

for cookie in cookies:
    print(cookie)
time.sleep(2)

cookies = driver.delete_all_cookies()
print(driver.get_cookies())
driver.quit()
