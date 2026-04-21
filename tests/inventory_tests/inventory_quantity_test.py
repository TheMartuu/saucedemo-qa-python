# Log in test 

#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Inventory_test(unittest.TestCase):
    """Creates a class that tests hoy many inventory items are displayed on page"""
    def setUp(self): 
        """Set up driver as parameter """
        self.driver = webdriver.Firefox()

    def test_displayed_inventory(self): 
        """Tests if 6 inventory items are displayed on page"""
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        #Login
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        #get products and get quantity 
        product_items = driver.find_elements(By.CLASS_NAME,'inventory_item')
        self.assertEqual(6,len(product_items))

    def tearDown(self):
        """Close browser """
        self.driver.close()

if __name__ == '__main__':
    unittest.main()