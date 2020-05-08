#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    menu_type = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'menu_type': self.menu_type,
            'id': self.id,
        }


class Series(Base):
    __tablename__ = 'series'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    hero = Column(String(20))
    image = Column(String(500))
    url = Column(String(500))
    date = Column(String(100))
    ep1 = Column(String(500))
    ep2 = Column(String(500))
    ep3 = Column(String(500))
    ep4 = Column(String(500))
    ep5 = Column(String(500))
    ep6 = Column(String(500))
    ep7 = Column(String(500))
    ep8 = Column(String(500))
    ep9 = Column(String(500))
    ep10 = Column(String(500))
    ep11 = Column(String(500))
    ep12 = Column(String(500))
    ep13 = Column(String(500))
    ep14 = Column(String(500))
    ep15 = Column(String(500))
    ep16 = Column(String(500))
    ep17 = Column(String(500))
    ep18 = Column(String(500))
    ep19 = Column(String(500))
    ep20 = Column(String(500))
    ep21 = Column(String(500))
    ep22 = Column(String(500))
    ep23 = Column(String(500))
    ep24 = Column(String(500))
    ep25 = Column(String(500))
    ep26 = Column(String(500))
    ep27 = Column(String(500))
    ep28 = Column(String(500))
    ep29 = Column(String(500))
    ep30 = Column(String(500))
    menu_id = Column(Integer, ForeignKey('menu.id'))
    menu = relationship(Menu)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'hero': self.hero,
            'image': self.image,
            'url': self.url,
            'date': self.date,
        }


class Movie(Base):
    __tablename__ = 'movie'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    hero = Column(String(20))
    image = Column(String(500))
    url = Column(String(500))
    date = Column(String(100))
    menu_id = Column(Integer, ForeignKey('menu.id'))
    menu = relationship(Menu)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'hero': self.hero,
            'image': self.image,
            'url': self.url,
            'date': self.date,
        }   


engine = create_engine('sqlite:///bigtv.db')
Base.metadata.create_all(engine)

