from sqlalchemy import Column, Integer, String;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy import create_engine;

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String)
    price = Column(Integer)

engine = create_engine('sqlite:///revi.db')
Base.metadata.create_all(engine)
    