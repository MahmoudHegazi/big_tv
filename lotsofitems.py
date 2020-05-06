#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Menu, Movie, Series, User 
engine = create_engine('sqlite:///bigtv.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create Admin user
User1 = User(name="Website Admin", email="mahmod.hagzy@gmail.com")
session.add(User1)
session.commit()

# Menu for Series
type1 = Menu(menu_type="Series")
session.add(type1)
session.commit()

series1 = Series(name="The End", description="In 2120 an engineer tries to solve the energy problem that threatens the survival of the human race",
                  hero="youssef el sherif" ,
                  image="https://elwekalanews.net/wp-content/uploads/2020/04/%D9%85%D8%B3%D9%84%D8%B3%D9%84-%D8%A7%D9%84%D9%86%D9%87%D8%A7%D9%8A%D8%A9.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series1)
session.commit()

series1 = Series(name="The Prince", description="that the story of Prince is similar to the story of our master Joseph, peace be upon him, and Kabeel,Habeel and Noble stories are from ancient times, but they are repeated tshroughout the ages.",
                  hero="Mohamed Ramdan" ,
                  image="https://s3-eu-west-1.amazonaws.com/static.jbcgroup.com/amd/pictures/0e628cc7d4a56975552bd9d75efd35f0.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series1)
session.commit()

series1 = Series(name="Valentino", description="He plays the role of Noor Abdul Majeed, the mighty artist Adel Imam, and he has a private school he owns, married to Dalal Abdel Aziz and he has three children",
                  hero="Adel Amam",
                  image="https://images.akhbarelyom.com/images/images/large/20200503092638730.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series1)
session.commit()


# Menu for Movies
type2 = Menu(menu_type="Movies")
session.add(type1)
session.commit()


series1 = Movie(name="Joker", description="The movie, which represents the story of the origin of the Joker, was re-released in 1981 and follows Arthur Flick, a failed comedian who turns to a life of crime.",
                  hero="Joaquin Phoenix",
                  image="https://upload.wikimedia.org/wikipedia/ar/8/82/Joker_2019_ME_poster.png",
                  url='test.html', date='10/2/2020',
                  menu=type1)

session.add(series1)
session.commit()

series1 = Movie(name="The Legend of Tarzan",
                  description="The Tarzan Legend is an action movie produced in the United States and released in 2016. The film is directed by David Yates and written by Stuart Betty.",
                  hero="alexander skarsgard" ,
                  image="https://ww.mycima.co/wp-content/uploads/2019/04/The-Legend-Of-Tarzan-2016-.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series1)
session.commit()

series1 = Movie(name="The Blue Elephant", description="The Blue Elephant has a 2014 Egyptian drama and mystery film, directed by Marwan Hamed and written by Ahmed Murad",
                  hero="Adel Amam" ,
                  image="https://media.linkonlineworld.com/img/large/2015/4/1/2015_4_1_12_49_51_303.jpg",
                  url='test.html', date='5/24/2020',
                  menu=type1)

session.add(series1)
session.commit()

print "added menu items!"


