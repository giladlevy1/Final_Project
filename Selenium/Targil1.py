from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException

driver1 = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver1.implicitly_wait(10) #Waiting time to driver respone
driver1.maximize_window() #Makes the page on whole screen

driver1.get("https://www.phptravels.net/admin")

driver1.find_element_by_css_selector("input[placeholder='Email']").send_keys("admin@phptravels.com")
driver1.find_element_by_css_selector("input[placeholder='Password']").send_keys("demoadmin")
driver1.find_element_by_css_selector("button[class='btn btn-primary btn-block ladda-button fadeIn animated btn-lg']").click()
sleep(3)

Dashboard_text = driver1.find_element_by_css_selector("#social-sidebar-menu > li:nth-child(1) > a > strong").text
if Dashboard_text == "DASHBOARD":
    print("success")
else:
    print("fail")

driver1.find_element_by_css_selector("#logout > a > strong").click()

sleep(2)
driver1.close()