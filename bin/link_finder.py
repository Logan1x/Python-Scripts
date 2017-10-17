
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# url = 'https://www.youtube.com/playlist?list=PLAwxTw4SYaPkQXg8TkVdIvYv4HfLG7SiH'   # playlist's url you want to scrape links from
# driver = webdriver.Chrome(r"C:\Users\gstar\Downloads\chromedriver_win32\chromedriver")  # path of your chrome webdriver
# driver.get(url=url)

# while True:
#     try:
#         loadMoreButton = driver.find_element_by_xpath("//button[contains(@aria-label,'Load more')]")  # Xpath of load button
#         time.sleep(2)
#         loadMoreButton.click()
#         time.sleep(10)
#     except Exception as e:
#         print(e)
#         break

# all_tr = driver.find_elements_by_tag_name("tr")

# list_of_links = []
# name = ""
# for tag in all_tr:
#     i = 2
#     temp_name = tag.get_attribute("data-title")
#     if temp_name == name:
#         while temp_name + " " + str(i) in list_of_links:
#             i += 1
#         final_name = temp_name + " " + str(i)
#     else:
#         name = temp_name
#         final_name = temp_name
        
#     for char in ["/", "*", ":", "?", '"', "|"]:
#         final_name = final_name.replace(char, "")
        
#     list_of_links.append(final_name)

# print('complete')
# time.sleep(2)
# driver.quit()






# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep

# def _execute_script(email, password, count):


#     # driver = webdriver.PhantomJS()
#     driver = webdriver.Chrome(r"C:\Users\gstar\Downloads\chromedriver_win32\chromedriver")
#     driver.get('https://www.facebook.com')

#     email_ID = driver.find_element_by_id('email')
#     pass_ID = driver.find_element_by_id('pass')


#     email_ID.send_keys(email)
#     pass_ID.send_keys(password)
#     pass_ID.send_keys(Keys.ENTER)
#     sleep(5)

#     for i in range(0,count):
#         driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
#         sleep(1)
	
#     sleep(5)

#     driver_tags = driver.execute_script('return document.getElementsByClassName("scaledImageFitWidth img")')

#     driver_img_list = {
#     'src' : [x.get_attribute('src') for x in driver_tags],
#     'alt' : [x.get_attribute('alt') for x in driver_tags],
#     }

#     driver.quit()

#     return driver_img_list


# def _check_memes(driver_img_list, verbose):

# 	alt_list = driver_img_list['alt']
# 	if len(alt_list) == 0:
# 		print("Error getting newsfeed. Possibly username or password was incorrect")
# 		return

# 	output = "\n{} memes in your newsfeed.\n{} total images in your newsfeed.\n{}% memes in newsfeed.\n"
# 	count = 0

# 	for key,alt in enumerate(alt_list):
# 		if "text" in alt or "meme" in alt :
# 			count += 1
# 			if verbose:
# 				print(driver_img_list['src'][key]) 

# 	print(output.format(count,len(alt_list),round(count*100/len(alt_list),2)))

# driver_img_list = _execute_script("prashantgoyal38@yahoo.com", "worldisrotten", 5)
# _check_memes(driver_img_list, 1)
