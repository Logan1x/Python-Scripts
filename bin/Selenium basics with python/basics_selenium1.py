
'''
Simple hands on the selenium with help of python library

'''
from selenium import webdriver
driver = webdriver.Chrome(executable_path="chromedriver.exe")    # to use the functionality of the web driver we need to create the object of the drive with specific browser which we want to use
driver.get("https://mohitpeshwani.github.io/crazyprogrammer/")   #to load the target url we user webdriver.get("url") to load it
driver.maximize_window() #to maxiumize the windows
driver.minimize_window() #to minimize the windows
print(driver.title) #to get the exact title of the page we can use the webdriver.title
driver.quit() # to close the automation windows