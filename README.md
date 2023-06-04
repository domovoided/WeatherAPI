# WeatherAPI

## Кратко
Python-скрипт, который выводит прогноз погоды на ближайшие N дней. Может взаимодействовать с разными API, которые предоставляют погоду.

Работает на русском языке.

## Реализовано
На данный подключено:
- [x] API Яндекс.Погода (любой тариф, кроме "Тестовый")
- [ ] OpenWeather (80%)

## Пример использования
```python
from api_services import Yandex
from api_services.exceptions import APIServiceError
from browsers.request import RequestBrowser
from config import YANDEX_TOKEN
from coordinates import GeopyCoordinates
from coordinates.exceptions import CantGetCoordinates
from gui.terminal import TerminalFormatter
from logs import init_logger, build_logger

request_browser = RequestBrowser()


def main():
    init_logger()
    logger = build_logger(__name__)

    try:
        coordinates = GeopyCoordinates('Санкт-Петербург')
    except CantGetCoordinates as e:
        logger.critical(e.message)
        exit(-1)

    api_service = Yandex(
        'https://api.weather.yandex.ru/v2/forecast',
        YANDEX_TOKEN,
        coordinates=coordinates,
        browser=request_browser
    )

    try:
        forecast_list = api_service.get_weather_forecast(5)
    except APIServiceError as e:
        logger.critical(e.message)
        exit(-1)

    TerminalFormatter.print(forecast_list)


if __name__ == "__main__":
    main()
```
