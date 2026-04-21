#  Add item to cart test 

#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Add_to_cart(unittest.TestCase):
    """Creates a class that tests if an item is added to cart """
    def setUp(self):
        """Set up driver"""
        self.driver = webdriver.Firefox()
    
    def test_add_item_to_cart(self): 
        """Tests if item is added to cart"""
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

        #Get cart badge 
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

        #Assert value in cart badge 
        self.assertEqual("1",cart_badge.text)
    def tearDown(self):
        """Close browser """
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

