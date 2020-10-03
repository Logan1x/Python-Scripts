from selenium import webdriver
from time import sleep
import filter_contacts

PATH_TO_CHROMEDRIVER = ''

wishingContacts = filter_contacts.filter_contacts("contacts.csv")
driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)
driver.get('https://web.whatsapp.com')
sleep(15)
contacts = dict()

for key, value in wishingContacts.items():
    pre_msg = "SOME PRE SALUTATION MESSAGE"
    post_msg = """
    SOME POST SALUTATION MESSAGE
    """
    input_box = None
    try:
        input_box = driver.find_element_by_css_selector("input[type='text']")
        input_box.click()
        input_box.send_keys(key)
        sleep(1)
        userbox = driver.find_element_by_css_selector("span[title='"+key+"']")
        userbox.click()
        inputbox = driver.find_element_by_css_selector("div[data-tab='1']")
        inputbox.click()
        inputbox.send_keys(pre_msg+value+post_msg)
        send_button = driver.find_element_by_css_selector(
            "span[data-icon='send']")
        send_button.click()
        sleep(1)
    except Exception:
        input_box.clear()
        continue
