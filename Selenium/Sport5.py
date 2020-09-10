from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver1 = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
driver1.implicitly_wait(5) #Waiting time to driver respone
driver1.maximize_window() #Makes the page on whole screen

driver1.get("https://www.sport5.co.il/Homepage.aspx?FolderId=890")

driver1.find_element_by_id("83-top-menu").click()
#find html element by ID, and click it - world football
sleep(1)

driver1.find_element_by_css_selector("#header > div > div.add-nav-liga > ul > li:nth-child(1) > a").click()
#find html element by selector, and click it - champions league
sleep(1)

spanish_league = driver1.find_element_by_css_selector("#header > div > div.add-nav-liga > ul > li:nth-child(3) > a")
print(spanish_league.text) #web element variable by the type of text

driver1.close()