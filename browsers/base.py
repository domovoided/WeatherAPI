from abc import ABC, abstractmethod


class BrowserABC(ABC):
    @abstractmethod
    def get(self, url: str, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def json(response) -> dict:
        pass
