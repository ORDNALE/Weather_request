# pip install bs4
# pip install resquests
from bs4 import BeautifulSoup
import requests

search = 'clima cuiaba'

url = f'https://www.google.com/search?q={search}'

r = requests.get(url)
s = BeautifulSoup(r.text, 'html.parser')
info = s.find('div', class_='BNeawe').text

print(info)
