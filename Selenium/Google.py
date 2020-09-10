from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver1 = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")

driver1.get("http://www.google.com")

driver1.implicitly_wait(5) #Waiting time to driver respone
driver1.maximize_window() #Makes the page on whole screen

search_element = driver1.find_element_by_name("q")
search_element.send_keys("cats" + Keys.ENTER) #Writes "cats" inside the searchbar,
                                              # Keys.ENTER = "ENTER" Key from the keyboard.

sleep(2)

driver1.close()