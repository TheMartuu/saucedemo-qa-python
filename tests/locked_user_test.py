#Locked user login test 

#modules 
#unittest framework 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class Locked_user_login_test(unittest.TestCase):
    def setUp(self):
        """Set up driver as parameter"""
        self.driver = webdriver.Firefox()
    def test_empty_login(self):
        driver = self.driver
        #Get URL
        driver.get("https://www.saucedemo.com/")

        #Get username field and add locked username
        locked_out_user = driver.find_element(By.ID,'user-name')
        locked_out_user.send_keys('locked_out_user')
         #Get password field and add  password  
        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        #Get error message 
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        self.assertTrue(error_msg.is_displayed())

        #Get message in error 
        self.assertIn("Epic sadface: Sorry, this user has been locked out.",error_msg.text)

    def tearDown(self):
        """close browser"""
        self.driver.close()
        
if __name__ == '__main__': 
    unittest.main()