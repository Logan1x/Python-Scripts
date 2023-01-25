'''
Explicit Wait command, the WebDriver is directed to wait until a certain condition occurs before proceeding with executing the code.
Setting Explicit Wait is important in cases where there are certain elements that naturally take more time to load

Implicit Wait directs the Selenium WebDriver to wait for a certain measure of time before throwing an exception.
Once this time is set, WebDriver will wait for the element before the exception occurs
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://mohitpeshwani.github.io/crazyprogrammer/")
#implicity waiting for the 10 seconds
driver.implicitly_wait(10)
#element will check after the 10 seconds of wait
element=driver.find_element(By.XPATH,"//div[@class=' hero flex flex-1 items-center justify-between ']//img[1]") #using xpath selector to get the element 
print(element.is_displayed())
driver.quit() 
