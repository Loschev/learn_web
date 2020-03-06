import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False


def get_bdva_news():
    html = get_html('https://bdva.ru/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='fat-event-sc').findAll('div', class_='list-skin-01')
        result_news = []
        for news in all_news:
            city = news.find('a').text
            city = ' '.join(city.split())
            url = news.find('a')['href']
            time = news.find('div', class_='fat-event-start').text
            time = ' '.join(time.split())
            place = news.find('span', class_='fat-event-location').text
            place = ' '.join(place.split())
            result_news.append({
                'city': city,
                'url': url,
                'time': time,
                'place': place
            })
        return result_news
    return False
