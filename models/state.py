#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
