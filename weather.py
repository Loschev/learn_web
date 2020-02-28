import requests

def weather_by_city(city_name):
    weather_url = 'https://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': '6891755b02af4134a49135148202802',
        'q': city_name,
        'format': 'json',
        'number_of_days': 1,
        'lang': 'ru'
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
        else:
            return "Сервис погоды временно недоступен"
    return False


if __name__ == '__main__':
    print(weather_by_city('Saint-Petersburg,Russia'))
