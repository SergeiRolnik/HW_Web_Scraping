import requests
from bs4 import BeautifulSoup
import datetime

BASE_URL = 'https://habr.com'
HEADERS = {'User-Agent': 'Chrome/39.0.2171.95'}
KEYWORDS = ['дизайн', 'фото', 'SQL', 'Python']
NUMBER_OF_PAGES = 10

for page in range(1, NUMBER_OF_PAGES + 1):

    res = requests.get(BASE_URL + '/page' + str(page), headers=HEADERS)
    soup = BeautifulSoup(res.text, features='html.parser')
    articles = soup.find_all(class_='tm-article-snippet')

    for article in articles:

        date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['datetime']
        date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ').date()
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        title = article.find(class_='tm-article-snippet__title-link').find('span').text
        hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
        hubs = [hub.find('span').text for hub in hubs]

        if not set(hubs).isdisjoint(set(KEYWORDS)):
            print('---------------------------------------')
            print(f'Date: {date}\nTitle: {title}\nURL: {BASE_URL + href}')
            print(f'Hubs: {", ".join(hubs)}')