#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''

    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", passive_deletes=True, backref="state")
    else:
        name = ""

        @property
        def cities(self):
            '''Getter for cities'''
            cities = [v for k, v in models.storage.all().items()
                      if 'City' in k and v.state_id == self.id]
            return cities
            #get_all = models.storage.all('City').items()
            # return [obj for obj in get_all if obj.state_id == self.id]
