'''
Let's check who we can handle the scroll in a web page using the python with selenium

Simplest wait is to execute the js using the 
        driver.execute_script("windows.scrollBy(0,500))

    Note:  we can execute javascript using 
            (1) driver.execute_script("","")
            (2) driver.execute_async_scipt("","")


'''

from selenium import webdriver
import time
driver =webdriver.Chrome(executable_path="chromeDriver.exe")
driver.get("https://mohitpeshwani.github.io/crazyprogrammer/")
time.sleep(3)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(3)
driver.quit()
