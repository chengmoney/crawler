import requests
from bs4 import BeautifulSoup
import bs4


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return ''


def get_date(html):
    soup = BeautifulSoup(html, 'html.parser')
    for ht in soup.find('tbody').children:
        if isinstance(ht, bs4.element.Tag):
            data = ht('td')


def print_date(data):
    pass


def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = get_html(url)
    data = get_date(html)
    print_date(data)


