#!/usr/bin/python3
"""Tests city"""
import unittest
import pep8
import os
from models.user import User
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """unittests for basemodel"""

    @classmethod
    def setUp(cls):
        """creates class"""
        cls.testUser = User()
        cls.testUser.email = "email"
        cls.testUser.password = "xxx"
        cls.testUser.first_name = "first"
        cls.testUser.last_name = "last"

    @classmethod
    def tearDown(cls):
        """deletes test class"""
        del cls.testUser
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        """tests docstrings"""
        self.assertTrue(len(User.__doc__) > 0)
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables(self):
        """tests init and class variables"""
        self.assertTrue(isinstance(self.testUser, User))
        self.assertTrue(issubclass(type(self.testUser), BaseModel))
        self.assertTrue('email' in self.testUser.__dict__)
        self.assertTrue('id' in self.testUser.__dict__)
        self.assertTrue('created_at' in self.testUser.__dict__)
        self.assertTrue('updated_at' in self.testUser.__dict__)
        self.assertTrue('password' in self.testUser.__dict__)
        self.assertTrue('first_name' in self.testUser.__dict__)
        self.assertTrue('last_name' in self.testUser.__dict__)

    def test_save(self):
        self.testUser.save()
        self.assertTrue(self.testUser.updated_at != self.testUser.created_at)

    def test_strings(self):
        self.assertEqual(type(self.testUser.email), str)
        self.assertEqual(type(self.testUser.password), str)
        self.assertEqual(type(self.testUser.first_name), str)
        self.assertEqual(type(self.testUser.first_name), str)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.testUser), True)


if __name__ == '__main__':
    unittest.main()

