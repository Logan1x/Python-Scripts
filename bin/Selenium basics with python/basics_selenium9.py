'''
Let us check how we can handle the alerts and popups on the website using selenium websdrive in python

we can driver.switch_to.alert()
where multiple things there accept using .accept()
where multiple things there accept using .dismiss()

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path= "chromeDriver.exe")
driver.get("https://demo.automationtesting.in/Alerts.html")
alert_box = driver.find_element(By.CSS_SELECTOR,".btn.btn-danger")
alert_box.click()
time.sleep(2)
# Switching to the ok using accept() else we can use the dismiss() for cancle purpose if available
driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.default_content()

time.sleep(2)
driver.quit()


