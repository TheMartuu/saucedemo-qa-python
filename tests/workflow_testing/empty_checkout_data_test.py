#  Empty checkout testing
#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Empty_checkout(unittest.TestCase):
    """Creates a class that tests if an item is added to cart """
    def setUp(self):
        """Set up driver"""
        self.driver = webdriver.Firefox()
    
    def test_empty_checkout(self): 
        """Tests if empty checkout cannot be done"""
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        #Log into website 
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        #Get item 
        item = driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
        item.click()

        #Click on Add to cart button 
        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, "[data-test^='add-to-cart']")
        add_to_cart_buttons[0].click()

        #click on shopping cart 
        shopping_cart = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
        shopping_cart.click()

        #click on checkout 
        driver.find_element(By.ID, 'checkout').click()
        time.sleep(2)

        #Fill in empty data
        driver.find_element(By.ID,'continue').click()

        #Assertions for first name 
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
        self.assertEqual("Error: First Name is required",error_message.text)
        driver.find_element(By.ID,'first-name').send_keys('test')
        driver.find_element(By.ID,'continue').click()
        self.assertEqual("Error: Last Name is required",error_message.text)
        driver.find_element(By.ID,'last-name').send_keys('case')
        driver.find_element(By.ID,'continue').click()
        self.assertEqual("Error: Postal Code is required",error_message.text)
        
    def tearDown(self):
        """Close browser """
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
