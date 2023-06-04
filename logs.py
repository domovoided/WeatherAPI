from logging import (Logger, getLogger,
                     StreamHandler,
                     DEBUG, INFO, Formatter)
from logging.handlers import RotatingFileHandler

from config import LOGS_DIR, APP_NAME


def init_logger(logger_name: str | None = None, log_format: str | None = None) -> None:
    if not logger_name:
        logger = getLogger(APP_NAME)
    else:
        logger = getLogger(logger_name)
    if not log_format:
        log_format = '[%(asctime)s - %(name)s:%(lineno)s] - %(levelname)s - %(message)s'
    logger.setLevel(DEBUG)

    stream_handler = StreamHandler()
    stream_handler.setFormatter(Formatter(log_format))
    stream_handler.setLevel(DEBUG)

    file_handler = RotatingFileHandler(filename=LOGS_DIR / f'{logger.name}.log',
                                       mode='a', maxBytes=10*1024*1024, backupCount=10, encoding='utf-8')
    file_handler.setFormatter(Formatter(log_format))
    file_handler.setLevel(INFO)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.debug("Базовый логер сконфигурирован")


def build_logger(package_name: str) -> Logger:
    logger = getLogger(f'{APP_NAME}.{package_name}')
    return logger
