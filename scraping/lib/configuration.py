import yaml
from scraping import API_ROUTE_FILE
from functools import partial
from collections import UserDict


def _corridor_selector(url, store, key):
    store_id = store['id']
    corridors = store['corridors']
    try:
        sub_corridor_id = next(c['id'] for c in corridors if c['name'] == key)
        return url.format(store=store_id, sub_corridor=sub_corridor_id)
    except StopIteration:
        raise KeyError(key)


class Configuration(UserDict):
    def __init__(self):
        super().__init__()

        with open(API_ROUTE_FILE, 'r') as file:
            self.data = yaml.load(file)

        url = self.data['url-template']

        corridor = partial(_corridor_selector, url)

        for store in self.data['stores']:
            store_name = store['name']
            setattr(self.__class__, store_name, partial(corridor, store))
