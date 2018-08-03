import pytest

from scraping.lib.configuration import Configuration


class TestConfiguration:

    def test_should_add_dynamic_method_of_each_store(self):
        configuration = Configuration()

        assert configuration

        url = configuration.minuto('cervejas')

        assert 'https://services.rappi.com.br/windu/products/store/700000129/sub_corridor/453624' == url

    def test_should_raise_key_error_when_trying_to_access_invalid_corridor(self):
        configuration = Configuration()

        assert configuration

        invalid_key = 'Banana'

        with pytest.raises(KeyError):
            configuration.minuto(invalid_key)
