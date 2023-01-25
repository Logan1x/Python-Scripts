'''
Input Box And Text Box fucntionality using selenium driver

(i) send_keys() to add the message or input into input_box/textarea
(ii) submit button to submit.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://app.hackthebox.com/login')
driver.maximize_window()
time.sleep(5)
# adding the id/class of input boxs into the variables
login_email = driver.find_element(By.XPATH,"//input[@id='loginEmail']")
password = driver.find_element(By.XPATH,"//input[@id='loginPassword']")
submit_btn = driver.find_element(By.XPATH,"//input[@id='loginPassword']")

# Now we will send the random names, email and message and submit 
login_email.send_keys("automation@gmail.com")
password.send_keys("Ronaldo the GOAT")
submit_btn.submit()
time.sleep(5)
driver.quit()