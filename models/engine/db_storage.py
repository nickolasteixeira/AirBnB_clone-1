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
        DBStorage class creates engine and a new session
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

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)


    def all(self, cls=None):
        """returns a dictionary
        Returns:
            returns the dictionary of the object
        """
        obj = {}
        clss = [value for key, value in models.classes.items()]
        if cls:
            if type(cls) == str:
                cls = models.classes[cls]
            clss = [cls]
        for one_class in clss:
            for value in self.__session.query(one_class):
                key = str(value.__class__.__name__) + "." + str(value.id)
                obj[key] = value
        return obj

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

    def close(self):
        '''
            Removes the session
        '''
        if self.__session:
            self.__session.close()

