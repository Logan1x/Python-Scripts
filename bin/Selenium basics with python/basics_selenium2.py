'''
Navigation commands mainly use to move previous page(<-) and forward page(->) page
(i) driver.back()
(ii) driver.forward()

'''

from selenium import webdriver
import time
driver =webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.github.com")
print(driver.title)
time.sleep(2) # to wait for 2 seconds
driver.get("https://www.google.com")
print(driver.title)
time.sleep(2)
driver.back() # it goes once action backward
time.sleep(2)
print("Navigated to the back page: ",driver.title)
driver.forward() # it goes to the next action page if gone 
print("Navigrated to the next page: ",driver.title)
driver.quit()
