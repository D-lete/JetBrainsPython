import requests
from bs4 import BeautifulSoup
import json


class WebScraper:

    def __init__(self):
        r = requests.get(input('Input the URL:\n> '), headers={'Accept-Language': 'en-US,en;q=0.5'})
        if not r or 'title' not in r.url:
            print('Invalid movie page!')
        elif r:
            parser = "html.parser"
            soup = BeautifulSoup(r.text, parser)
            a = {'title': soup.title.string, 'description': soup.find('p').getText()}
            print(a)


WebScraper()
