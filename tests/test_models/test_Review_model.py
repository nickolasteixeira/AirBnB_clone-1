#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''
    @classmethod
    def setUpClass(cls):
        cls.new_review = Review()
        cls.new_review.place_id = '11111'
        cls.new_review.user_id = '11111'
        cls.new_review.text = 'this is a text'
        
    def test_Review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        self.assertIsInstance(self.new_review, BaseModel)

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        self.assertTrue("place_id" in self.new_review.__dir__())
        self.assertTrue("user_id" in self.new_review.__dir__())
        self.assertTrue("text" in self.new_review.__dir__())

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        place_id = getattr(self.new_review, "place_id")
        user_id = getattr(self.new_review, "user_id")
        text = getattr(self.new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
