import re

import requests
from bs4 import BeautifulSoup


def abstract_all_urls(url):
    atag_elems =  fetch_bs_obj(url)
    # elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

    pattern = re.compile('^(?!http).*$')
    urls = []
    for elem in atag_elems:
        path = str(elem.attrs['href']) 
        if pattern.match(path):
            urls.append(path)
            next_atag_elems = fetch_bs_obj(url=path, domain=url)
            for next_elem in next_atag_elems:
                next_url = str(next_elem.attrs['href'])
                if pattern.match(next_url):
                    urls.append(next_url)

    urls = set(urls)

    return urls


def fetch_bs_obj(url: str, domain: str = "") -> None:
    if domain != "":
        url = domain + url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    atag_elems = soup.find_all('a')
    return atag_elems


if __name__ == '__main__':
    urls = abstract_all_urls('https://db.salesnow.jp/')
    print(len(urls))
    print(urls)