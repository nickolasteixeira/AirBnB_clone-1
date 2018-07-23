#!/usr/bin/python3
'''
    Define class DBStorage
'''
import models
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    '''
        DBStorage
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''initializing DBStorage object

        '''
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ), pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine)
        self.__session = Session()

        if getenv('HBNB_ENV') == 'test':
            getenv('HBNB_MYSQL_USER').__table__.drop(self.__engine)

    def all(self, cls=None):
        '''
            Gets all the queries associated with the class

        '''
        new_key = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = str(obj.__class__.__name__) + "." + str(obj.id)
                new_key[key] = obj
        else:
            # ADD ALL CLASSES LATER
            all_classes = [State, City]
            for classes in all_classes:
                for obj in self.__session.query(classes).all():
                    key = str(obj.__class__.__name__) + "." + str(obj.id)
                    new_key[key] = obj
        return new_key

    def new(self, obj):
        ''' Adds a new obj to the database'''
        self.__session.add(obj)

    def save(self):
        ''' Saves your current session'''
        self.__session.commit()

    def delete(self, obj=None):
        ''' Deletes the current object'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ''' Reloads the engine'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
