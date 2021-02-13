from bs4 import BeautifulSoup
import requests
from random import randint
from .links import *
from .news.fff_news import *


def randomNews():
    header ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    urls = [football_italia,fourfourtwo,mirror,caughtoffside,talksport,tribalfootball]
    for url in urls:
        try:
            if(url['id'] == 0):
                fffNews(url['url'])
        except Exception as e:
            print(e)
