#  Sum of items price testing 
#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Add_to_cart(unittest.TestCase):
    """Creates a class that tests if items prices are summed up correctly"""
    def setUp(self):
        """Set up driver"""
        self.driver = webdriver.Firefox()
    
    def test_add_item_to_cart(self): 
        """Tests if item is added to cart and summed up when checking out"""
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        #Log into website 
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        #Get first item 
        first_item = driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div')
        first_item.click()

        #Click on Add to cart button 
        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, "[data-test^='add-to-cart']")
        add_to_cart_buttons[0].click()

        #click back 
        driver.find_element(By.ID,'back-to-products').click()

        #Get second item 
        second_item = driver.find_element(By.XPATH,'//*[@id="item_0_title_link"]/div')
        second_item.click()

        #Click on Add to cart button 
        add_to_cart_buttons = driver.find_elements(By.CSS_SELECTOR, "[data-test^='add-to-cart']")
        add_to_cart_buttons[0].click()

        #Go to shopping cart 
        shopping_cart = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
        shopping_cart.click()

        #get inventory 
        prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        first_item_price = float(prices[0].text.replace("$", ""))
        second_item_price = float(prices[1].text.replace("$", ""))

        #checkout
        driver.find_element(By.ID,'checkout').click()
        
        #fill checkout data 
        driver.find_element(By.ID,'first-name').send_keys('test')
        driver.find_element(By.ID,'last-name').send_keys('case')
        driver.find_element(By.ID,'postal-code').send_keys('1234')
        driver.find_element(By.ID,'continue').click()

        #Assert sum 
        price_total = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        total_text = price_total.text.replace("Item total: $", "")
        self.assertEqual(float(total_text), first_item_price + second_item_price)
        
    def tearDown(self):
        """Close browser """
        self.driver.close()


if __name__ == '__main__':
    unittest.main()