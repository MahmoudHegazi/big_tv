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
