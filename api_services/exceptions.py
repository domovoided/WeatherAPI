from typing import Type

from .base import APIServiceABC


class APIServiceError(Exception):
    def __init__(self, api_service: Type[APIServiceABC]):
        self.message = f'Программа не может получить прогноз погоды от {api_service.__name__}'
