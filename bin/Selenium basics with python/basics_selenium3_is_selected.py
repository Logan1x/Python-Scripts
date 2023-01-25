'''
Demonstrating the condtional function is_selected in this file
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://demoqa.com/radio-button")

# storing the two elements one to select and another non-selected to demonstrate true and false

selected_button = driver.find_element(By.CSS_SELECTOR,"label[for='yesRadio']")
selected_button2 = driver.find_element(By.CSS_SELECTOR,"label[for='impressiveRadio']")
driver.click(selected_button)
print("Expected to get the element is selected to be true\n actuall result: ",selected_button.is_selected() )
print("Expected to get the element is selected to be false\n actuall result: ",selected_button2.is_selected() )

