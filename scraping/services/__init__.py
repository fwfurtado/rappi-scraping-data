from scraping.services.product_service import ProductService
from scraping.validators import product_validator

product_service = ProductService(product_validator)

__all__ = [product_service]
