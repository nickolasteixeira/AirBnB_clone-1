#!/usr/bin/python3

'''
    All the test for the amenity model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
        Testing Amenity class
    '''
    @classmethod
    def setUpClass(cls):
        '''
            setup class instance
        '''
        cls.new_amenity = Amenity()
        cls.new_amenity.name = "amenity"

    def test_Amenity_inheritence(self):
        '''
            tests that the Amenity class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        '''
            Test that Amenity class had name attribute.
        '''
        self.assertTrue("name" in self.new_amenity.__dir__())

    def test_Amenity_attribute_type(self):
        '''
            Test that Amenity class had name attribute's type.
        '''
        name_value = getattr(self.new_amenity, "name")
        self.assertIsInstance(name_value, str)
