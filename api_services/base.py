from abc import ABC, abstractmethod

from browsers.base import BrowserABC
from coordinates.base import CoordinatesDC
from structures import WeatherToOneDay


class APIServiceABC(ABC):

    def __init__(self, coordinates: CoordinatesDC, browser: BrowserABC):
        self._coordinates = coordinates
        self._browser = browser

    @abstractmethod
    def get_weather_forecast(self, days: int) -> list[WeatherToOneDay]:
        pass
