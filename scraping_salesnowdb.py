import re

import requests
from bs4 import BeautifulSoup


def abstract_all_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    elems = soup.find_all('a')
    # elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

    urls = [elem.attrs['href'] for elem in elems]
    return urls


if __name__ == '__main__':
    urls = abstract_all_urls('https://xxxxxxxxx/')
    print(len(urls))
    print(urls)