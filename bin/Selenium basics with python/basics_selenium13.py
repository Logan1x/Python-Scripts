'''
Let us check the Double Click action using mouse handling on python selenium

step 1:  We need to import addition Object which is
                ActionChain
step 2:
        Also initilize it using using a variable is always preferable
                action =ActionChain(webdriver)

step 3:
        to perform any Doubleclick
            action.doule_click(element).perform()    ------------> Double click action
            action.context_click(element).perform()  ------------> Right click actions appear

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
element = driver.find_element(By.CSS_SELECTOR,"button[ondblclick='myFunction1()']")
time.sleep(2)
#ActionChains(driver).double_click(element).perform()
ActionChains(driver).context_click(element).perform()

time.sleep(2)
label2 = driver.find_element(By.ID,"field2")
print(label2.get_property)
driver.quit()
