from scraping.lib import Right
from scraping.models import Product


class ProductService:
    def __init__(self, validator):
        self._validator = validator

    def create_new_product(self, form):
        result = self._validator.validate(form)

        if result.is_right:
            return Right(value=Product(**form))

        return result
