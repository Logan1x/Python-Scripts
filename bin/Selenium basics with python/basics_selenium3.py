'''
conditional commands are used to check wheater the fuction is working fine or not properly (Validation purpose)
(i) is_enable()
(ii) is_displayed()
(iii) is_selected() 

prior this we need to select the selector to check for the element to use
using css selector and xpath selector
'''
from selenium import webdriver
from selenium.webdriver.common.by import By # need to use this selector 
driver = webdriver.Chrome(executable_path="chromedriver.exe")


'''
Using the CSS_selector we are selecting input and checking wheather it's dispalyed properly or not 
Executed : 1)is_displayed()  2)is_enabled()

'''
driver.get("https://www.google.com/")
 
element = driver.find_element(By.CSS_SELECTOR,"input[title='Search']")
 
print(element.is_displayed())
print(element.is_enabled())

