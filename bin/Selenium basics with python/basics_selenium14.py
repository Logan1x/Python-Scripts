'''
Let us perform some more functionality around ActionChain

 Drag and Drop -->   we can simple drag and drop the elements using 
                        action.drag_and_drop(element_source, element_target).perform()



'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
element = driver.find_element(By.CSS_SELECTOR,"button[ondblclick='myFunction1()']")
time.sleep(2)
action =ActionChains(driver)
drag = driver.find_element(By.ID,"draggable")
to_drop = driver.find_element(By.ID,"droppable")
action.drag_and_drop(drag,to_drop).perform()
time.sleep(2)
driver.maximize_window()
driver.save_screenshot("dragAnddrop.png")
driver.quit()
