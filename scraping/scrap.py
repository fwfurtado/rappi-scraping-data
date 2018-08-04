from requests import get

from scraping.lib import configuration
from scraping.services import product_service


def get_all_stores():
    for store in configuration['stores']:
        yield store


def _get_all_corridors_by_store(store):
    name = store['name']
    store_id = store['id']

    for corridor in store['corridors']:
        corridor_id = corridor['id']
        url = configuration.url.format(store=store_id, sub_corridor=corridor_id)
        yield name, url


def get_all_corridors(store_sequence):
    for corridor_items in map(_get_all_corridors_by_store, store_sequence):
        for item in list(corridor_items):
            yield item


def get_all_products(corridor_sequence):
    for name, url in corridor_sequence:
        for product in _get_products(name, url):
            yield product


def _get_products(name, url):
    all_products = get(url).json()['products']

    for product_json in all_products:
        form = {
            'name': product_json['name'],
            'price': product_json['price']
        }

        result = product_service.create_new_product(form)

        if result.is_right:
            yield result.value
        else:
            print(result.value)


def main():
    of_all_stores = get_all_stores()

    in_all_corridors_of_all_stores = get_all_corridors(of_all_stores)

    products = get_all_products(in_all_corridors_of_all_stores)

    for item in products:
        print(item)


if __name__ == '__main__':
    main()
