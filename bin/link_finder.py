
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.youtube.com/playlist?list=PLAwxTw4SYaPkQXg8TkVdIvYv4HfLG7SiH'   # playlist's url you want to scrape links from
driver = webdriver.Chrome(r"C:\Users\gstar\Downloads\chromedriver_win32\chromedriver")  # path of your chrome webdriver
driver.get(url=url)

while True:
    try:
        loadMoreButton = driver.find_element_by_xpath("//button[contains(@aria-label,'Load more')]")  # Xpath of load button
        time.sleep(2)
        loadMoreButton.click()
        time.sleep(10)
    except Exception as e:
        print(e)
        break

all_tr = driver.find_elements_by_tag_name("tr")

list_of_links = []
name = ""
for tag in all_tr:
    i = 2
    temp_name = tag.get_attribute("data-title")
    if temp_name == name:
        while temp_name + " " + str(i) in list_of_links:
            i += 1
        final_name = temp_name + " " + str(i)
    else:
        name = temp_name
        final_name = temp_name
        
    for char in ["/", "*", ":", "?", '"', "|"]:
        final_name = final_name.replace(char, "")
        
    list_of_links.append(final_name)

print('complete')
time.sleep(2)
driver.quit()
