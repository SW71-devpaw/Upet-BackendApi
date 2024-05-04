from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Enum
from config.db import Base, engine

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String(255))
    petOwnerId = Column(Integer, ForeignKey('petowners.id'))
    breed = Column(String(255))
    species = Column(String(255))
    weight = Column(DECIMAL)
    age = Column(Integer)
    image_url = Column(String(255))
    gender = Column(Enum("Male","Female", name='gender'))
