from abc import ABC, abstractmethod
from datetime import datetime


class Handler(ABC):

    @abstractmethod
    def emit(self, message: str):
        pass


class ConsoleHandler(Handler):
    def emit(self, message: str):
        print(message)


class FileHandler(Handler):
    def emit(self, message: str):
        return f'Запись в файл: {message}'


class TimeMixin:
    def format_with_timestamp(self, message: str):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'[{now}] [{message!r}]'


class Logger(TimeMixin):
    def __init__(self, handlers: list):
        self._handlers = handlers

    def log(self, message: str):
        mess = self.format_with_timestamp(message)
        for h in self._handlers:
            h.emit(mess)

    def __call__(self, *args, **kwargs):
        self.log(*args, **kwargs)
