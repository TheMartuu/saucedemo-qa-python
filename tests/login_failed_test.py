# Failed Log in test 

#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Create Class for test case 
class using_unittest1(unittest.TestCase): 
    def setUp(self): 
        """Set up driver as parameter """
        self.driver = webdriver.Firefox()
    def test_searchfortext (self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        #Get username field and add wrong username
        username = driver.find_element(By.ID,'user-name')
        username.send_keys('wrong_user')
        #Get password field and add value 
        password = driver.find_element(By.ID,'password')
        password.send_keys('wrong_password')
        password.send_keys(Keys.ENTER)

        #Get error message by CSS Selector 
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        self.assertTrue(error_msg.is_displayed())

        #Get message in error 
        self.assertIn("Epic sadface: Username and password do not match any user in this service", error_msg.text)

    def tearDown(self): 
        """close browser"""
        self.driver.close()

if __name__ == '__main__':
    unittest.main()