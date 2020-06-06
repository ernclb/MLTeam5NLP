import requests
from bs4 import BeautifulSoup
r = requests.get('http://google.com')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)