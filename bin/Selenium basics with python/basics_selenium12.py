'''
Let'us handle the mouse hower or touch on mobile screen actions through the selenium web driver commands

step 1:  We need to import addition Object which is
                ActionChain
step 2:
        Also initilize it using using a variable is always preferable
                action =ActionChain(webdriver)

step 3:
        to perform any action we need to
                element.move_to().perform()

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver =webdriver.Chrome(executable_path="chromeDriver.exe")
driver.get("https://www.browserstack.com")
action = ActionChains(driver)
time.sleep(3)
product_menu = driver.find_element(By.CSS_SELECTOR,"#product-menu-toggle")
live_submenu = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Live'] div[class='dropdown-link-text']")
action.move_to_element(product_menu).perform()
time.sleep(2)
live_submenu.click()
time.sleep(2)
print("Title include Live: ",driver.title)
driver.quit()