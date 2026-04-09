#  Complete Workflow testing from login to checkout 
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

        #click on shopping cart 
        shopping_cart = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
        shopping_cart.click()

        #click on checkout 
        checkout = driver.find_element(By.NAME,'checkout')
        checkout.click()

        #Fill in name, last name and zip code 
        driver.find_element(By.ID,'first-name').send_keys('test')
        driver.find_element(By.ID,'last-name').send_keys('case')
        driver.find_element(By.ID,'postal-code').send_keys('1234')
        continue_button = driver.find_element(By.ID,'continue')
        continue_button.click()

        #Click on finish 
        finish_button = driver.find_element(By.ID,'finish')
        finish_button.click()

        #Assert complete header and text 
        complete_header = driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2')
        complete_text = driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/div')
        self.assertEqual('Thank you for your order!',complete_header.text)
        self.assertEqual('Your order has been dispatched, and will arrive just as fast as the pony can get there!',complete_text.text)


    def tearDown(self):
        """Close browser """
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
