from dataclasses import dataclass
from datetime import datetime
from enum import Enum, StrEnum
from typing import NamedTuple, TypeAlias

Celsius: TypeAlias = int


class WeatherType(StrEnum):
    clear = "ясно"
    partly_cloudy = "малооблачно"
    cloudy = "облачно с прояснениями"
    overcast = "пасмурно"
    drizzle = "морось"
    light_rain = "небольшой дождь"
    rain = "дождь"
    moderate_rain = "умеренно сильный дождь"
    heavy_rain = "сильный дождь"
    continuous_heavy_rain = "длительный сильный дождь"
    showers = "ливень"
    wet_snow = "дождь со снегом"
    light_snow = "небольшой снег"
    now = "снег"
    snow_showers = "снегопад"
    hail = "град"
    thunderstorm = "гроза"
    thunderstorm_with_rain = "дождь с грозой"
    thunderstorm_with_hail = "гроза с градом"


class WindDirection(StrEnum):
    NW = "северо-западный"
    N = "северный"
    NE = "северо-восточный"
    E = "восточный"
    SE = "юго-восточный"
    S = "южный"
    SW = "юго-западный"
    W = "западный"
    C = "штиль"


class TimesOfDay(StrEnum):
    night = "Ночь"
    morning = "Утро"
    day = "День"
    evening = "Вечер"


@dataclass(frozen=True, slots=True)
class WeatherToOneTime:
    temperature: Celsius
    weather_type: WeatherType
    wind_direction: WindDirection
    date: datetime
    time_of_day: TimesOfDay


class WeatherToOneDay(NamedTuple):
    night: WeatherToOneTime
    morning: WeatherToOneTime
    day: WeatherToOneTime
    evening: WeatherToOneTime
