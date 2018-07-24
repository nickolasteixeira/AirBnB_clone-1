#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    @classmethod
    def setUpClass(cls):
        cls.new_user = User()
        cls.new_user.email = "nickemail@email.com"
        cls.new_user.first_name = "nick"
        cls.new_user.last_name = "texmex"
        cls.new_user.password = "password"
 
    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_user, BaseModel)

    def test_User_attributes(self):
        '''
            Test the user attributes exist
        '''

        self.assertTrue("email" in self.new_user.__dir__())
        self.assertTrue("first_name" in self.new_user.__dir__())
        self.assertTrue("last_name" in self.new_user.__dir__())
        self.assertTrue("password" in self.new_user.__dir__())

    def test_type_email(self):
        '''
            Test the type of name
        '''
        self.assertIsInstance(self.new_user.email, str)

    def test_type_first_name(self):
        '''
            Test the type of name
        '''
        self.assertIsInstance(self.new_user.first_name, str)

    def test_type_last_name(self):
        '''
            Test the type of last_name
        '''
        self.assertIsInstance(self.new_user.last_name, str)

    def test_type_password(self):
        '''
            Test the type of password
        '''
        self.assertIsInstance(self.new_user.password, str)
