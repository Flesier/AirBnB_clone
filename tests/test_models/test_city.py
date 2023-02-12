#!/usr/bin/python3
"""Tests city"""
import unittest
import pep8
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """unittests for basemodel"""

    @classmethod
    def setUp(cls):
        """creates class"""
        cls.testCity = City()
        cls.testCity.name = "test"
        cls.testCity.state_id = "T"

    @classmethod
    def tearDown(cls):
        """deletes test class"""
        del cls.testCity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8_city(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings_city(self):
        """tests docstrings"""
        self.assertTrue(len(City.__doc__) > 0)
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_init_and_class_variables_city(self):
        """tests init and class variables"""
        self.assertTrue(isinstance(self.testCity, City))
        self.assertTrue(issubclass(type(self.testCity), BaseModel))
        self.assertTrue(self.testCity.name == "test")
        self.assertTrue(self.testCity.state_id == "T")
        self.assertIsNotNone(self.testCity.id)
        self.assertIsNotNone(self.testCity.updated_at)
        self.assertIsNotNone(self.testCity.created_at)

    def test_save_city(self):
        self.testCity.save()
        self.assertTrue(self.testCity.updated_at != self.testCity.created_at)


if __name__ == '__main__':
    unittest.main()

