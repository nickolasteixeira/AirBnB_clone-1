#!/usr/bin/python3
'''
    Testing the db_storage module.
'''

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.place import Place
from models.user import User

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 
                 'skipping db storage tests')

class testDBStorage(unittest.TestCase):
    '''
        Testing the DBclass
    '''

    def test_State(self):
        '''
            Tests States
        '''
        new_state = State(name='California')
        self.assertEqual(new_state.name, 'California') 

    def test_City(self):
        '''
            Tests Cities    
        '''
        new_city = City(name='SF')
        self.assertEqual(new_city.name, 'SF')

    def test_User(self):
        new_user = User(email='bob@hbtn.io', password='bobpwd', first_name='Bob', last_name='Dylan')
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)
        
        self.assertEqual(new_user.password, 'bobpwd')
        self.assertEqual(new_user.first_name, 'Bob')
        self.assertEqual(new_user.last_name, 'Dylan')

        
    
