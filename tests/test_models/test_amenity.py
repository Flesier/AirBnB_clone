#!/usr/bin/python3
"""tests for class amenity"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class TestAmenity(unittest.TestCase):
    """this will test the Amenity class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.lord = Amenity()
        cls.lord.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.lord

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_Amen(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_Amen(self):
        """test for docstrings"""
        self.assertIsNotNone(self.lord.__doc__)

    def test_attr_Amen(self):
        """chekcing if amenity have attibutes"""
        self.assertTrue('id' in self.lord.__dict__)
        self.assertTrue('created_at' in self.lord.__dict__)
        self.assertTrue('updated_at' in self.lord.__dict__)
        self.assertTrue('name' in self.lord.__dict__)

    def test_inheritance_Amen(self):
        """test if inheritance works"""
        self.assertTrue(issubclass(self.lord.__class__, BaseModel), True)

    def test_attrtype_Amen(self):
        """test attr types in instance"""
        self.assertEqual(type(self.lord.name), str)

    def test_save(self):
        """test the save function"""
        self.lord.save()
        self.assertNotEqual(self.lord.created_at, self.lord.updated_at)

    def test_to_dict(self):
        """test if dictionary function works"""
        self.assertEqual('to_dict' in dir(self.lord), True)


if __name__ == "__main__":
    unittest.main()
