class Product:
    def __init__(self, title: str, price: float):
        self._title = title
        self._price = price

    @property
    def title(self):
        return self._title

    @property
    def price(self):
        return self._price
