import requests
from bs4 import BeautifulSoup

url = 'https://www.nature.com/nature/articles'
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
parser = "html.parser"
soup = BeautifulSoup(r.content, parser)
print(soup.find_all('<div>'))
