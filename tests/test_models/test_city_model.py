#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.city import City


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    @classmethod
    def setUpClass(cls):
        '''
            setup instances for each test
        '''
        cls.new_city = City()
        cls.new_city.state_id = '209420834'
        cls.new_city.name = "SF"
    
    def test_City_inheritance(self):
        '''
            tests that the City class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_city, BaseModel)

    def test_User_attributes(self):
        self.assertTrue("state_id" in self.new_city.__dir__())
        self.assertTrue("name" in self.new_city.__dir__())

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_name(self):
        '''
            Test the type of name
        '''
        name = getattr(self.new_city, "state_id")
        self.assertIsInstance(name, str)
