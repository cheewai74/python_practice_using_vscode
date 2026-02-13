'''
Extract information from websites
'''

import requests
from bs4 import BeautifulSoup

reponse = requests.get('http://google.com')
soup = BeautifulSoup(reponse.text, 'html.parser')
print(soup.title.text)