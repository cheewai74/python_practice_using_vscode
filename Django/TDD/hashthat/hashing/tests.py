from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from .forms import HashForm
from .models import Hash
import hashlib 

# class FunctionalTestCase(TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
       
#     def test_there_is_homepage(self):
#         self.driver.get("http://localhost:8000")
#         # assert driver.page_source.find('install')
#         # self.assertIn('install', self.driver.page_source)
#         self.assertIn('Enter hash here:', self.driver.page_source)
        
#     def test_hash_of_hello(self):
#         self.driver.get("http://localhost:8000")
#         text = self.driver.find_element_by_id('id_text')
#         text.send_keys('hello')
#         self.driver.find_element_by_name('submit').click()
#         self.assertIn('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', self.driver.page_source)
         
#     def tearDown(self):
#         self.driver.quit()
        
        
class UnitTestCase(TestCase):
    
    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')
        
    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())
        
    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824', text_hash.upper())
        
    def test_hash_object(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824'
        hash.save()
        pulled_hash = Hash.objects.get(hash='2CF24DBA5FB0A30E26E83B2AC5B9E29E1B161E5C1FA7425E73043362938B9824')
        self.assertEqual(hash.text, pulled_hash.text)
        
        
        
        