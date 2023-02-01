'''
In this web page we will select the checkbox and radio types of input 
using 
    element.click()
And also check whenever there is a iframe we need to go into iframe using (optional)(Note: we are selecting radio buttons in frame that's why required to go iframe)
  (i)switch_to.frame('frame_id') --> to select the elements in the specific sections
  (ii)switch_to.default_content() --> switch to normal mode always is best practice
  (This two are mostly used in the automation testing perspective. "In safty place like the tracsaction for ex, slack transcation they use nested iframes.)


'''

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

#Switching to iframe with id you can even use iframe_name
driver.switch_to.frame('iframeResult')

#getting the locators of the elements
html_selector = driver.find_element(By.XPATH, "//input[@id='html']")
css_selector = driver.find_element(By.XPATH, "//input[@id='css']")
js_selector = driver.find_element(By.XPATH, "//input[@id='javascript']")

#Selected the element 
html_selector.click()

# html selector should give the true and other will be false
print(html_selector.is_selected())
print(css_selector.is_selected())
print(js_selector.is_selected())

#Switching to normal window format
driver.switch_to.default_content()
driver.quit()


