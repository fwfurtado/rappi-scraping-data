from scraping.lib.session_factory import Session

session = Session()


def save(product):
    session.add(product)
