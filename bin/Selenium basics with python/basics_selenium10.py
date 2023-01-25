'''
Handling the Windows tab using selenium webdriver with Python

Basics which is necessary to understand

Every windows has it's own hexadecimal value assign with it ex,(CDwindow-5907D74FC9E6C6E2918AB140D08C34AE) 
using  
        driver.current_window_handler

To switch into within any other tab of the similar webpage we can simply use the same
            
        driver.switch_to.windows(handler)

to get all the windows

        driver.window_handles

Remeber difference between the two .quit() and .close()
    --> quit() terminate the browser
    --> close() terminate the current tab on the browser

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver =webdriver.Chrome(executable_path="chromeDriver.exe")
driver.get("https://demo.automationtesting.in/Windows.html")
clicked_element = driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
time.sleep(2)
print(driver.current_window_handle)
tabs = driver.window_handles
for tab in tabs:
    driver.switch_to.window(tab)
    time.sleep(2)
    print(driver.title)
    driver.close()
driver.quit()



