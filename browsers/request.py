from requests import Response, get, RequestException, JSONDecodeError

from browsers.base import BrowserABC
from browsers.exceptions import CantGetResponse, CantGetJSONResponse
from logs import build_logger

logger = build_logger(__name__)


class RequestBrowser(BrowserABC):
    def get(self, url: str, params: dict = None, **kwargs) -> Response:
        try:
            logger.info(f'Отправляется GET запрос по URL: {url}')
            response = get(url, params=params, **kwargs)
        except RequestException as e:
            logger.error(f'Не удалось получить ответ по URL: {url}, {e.args}')
            raise CantGetResponse
        logger.info(f'Ответ получен на GET запрос по URL: {url}')
        return response

    @staticmethod
    def json(response) -> dict:
        try:
            response_json = response.json()
        except JSONDecodeError:
            logger.error(f'Не удалось преобразовать ответ в JSON, {response=}')
            raise CantGetJSONResponse

        return response_json
