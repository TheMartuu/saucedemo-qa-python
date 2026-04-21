#Empty password test 

#modules 
#unittest framework 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest

class Empty_login_test(unittest.TestCase):
    def setUp(self):
        """Set up driver as parameter"""
        self.driver = webdriver.Firefox()
    def test_empty_login(self):
        driver = self.driver
        #Get URL
        driver.get("https://www.saucedemo.com/")

        #Get username field and add valid username
        valid_username = driver.find_element(By.ID,'user-name')
        valid_username.send_keys('problem_user')
         #Get password field and add empty password  
        empty_password = driver.find_element(By.ID,'password')
        empty_password.send_keys('')
        empty_password.send_keys(Keys.ENTER)

        #Get error message 
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        self.assertTrue(error_msg.is_displayed())

        #Get message in error 
        self.assertIn("Epic sadface: Password is required",error_msg.text)

    def tearDown(self):
        """close browser"""
        self.driver.close()
        
if __name__ == '__main__': 
    unittest.main()