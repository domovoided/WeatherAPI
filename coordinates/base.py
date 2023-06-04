from abc import abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CoordinatesDC:
    latitude: float
    longitude: float


class CoordinatesABC:
    def __init__(self, city_name: str):
        self.city_name = city_name
        self._coordinates = self.get_coordinates_by_city_name(city_name)

    @abstractmethod
    def get_coordinates_by_city_name(self, city_name: str) -> CoordinatesDC:
        pass

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def latitude(self):
        return self._coordinates.latitude

    @property
    def longitude(self):
        return self._coordinates.longitude
