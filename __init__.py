from flask import Flask, render_template

from bidva_news import get_bdva_news
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Прогноз погоды и парсинг сайта'
    weather = weather_by_city('Saint_Peterburg,Russia')
    news_list = get_bdva_news()
    return render_template('index.html', page_title=title, weather=weather, news_list=news_list)


if __name__ == "__main__":
    app.run(debug=True)
