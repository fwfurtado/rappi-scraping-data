from requests import get
from functools import partial
from scraping.lib import configuration as config
from scraping.services import product_service


def get_all_stores(configuration):
    for store in configuration['stores']:
        yield store


def _get_all_corridors_by_store(url, store):
    name = store['name']
    store_id = store['id']

    for corridor in store['corridors']:
        corridor_id = corridor['id']
        yield name, url.format(store=store_id, sub_corridor=corridor_id)


def get_all_corridors(url, store_sequence):

    get_all_corridors_by_store = partial(_get_all_corridors_by_store, url)

    for corridor_items in map(get_all_corridors_by_store, store_sequence):
        for item in list(corridor_items):
            yield item


def get_all_products(corridor_sequence):
    for name, url in corridor_sequence:
        for product in _get_products(name, url):
            yield product


def _get_products(store_name, url):
    all_products = get(url).json()['products']

    for product_json in all_products:
        form = {
            'store': store_name,
            'name': product_json['name'],
            'price': product_json['price'],
            'real_price': product_json['real_price'],
        }

        result = product_service.create_new_product(form)

        if result.is_right:
            yield result.value
        else:
            print(result.value)


def main():

    url_template = config.url

    of_all_stores = get_all_stores(config)

    in_all_corridors_of_all_stores = get_all_corridors(url_template, of_all_stores)

    products = get_all_products(in_all_corridors_of_all_stores)

    for item in products:
        print(item)


if __name__ == '__main__':
    main()
