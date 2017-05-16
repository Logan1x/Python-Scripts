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

driver = webdriver.Firefox()
driver.get('http://c.mi.com/')
print("Opened MI community...")
signin = driver.find_element_by_css_selector(".sign-action > a:nth-child(1)")
signin.click()
time.sleep(10)
email = driver.find_element_by_xpath("//input[@id='username' or @name='email']")
email.send_keys('+919413752866')
print("Email Id entered...")
password = driver.find_element_by_xpath("//input[@id='pwd']")
password.send_keys('L0g@n!*x')
print("Password entered...")
button = driver.find_element_by_xpath("//input[@id='login-button']")
button.click()
print('login successfully')
time.sleep(7)
threadbutton = driver.find_element_by_css_selector(".thread-box > h4:nth-child(1) > a:nth-child(2)")
threadbutton.click()
print("clicked")
'''time.sleep(15)
statusbox1 = driver.find_element_by_css_selector("#fid")
statusbox1.click()'''
time.sleep(2)
selectforum = Select(driver.find_element_by_name('fid'))
'''all_options = [o.get_attribute(41) for o in select.options]

for x in all_options:
    select.select_by_value(x)
    time.sleep(3)'''
selectforum.select_by_value('41')
print("done")
time.sleep(8)
selecttag = Select(driver.find_element_by_name('typeid'))
selecttag.select_by_value('62')
print("Again done")

title = driver.find_element_by_css_selector("#subject")
title.send_keys('Bot Typing Here....')
time.sleep(5)
#statusbox4 = driver.find_elements_by_class_name('area')
#select2 = Select(driver.find_element_by_id('e_iframe'))
#a = select2.find_element_by_css_selector("#subject")

#a.send_keys('Thanks for listening from my bot..')
print('only selected')
submit = driver.find_element_by_css_selector(".btn-orange")

print('selected')
