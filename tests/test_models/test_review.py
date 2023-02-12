#!/usr/bin/python3
"""tests for class review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):
    """test for review class"""

    @classmethod
    def setUpClass(cls):
        """set up before functions"""
        cls.newreview = Review()
        cls.newreview.place_id = "7272728"
        cls.newreview.user_id = "Lul"
        cls.newreview.text = "Place is meh"

    @classmethod
    def teardown(cls):
        """teardown"""
        del cls.newreview

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_review(self):
        """tests pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_review(self):
        """test for docstring"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """checking instance attributes"""
        self.assertTrue('id' in self.newreview.__dict__)
        self.assertTrue('created_at' in self.newreview.__dict__)
        self.assertTrue('updated_at' in self.newreview.__dict__)
        self.assertTrue('place_id' in self.newreview.__dict__)
        self.assertTrue('text' in self.newreview.__dict__)
        self.assertTrue('user_id' in self.newreview.__dict__)

    def test_subclass_review(self):
        """test for inheritance"""
        self.assertTrue(issubclass(self.newreview.__class__, BaseModel), True)

    def test_attr_types_review(self):
        """test attribute type in instance"""
        self.assertEqual(type(self.newreview.text), str)
        self.assertEqual(type(self.newreview.place_id), str)
        self.assertEqual(type(self.newreview.user_id), str)

    def test_save(self):
        """test save function"""
        self.newreview.save()
        self.assertNotEqual(self.newreview.created_at,
                            self.newreview.updated_at)

    def test_to_dict(self):
        """test dictionary is there"""
        self.assertEqual('to_dict' in dir(self.newreview), True)


if __name__ == "__main__":
    unittest.main()

