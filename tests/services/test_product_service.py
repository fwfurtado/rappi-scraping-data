import pytest

from scraping.services import ProductService
from scraping.validators import ProductValidator


class TestProductService:

    @pytest.fixture()
    def service(self, validator):
        return ProductService(validator)

    @pytest.fixture()
    def validator(self):
        return ProductValidator()

    def test_should_return_validation_errors_when_trying_to_create_a_new_product_with_invalid_form(self, service):
        form = {'title': 'Stella'}

        result = service.create_new_product(form)

        assert result.is_left

        errors = result.value

        assert errors['price']

        price_error = errors['price']

        assert 'required field' in price_error

    def test_should_return_new_product_when_form_is_valid(self, service):
        form = {'title': 'stella', 'price': 2.9}

        result = service.create_new_product(form)

        assert result.is_right

        product = result.value

        assert 'stella' == product.title
        assert 2.9 == product.price
