from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
from time import sleep

class Test_AOS(TestCase):

    def setUp(self):
        print("SetUP:")
        self.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")

    def tearDown(self):
        self.driver.close()
        print("teardown ^")

    def test_search_in_python_org(self):
        driver1 = self.driver
        driver1.get("http://www.python.org")

        driver1.implicitly_wait(5) #Waiting time to driver respone
        driver1.maximize_window() #Makes the page on whole screen
        sleep(2) #2 sec sleep command

        self.assertIn("Python",driver1.title)
        elem1 = driver1.find_element_by_name("q")
        elem1.send_keys("pycon")
        elem1.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver1.page_source)
