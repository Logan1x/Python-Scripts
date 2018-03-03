from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import getpass

driver = webdriver.Firefox()
driver.get('http://c.mi.com/')
print("Opened MI community...")
signin = driver.find_element_by_css_selector(".sign-action > a:nth-child(1)")
signin.click()
time.sleep(10)
email = driver.find_element_by_xpath(
    "//input[@id='username' or @name='email']")
email.send_keys('Email id')
print("Email Id entered...")
password = driver.find_element_by_xpath("//input[@id='pwd']")
password_input = getpass.getpass("Enter your password:")
password.send_keys(password_input)
print("Password entered...")
button = driver.find_element_by_xpath("//input[@id='login-button']")
button.click()
print('login successfully')
time.sleep(7)
threadbutton = driver.find_element_by_css_selector(
    ".thread-box > h4:nth-child(1) > a:nth-child(2)")
threadbutton.click()
print("clicked on new thread button")
time.sleep(2)
selectforum = Select(driver.find_element_by_name('fid'))

selectforum.select_by_value('41')
print("Forum selected")
time.sleep(8)
selecttag = Select(driver.find_element_by_name('typeid'))
selecttag.select_by_value('62')
print("Catagory selected")

title = driver.find_element_by_css_selector("#subject")
title.send_keys('Bot Typing Here....')
print('Title Entered  waiting for your contant')
time.sleep(10)
submit = driver.find_element_by_css_selector(".btn-orange")
submit.click()
print('submitted')
