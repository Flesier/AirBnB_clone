#!/usr/bin/python3
"""tests for class state"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):
    """test state class"""

    @classmethod
    def setUpClass(cls):
        """set up functions"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def teardown(cls):
        """teardown after functions"""
        del cls.state

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_stat(self):
        """checks for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_stat(self):
        """test for docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_attr_stat(self):
        """test for existance of keys"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_inheritance_stat(self):
        """test inheritance"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attrtype_stat(self):
        """test attribute type"""
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        """test save function"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        """test dictionary function"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()

