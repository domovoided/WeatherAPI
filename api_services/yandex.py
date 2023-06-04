from datetime import datetime

from structures import WeatherToOneDay, TimesOfDay, WeatherToOneTime, WeatherType, WindDirection, Celsius
from .base import APIServiceABC
from .exceptions import APIServiceError


class Yandex(APIServiceABC):
    def __init__(self, token: str, **kwargs):
        super().__init__(**kwargs)
        self._token = token
        self._root_url = 'https://api.weather.yandex.ru/v2/forecast'

    def get_weather_forecast(self, days: int) -> list[WeatherToOneDay]:
        yandex_response_json = self._get_response()
        forecast_list = []
        for day_number in range(0, days):
            forecast_for_day = WeatherToOneDay(
                night=_parse_yandex_response(yandex_response_json, TimesOfDay.night, day_number),
                morning=_parse_yandex_response(yandex_response_json, TimesOfDay.morning, day_number),
                day=_parse_yandex_response(yandex_response_json, TimesOfDay.day, day_number),
                evening=_parse_yandex_response(yandex_response_json, TimesOfDay.evening, day_number)
            )
            forecast_list.append(forecast_for_day)
        return forecast_list

    def _get_response(self) -> dict:
        response = self._browser.get(self._root_url, params={
            'lat': self._coordinates.latitude,
            'lon': self._coordinates.longitude,
            'lang': ['ru_RU']
        }, headers={'X-Yandex-API-Key': self._token})
        response_json = self._browser.json(response)
        print(response_json)
        return response_json


def _parse_yandex_response(yandex_dict: dict, time_of_day: TimesOfDay, day_number: int) -> WeatherToOneTime:
    yandex_dict = yandex_dict.get("forecasts", "forbidden")
    if yandex_dict == "forbidden":
        raise APIServiceError(Yandex)
    return WeatherToOneTime(
        temperature=_parse_temperature(yandex_dict, time_of_day, day_number),
        weather_type=_parse_weather_type(yandex_dict, time_of_day, day_number),
        wind_direction=_parse_wind_direction(yandex_dict, time_of_day, day_number),
        time_of_day=time_of_day,
        date=_parse_date(yandex_dict, day_number),
    )


def _parse_temperature(yandex_dict: dict, time_of_day: TimesOfDay, day_number: int) -> Celsius:
    temperature_avg = yandex_dict[day_number]["parts"][time_of_day.name]["temp_avg"]
    return int(temperature_avg)


def _parse_weather_type(yandex_dict: dict, time_of_day: TimesOfDay, day_number: int) -> WeatherType:
    weather_type = yandex_dict[day_number]["parts"][time_of_day.name]["condition"]
    weather_type = str(weather_type).replace("-", "_")
    weather_type = WeatherType[weather_type]
    return weather_type


def _parse_wind_direction(yandex_dict: dict, time_of_day: TimesOfDay, day_number: int) -> WindDirection:
    wind_direction = yandex_dict[day_number]["parts"][time_of_day.name]["wind_dir"]
    wind_direction = WindDirection[str(wind_direction).upper()]
    return wind_direction


def _parse_date(yandex_dict: dict, day_number: int) -> datetime:
    date_ts = int(yandex_dict[day_number]["date_ts"])
    date = datetime.fromtimestamp(date_ts)
    return date
