from sqlalchemy import Column, String, Numeric

from scraping.lib.session_factory import Base


class Product(Base):
    name = Column(String, nullable=False)
    price = Column(Numeric(precision=9, scale=3), nullable=False)
    real_price = Column(Numeric(precision=9, scale=3), nullable=False)
    store = Column(String, nullable=False)
