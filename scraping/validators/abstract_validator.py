from abc import ABC, abstractmethod
from cerberus import Validator

from scraping.lib import Either, Right, Left


class AbstractValidator(ABC):

    def __init__(self):
        self._validator = Validator()

    @abstractmethod
    def schema(self) -> dict:
        pass

    def validate(self, input_object) -> Either:
        if self._validator.validate(input_object, self.schema()):
            return Right(value=None)

        return Left(value=self._validator.errors)
