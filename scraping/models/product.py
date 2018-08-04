class Product:
    def __init__(self, name: str, price: float, store: str, real_price: float = 0.0):
        self._name = name
        self._price = price
        self._real_price = real_price
        self._store = store

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def store(self):
        return self._store

    @property
    def real_price(self):
        return self._real_price

    def __repr__(self):
        return 'Product(name="{_name}", price={_price}, store="{_store}", real_price={_real_price})'.format(**self.__dict__)
