from abc import ABC, abstractmethod


class Either(ABC):

    @property
    @abstractmethod
    def is_left(self) -> bool:
        pass

    @property
    @abstractmethod
    def is_right(self) -> bool:
        pass

    @property
    @abstractmethod
    def value(self) -> object:
        pass


class Left(Either):

    def __init__(self, value):
        self._value = value

    @property
    def is_left(self) -> bool:
        return True

    @property
    def is_right(self) -> bool:
        return False

    @property
    def value(self) -> object:
        return self._value


class Right(Either):
    def __init__(self, value):
        self._value = value

    @property
    def is_left(self) -> bool:
        return False

    @property
    def is_right(self) -> bool:
        return True

    @property
    def value(self) -> object:
        return self._value
