'''
We are trying to interact with the links and mainly simply we can get them using the By function

Let's getting the No of the links, all link text, partial link text so we get hands on find_elements function too.


another ways to find 
(i)  By.LINK_TEXT --> complete text for single element
(ii) By.PARTIAL_LINK_TEXT --> partial text is enough for finding individual work
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome(executable_path="chromeDriver.exe")
driver.get("https://mohitpeshwani.github.io/crazyprogrammer/")
time.sleep(5)
no_of_links = driver.find_elements(By.TAG_NAME,'a')
time.sleep(2)
print("No of the links available in the web page:", len(no_of_links))

#we link to go on the link no 2
no_of_links[2].click()

#printing the assosicate text with the link
for i in no_of_links:
    print(i.text)

#element using LINK_TEXT
print(driver.find_element(By.LINK_TEXT,'mohitpesh23@gmail.com').is_displayed())

#element using LINK_TEXT
print(driver.find_element(By.PARTIAL_LINK_TEXT,'mohitpesh23').is_displayed())

time.sleep(5)
driver.quit()

