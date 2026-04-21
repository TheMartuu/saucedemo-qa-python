# Log out test 

#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Create Class for test case 
class logout_test(unittest.TestCase): 
    def setUp(self): 
        """Set up driver as parameter """
        self.driver = webdriver.Firefox()
    def test_log_out (self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        #Assert title in page 
        self.assertIn("Swag Labs",driver.title)  

        #Get username field and add value
        username = driver.find_element(By.ID,'user-name')
        username.send_keys('standard_user')
        
        #Get password field and add value 

        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        time.sleep(2)

        #Assert URL change after logging in 
        self.assertIn("inventory.html", driver.current_url)
        
        #Assert that products are displayed 
        products_title = driver.find_element(By.CLASS_NAME, "title")
        self.assertEqual("Products", products_title.text)

        #Click on burger menu and select logout
        driver.find_element(By.ID,'react-burger-menu-btn').click()
        driver.find_element(By.ID,'logout_sidebar_link').click()

        #Assert login button is visible after logout  
        login_button = driver.find_element(By.ID, 'login-button')
        self.assertTrue(login_button.is_displayed())

    def tearDown(self): 
        """Close browser"""
        self.driver.close()

#Execute test: 
if __name__ == '__main__':
    unittest.main()

