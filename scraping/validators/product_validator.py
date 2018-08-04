from scraping.validators.abstract_validator import AbstractValidator


class ProductValidator(AbstractValidator):

    def __init__(self):
        super().__init__()

    def schema(self):
        return {
                    'name': {'type': 'string', 'required': True, 'empty': False},
                    'store': {'type': 'string', 'required': True, 'empty': False},
                    'price': {'type': 'float', 'required': True},
                    'real_price': {'type': 'float', 'required': True},
               }
