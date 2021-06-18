import requests
import string
from bs4 import BeautifulSoup


def article_scraper():
    url = 'https://www.nature.com/nature/articles'
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    parser = "html.parser"
    soup = BeautifulSoup(r.content, parser)
    articles = soup.find_all('article', class_='u-full-height c-card c-card--flush')
    saved_articles = []
    for article in articles:
        article_type = article.find('span', class_="c-meta__type")
        if article_type.text == 'News':
            link = article.a.get('href')
            para = article.p.text.strip()
            heading = article.find('a').text.strip()
            for i in heading:
                if i in string.punctuation:
                    heading.replace(i, '')
            name = heading.replace(' ', '_')
            file = open(f'{name}.txt', 'wb')
            file.write((str(link)).encode())
            file.write(('Article_name :' + heading).encode())
            file.write(('Article Content :' + para).encode())
            file.close()
            saved_articles.append(name)


# print((link))
# print('Saved Articles :', saved_articles)
article_scraper()
