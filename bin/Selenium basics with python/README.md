## Selenium Driver with the Python from scratch with examples

## Need to install
<b>Python<br>
Selenium ------------------> <i>pip instll selenium</i><br>
Chromedriver---------------><i>https://chromedriver.chromium.org/getting-started<i><br>
</b>

<hr>

## Selenium basics 1
 (i)  basics of the selenium web driver small commands<br>
 (ii) minimize and maximise the functionality<br>

<hr>

## Selenium basics 2
Navigation commands mainly use to move previous page(<-) and forward page(->) page
(i) driver.back()<br>
(ii) driver.forward()<br>

<hr>

## Selenium basics 3
Demonstrating the condtional function is_selected, is_enabled, is_displayed() mainly for validation purpose<br>
 (i)   is_enabled()<br>
 (ii)  is_selected()<br>
 (iii) is_displayed()<br>

<hr>

## Selenium basics 4

<b>Demonstrating the Waits in selenium web driver</b><br>

Explicit Wait command, the WebDriver is directed to wait until a certain condition occurs before proceeding with executing the code.
Setting Explicit Wait is important in cases where there are certain elements that naturally take more time to load
<br>
Implicit Wait directs the Selenium WebDriver to wait for a certain measure of time before throwing an exception.
Once this time is set, WebDriver will wait for the element before the exception occurs
<br>

<hr>

## Selenium basics 5
Input Box And Text Box fucntionality using selenium driver <br>

(i) send_keys() to add the message or input into input_box/textarea<br>
(ii) submit button to submit. <br>


<hr>

## Selenium basics 6
In this web page we will select the checkbox and radio types of input 
using <br>
    element.click()<br>
And also check whenever there is a iframe we need to go into iframe using (optional)(Note: we are selecting radio buttons in frame that's why required to go iframe)<br>
  (i)switch_to.frame('frame_id') --> to select the elements in the specific sections<br>
  (ii)switch_to.default_content() --> switch to normal mode always is best practice<br>
  (This two are mostly used in the automation testing perspective. "In safty place like the tracsaction for ex, slack transcation they use nested iframes.)<br>

<hr>

## Selenium basics 7
Lets select from the drop down plane with the help of the selenium web driver command by 3 ways as follow: <br>
Step 1) Select the element using the element = select(driver.find_element())  <br>
Step 2) Select the value using the following three ways  we have <br>
        (i)element.select_by_visible_text("") <br>
        (ii)element.select_by_value("") <br>
        (iii)element.select_by_index() <br>
<hr>

## Selenium basics 8 
'''
We are trying to interact with the links and mainly simply we can get them using the By function <br>

Let's getting the No of the links, all link text, partial link text so we get hands on find_elements function too. <br>


another ways to find 
(i)  By.LINK_TEXT --> complete text for single element <br>
(ii) By.PARTIAL_LINK_TEXT --> partial text is enough for finding individual work <br>
'''

<hr>

## Selenium basics 9 

Let us check how we can handle the alerts and popups on the website using selenium websdrive in python
<br>
we can driver.switch_to.alert()<br>
where multiple things there accept using .accept()<br>
where multiple things there accept using .dismiss() 
<br>
another ways to find <br>
(i)  By.LINK_TEXT --> complete text for single element<br>
(ii) By.PARTIAL_LINK_TEXT --> partial text is enough for finding individual work
'''<br>
<hr>

## Selenium basics 10 
Handling the Windows tab using selenium webdriver with Python<br>

Basics which is necessary to understand.<br>

<hr>

## Selenium basics 11 

handle the scroll in a web page using the python with selenium<br>

<hr>

## Selenium basics 12 

handle the mouse hower or touch on mobile screen actions through the selenium web driver commands<br>


## Selenium basics 13 

Double Click action using mouse handling on python selenium<br>

## Selenium basics 14

perform some more functionality around ActionChain<br>


<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://www.linkedin.com/in/mohitpeshwani/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="mohit peshwani" height="30" width="40" /></a>
<a href="https://instagram.com/coding_nightmare" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="coding_nightmare" height="30" width="40" /></a>
<a href="https://www.figma.com/@mohitpeshwani" target="blank"><img align="center" src="https://logowik.com/content/uploads/images/figma.jpg" alt="mohit peshwani" height="30" width="40" /></a>
</p>
