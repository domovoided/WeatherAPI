from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

APP_NAME = 'WeatherForecast'
BASE_DIR = Path(__name__).parent

# Директории
LOGS_DIR = BASE_DIR / 'logs'

YANDEX_TOKEN = getenv('YANDEX_TOKEN')
OPENWEATHER_TOKEN = getenv('OPENWEATHER_TOKEN')

MONTHS = {
    '01': 'января',
    '02': 'февраля',
    '03': 'марта',
    '04': 'апреля',
    '05': 'мая',
    '06': 'июня',
    '07': 'июля',
    '08': 'августа',
    '09': 'сентября',
    '10': 'октября',
    '11': 'ноября',
    '12': 'декабря'
}

TIMES_OF_DAY = {
    'night': 'Ночь',
    'morning': 'Утро',
    'day': 'День',
    'evening': 'Вечер'
}

CONDITIONS = {
    'clear': 'ясно',
    'partly-cloudy': 'малооблачно',
    'cloudy': 'облачно с прояснениями',
    'overcast': 'пасмурно',
    'drizzle': 'морось',
    'light-rain': 'небольшой дождь',
    'rain': 'дождь',
    'moderate-rain': 'умеренно сильный дождь',
    'heavy-rain': 'сильный дождь',
    'continuous-heavy-rain': 'длительный сильный дождь',
    'showers': 'ливень',
    'wet-snow': 'дождь со снегом',
    'light-snow': 'небольшой снег',
    'snow': 'снег',
    'snow-showers': 'снегопад',
    'hail': 'град',
    'thunderstorm': 'гроза',
    'thunderstorm-with-rain': 'дождь с грозой',
    'thunderstorm-with-hail': 'гроза с градом'
}

WIND_DIRECTION = {
    'nw': 'северо-западный',
    'n': 'северный',
    'ne': 'северо-восточный',
    'e': 'восточный',
    'se': 'юго-восточный',
    's': 'южный',
    'sw': 'юго-западный',
    'w': 'западный',
    'с': 'штиль'
}
