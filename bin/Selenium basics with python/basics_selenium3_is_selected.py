'''
Demonstrating the condtional function is_selected in this file
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://demoqa.com/radio-button")

# storing elements and detect wheather they are selected or not

selected_button = driver.find_element(By.CSS_SELECTOR,"label[for='yesRadio']")
selected_button2 = driver.find_element(By.CSS_SELECTOR,"label[for='impressiveRadio']")
print(selected_button.is_selected())
driver.quit()
