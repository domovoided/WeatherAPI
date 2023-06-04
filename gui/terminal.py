from api_services.yandex import WeatherToOneTime
from structures import WeatherToOneDay


class TerminalFormatter:

    @classmethod
    def print(cls, forecast: list[WeatherToOneDay]):
        for day_forecast in forecast:
            print('\033[32m|============|')
            print(f'|-{day_forecast.night.date.strftime("%d.%m.%Y")}-|')
            print('|============|\033[0m')
            print(f'{cls.format_weather(day_forecast.night)}\n'
                  f'{cls.format_weather(day_forecast.morning)}\n'
                  f'{cls.format_weather(day_forecast.day)}\n'
                  f'{cls.format_weather(day_forecast.evening)}')

    @staticmethod
    def format_weather(weather: WeatherToOneTime) -> str:
        if weather.temperature > 0:
            return (f'Время дня - \033[1m{weather.time_of_day.value}\033[0m\n'
                    f'Температура: \033[31m{weather.temperature}\033[0m, {weather.weather_type.value}, ветер: {weather.wind_direction}')
        else:
            return (f'Время дня - \033[1m{weather.time_of_day.value}\033[0m\n'
                    f'Температура: \033[36m{weather.temperature}\033[0m, {weather.weather_type.value}, ветер: {weather.wind_direction}')
