#  Multiple items checkout - assert badge quantity and checkou message  
#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Complete_Workflow(unittest.TestCase):
    """Creates a class that tests if an item is added to cart """
    def setUp(self):
        """Set up driver"""
        self.driver = webdriver.Firefox()
    
    def test_add_item_to_cart(self): 
        """Tests if item is added to cart.
        Tests badge count when adding items to cart 
        Tests total sum of the items price"""
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        #Log into website with standard user 
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        #Save prices and add to cart
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        expected_total = 0
        for product in products[:3]:
            price = product.find_element(By.CLASS_NAME, "inventory_item_price")
            expected_total += float(price.text.replace("$", ""))
            product.find_element(By.CSS_SELECTOR, "[data-test^='add-to-cart']").click()
        

        #click on shopping cart 
        shopping_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
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

        # Assert subtotal
        subtotal = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        actual_total = float(subtotal.text.replace("Item total: $",""))
        self.assertEqual(expected_total, actual_total)

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
