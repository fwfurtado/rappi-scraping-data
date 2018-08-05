from contextlib import ContextDecorator
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import sessionmaker

connection_string = 'postgresql+psycopg2://scraping:123mudar@localhost:5432/rappi'

engine = create_engine(connection_string, echo=True)

Session = sessionmaker(bind=engine)


class Transactional(ContextDecorator):

    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        has_exception = exc_type is None

        if has_exception:
            self.session.commit()
        else:
            self.session.rollback()
        return has_exception


class BaseTable:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.now())


Base = declarative_base(cls=BaseTable)