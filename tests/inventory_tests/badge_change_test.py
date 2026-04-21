#Change in cart badge test 

#modules 
#unittest framework 
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

class Disappearing_Badge_Test(unittest.TestCase):
    """Checks if a badge disappears when deleting a product from cart"""
    def setUp(self):
        """Set up webdriver"""
        self.driver = webdriver.Firefox()

    def test_disappearing_badge(self):
        """Test disappearing badge when deleting a product from cart"""     
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

        #click on cart and display items
        cart_items = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
        cart_items.click()

        #click on remove button 
        remove_button = driver.find_element(By.XPATH,'//*[@id="remove-sauce-labs-backpack"]')
        remove_button.click()

        #Assert that cart button does not have any value 
        cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(0, len(cart_badge))

    def tearDown(self):
        """Close browser """
        self.driver.close()


if __name__ == '__main__':
    unittest.main()