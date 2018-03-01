from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleepfrom selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import getpass

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print("facebook opened...")
time.sleep(2)
Email = raw_input("Enter your Email ID:")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(Email)
print("Email Id entered...")
password1 = getpass.getpass("Enter your Facebook password: ")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(password1)
print("Password entered...")
button = driver.find_element_by_xpath("//input[@id='u_0_r']")
button.click()
print("signed in")
time.sleep(7)
inputbox = driver.find_element_by_css_selector("span._5qtp")
inputbox.click()
time.sleep(3)
Text = raw_input("\tWhats on your mind? Enter here: \n")
text = driver.find_element_by_css_selector("#composer_text_input_box")
text.click()
text.send_keys(Text)
postbutton = driver.find_element_by_xpath("//*[text()='Post']")
postbutton.click()
time.sleep(10)
driver.close()

# Thank You Stackoverflow and Jio for help
