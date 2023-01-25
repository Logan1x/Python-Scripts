'''
Lets select from the drop down plane with the help of the selenium web driver command by 3 ways as follow:
Step 1) Select the element using the element = select(driver.find_element())
Step 2) Select the value using the following three ways  we have
        (i)element.select_by_visible_text("")
        (ii)element.select_by_value("")
        (iii)element.select_by_index()
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="chromeDriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
link_first = Select(driver.find_element(By.ID,'RESULT_RadioButton-9'))

#link_first.select_by_visible_text("Afternoon")

#link_first.select_by_value("Radio-2")

link_first.select_by_index(2)

time.sleep(2)

driver.quit()


