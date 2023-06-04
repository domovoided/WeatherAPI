from geopy import geocoders, Location

from coordinates.base import CoordinatesABC, CoordinatesDC
from coordinates.exceptions import CantGetCoordinates


class GeopyCoordinates(CoordinatesABC):
    def get_coordinates_by_city_name(self, city_name: str) -> CoordinatesDC:
        try:
            coordinates = geocoders.Nominatim(user_agent='telebot').geocode(city_name)
            return self._parse_coordinates(coordinates)
        except Exception:
            raise CantGetCoordinates(city_name)

    @staticmethod
    def _parse_coordinates(geocode: Location) -> CoordinatesDC:
        latitude = float(geocode.latitude)
        longitude = float(geocode.longitude)
        return CoordinatesDC(latitude, longitude)
