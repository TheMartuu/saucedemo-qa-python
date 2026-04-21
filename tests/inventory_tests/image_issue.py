#Image issue: check that all pictures are the same 

#modules
#unittest framework
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Image_issue(unittest.TestCase): 
    """Checks that all images are the same (Visual issue)"""
    def setUp(self): 
        """Set up driver as parameter """
        self.driver = webdriver.Firefox()
    def test_searchfortext (self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        #Assert title in page 
        self.assertIn("Swag Labs",driver.title)  

        #Get username field and add value
        username = driver.find_element(By.ID,'user-name') 
        username.send_keys('problem_user') #log in as problem user 
        
        #Get password field and add value 
        password = driver.find_element(By.ID,'password')
        password.send_keys('secret_sauce')
        password.send_keys(Keys.ENTER)

        # Get all images in page 
        images = driver.find_elements(By.CLASS_NAME, "inventory_item_img")

        # Get src from images 
        image_sources = [img.get_attribute("src") for img in images if img.get_attribute("src") is not None]

        print(image_sources)  


        # Check all src are equal 
        self.assertTrue(all(src == image_sources[0] for src in image_sources))     

    def tearDown(self): 
        """Close browser"""
        self.driver.close()

#Execute test: 
if __name__ == '__main__':
    unittest.main()
