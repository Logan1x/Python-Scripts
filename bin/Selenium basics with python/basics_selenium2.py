from selenium import webdriver
import time
driver =webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.github.com")
print(driver.title)
time.sleep(2)
driver.get("https://www.google.com")
print(driver.title)
time.sleep(2)
driver.back()
time.sleep(2)
print("Navigated to the back page: ",driver.title)
driver.forward()
print("Navigrated to the next page: ",driver.title)
