# Creating a database with SQLAlchemy has 4 major coding components:
#
# CONFIGURATION-
# generally shouldn't change from project to project
# imports all modules needed
# creates instance of declarative base
# creates (or connects) the database and adds tables and columns
#
# CLASS-
# representation of table as a python class
# extends the Base class
# nested inside will be table and mapper code
#
# TABLE-
# representation of a specific table in the database
#
# MAPPER-
# connects table columns to the class that represents it
# maps python objects to columns in the database

###### BEGINNING CONFIGURATION CODE ######
import os   # allows to interface with the
            # underlying operating system that
            # Python is running on. You can find
            # important information about your
            # location or about the process.

import sys  # provides a number of functions
            # and variables that can be used
            # to manipulate different parts of
            # the Python run-time environment.

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship # in order to create ForeignKey relationships

from sqlalchemy import create_engine

Base = declarative_base()   # Will let
                            # SQLAlchemy know
                            # that our classes
                            # are special
                            # SQLAlchemy
                            # classes that
                            # correspond to
                            # tables in our
                            # database

###### CLASS CODE ######
class Restaurant(Base):
    ###### TABLE CODE ######
    __tablename__ = 'restaurant'
    ###### MAPPER CODE ######
    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)

class MenuItem(Base):
    ###### TABLE CODE ######
    __tablename__ = 'menu_item'
    ###### MAPPER CODE ######
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


###### ENDING CONFIGURATION CODE ######
engine = create_engine(
'sqlite:///restaurantmenu.db')  # Instance of
                                # create_engine
                                # class points
                                # to the
                                # database we'll
                                # use.

Base.metadata.create_all(engine)    # Goes into
                                    # the
                                    # database
                                    # and adds
                                    # the
                                    # classes
                                    # we'll
                                    # create
                                    # as new
                                    # tables in
                                    # our
                                    # database
