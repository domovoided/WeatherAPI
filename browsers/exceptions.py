class BrowserException(Exception):
    def __init__(self, message: str = None):
        self.message = message


class CantGetResponse(BrowserException):
    pass


class CantGetJSONResponse(CantGetResponse):
    pass
