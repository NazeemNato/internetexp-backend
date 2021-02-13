from bs4 import BeautifulSoup
import requests
from random import randint

def fffNews(url):
    result = []
    news = []
    header ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        source = requests.get(url ,headers=header).text
        soup = BeautifulSoup(source,'lxml')
        find_container = soup.find('section',class_="listingResultsWrapper news")
        find_news = find_container.find('div',class_="listingResults news")
        for div in find_news.find_all('div',class_='listingResult'):
            for news_text in div.find_all('a',href=True):
                if news_text.text:
                    try:
                        article = news_text.find('p',class_='synopsis').text
                        # news.append(news_text['aria-label'])
                        print(news_text['aria-label'])
                    except:
                        print('Error')

    except Exception as e:
        print(e)
        return []
