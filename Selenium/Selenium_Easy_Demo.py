from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver1 = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver1.implicitly_wait(10) #Waiting time to driver respone
driver1.maximize_window() #Makes the page on whole screen

driver1.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
try:
    driver1.find_element_by_id("at-cv-lightbox-close").click()  #click X on pop messagge.
except NoSuchElementException:
    pass

driver1.find_element_by_css_selector("input[placeholder='Please enter your Message']").send_keys("my message")
#write in css selector the specified css selector type. - this case, placeorder.

driver1.find_element_by_css_selector("button[onclick='showInput();']").click() #in html search - button[onclick='showInput();']
sleep(2)

driver1.close()