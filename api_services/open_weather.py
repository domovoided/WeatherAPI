from datetime import datetime

from api_services.base import APIServiceABC
from structures import WeatherToOneDay, TimesOfDay, WeatherToOneTime, Celsius, WeatherType, WindDirection


class OpenWeather(APIServiceABC):
    def __init__(self, root_url: str, token: str, **kwargs):
        super().__init__(**kwargs)
        self._root_url = root_url
        self._token = token
        self._day_number = 0
        self._raw_data_list: list[dict] = []

    def get_weather_forecast(self, days: int) -> list[WeatherToOneDay]:
        openweather_json = self._get_response()
        self._read_json_data(openweather_json)
        self._prepare_response_forecast()

        forecast_list = []
        for day_number in range(0, days):
            self._day_number = day_number
            forecast_for_day = WeatherToOneDay(
                night=self._parse_response(TimesOfDay.night),
                morning=self._parse_response(TimesOfDay.morning),
                day=self._parse_response(TimesOfDay.day),
                evening=self._parse_response(TimesOfDay.evening)
            )
            forecast_list.append(forecast_for_day)
            break
        return forecast_list

    def _read_json_data(self, response_json: dict) -> None:
        self._raw_data_list = response_json.get('list')

    def _get_response(self) -> dict:
        response = self._browser.get(self._root_url, params={
            'lat': self._coordinates.latitude,
            'lon': self._coordinates.longitude,
            'appid': self._token,
            'units': 'metric',
            'lang': 'ru',
        })
        response_json = self._browser.json(response)
        return response_json

    def _parse_response(self, time_of_day: TimesOfDay) -> WeatherToOneTime:
        time_forecast = self._raw_data_list[0]
        print(time_forecast)
        weather_to_one_time = WeatherToOneTime(
            temperature=_parse_temperature(time_forecast),
            weather_type=_parse_weather_type(time_forecast),
            wind_direction=_parse_wind_direction(time_forecast),
            date=_parse_date(time_forecast),
            time_of_day=time_of_day
        )
        self._raw_data_list.pop(0)
        return weather_to_one_time

    def _prepare_response_forecast(self):
        for i, time in enumerate(self._raw_data_list):
            if '00:00:00' in time.get('dt_txt'):
                self._raw_data_list = self._raw_data_list[i::2]
                break


def _parse_temperature(forecast: dict) -> Celsius:
    temperature = forecast['main']['temp']
    print(temperature)
    return int(temperature)


def _parse_weather_type(forecast: dict) -> WeatherType:
    weather = forecast['weather'][0]
    weather_type = weather['description']
    print(weather_type)



def _parse_wind_direction(forecast: dict) -> WindDirection:
    ...


def _parse_date(forecast: dict) -> datetime:
    ...
