class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f'Product(title="{self.name}", price={self.price})'
