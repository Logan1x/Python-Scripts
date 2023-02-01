'''
Explicit Wait command, the WebDriver is directed to wait until a certain condition occurs before proceeding with executing the code.
Setting Explicit Wait is important in cases where there are certain elements that naturally take more time to load

Implicit Wait directs the Selenium WebDriver to wait for a certain measure of time before throwing an exception.
Once this time is set, WebDriver will wait for the element before the exception occurs
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://mohitpeshwani.github.io/crazyprogrammer/")
try:
    # wait 10 extra seconds before looking for element until it found my website image
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img[src='./images/man12.png']"))
    )
    print(element.is_displayed()) # should return true
    print("Demontrating the explicit wait ")
finally:
    driver.quit()