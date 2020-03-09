import os

basedir = os.path.dirname(__file__)

WEATHER_DEFAULT_CITY = 'Saint_Peterburg,Russia'
WEATHER_API_KEY = '6891755b02af4134a49135148202802'
WEATHER_URL = 'https://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
