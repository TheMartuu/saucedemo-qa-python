# Sort items test 

#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select 

class Inventory_sort(unittest.TestCase):
    """Creates a class that tests item sorting"""
    def setUp(self): 
        """Set up driver as parameter """
        self.driver = webdriver.Firefox()
    
    def test_sorting_items(self): 
        """Tests if items are sorted from A-Z and to Z-A"""
        driver = self.driver
        driver.get('https://www.saucedemo.com/')

        #Login
        driver.find_element(By.ID,'user-name').send_keys('standard_user')
        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        #Get drop down 
        product_sort = Select(driver.find_element(By.CLASS_NAME,'product_sort_container'))
        product_sort.select_by_value('az')

        #Get product names 
        product_names = driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        names_az = [p.text for p in product_names]

        #Order products Z->A 
        product_sort.select_by_value('za')

        #Get items in reverse order 
        product_names = driver.find_elements(By.CLASS_NAME,'inventory_item_name')
        names_za = [p.text for p in product_names]

        #check if both lists have the reversed order 
        self.assertEqual(names_az,list(reversed(names_za)))

    def tearDown(self):
        """Close browser """
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
