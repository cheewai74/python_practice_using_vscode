from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class FunctionalTestCase(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
       
    def test_there_is_homepage(self):
        self.driver.get("http://localhost:8000")
        # assert driver.page_source.find('install')
        # self.assertIn('install', self.driver.page_source)
        self.assertIn('Enter hash here:', self.driver.page_source)
        
    def test_hash_of_hello(self):
        self.driver.get("http://localhost:8000")
        text = self.driver.find_element_by_id('id_text')
        text.send_keys('hello')
        self.driver.find_element_by_name('submit').click()
        self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.driver.page_source)
         
    def tearDown(self):
        self.driver.quit()
