#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        re_view = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(re_view))
        self.assertNotIn("place_id", re_view.__dict__)

    def test_user_id_is_public_class_attribute(self):
        re_view = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(re_view))
        self.assertNotIn("user_id", re_view.__dict__)

    def test_text_is_public_class_attribute(self):
        re_view = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(re_view))
        self.assertNotIn("text", re_view.__dict__)

    def test_two_reviews_unique_ids(self):
        re_view1 = Review()
        re_view2 = Review()
        self.assertNotEqual(re_view1.id, re_view2.id)

    def test_two_reviews_different_created_at(self):
        re_view1 = Review()
        sleep(0.05)
        re_view2 = Review()
        self.assertLess(re_view1.created_at, re_view2.created_at)

    def test_two_reviews_different_updated_at(self):
        re_view1 = Review()
        sleep(0.05)
        re_view2 = Review()
        self.assertLess(re_view1.updated_at, re_view2.updated_at)

    def test_str_representation(self):
        date_time = datetime.today()
        dt_repr = repr(date_time)
        re_view = Review()
        re_view.id = "123456"
        re_view.created_at = re_view.updated_at = date_time
        rvstr = re_view.__str__()
        self.assertIn("[Review] (123456)", rvstr)
        self.assertIn("'id': '123456'", rvstr)
        self.assertIn("'created_at': " + dt_repr, rvstr)
        self.assertIn("'updated_at': " + dt_repr, rvstr)

    def test_args_unused(self):
        re_view = Review(None)
        self.assertNotIn(None, re_view.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date_time = datetime.today()
        dt_iso = date_time.isoformat()
        re_view = Review(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(re_view.id, "345")
        self.assertEqual(re_view.created_at, date_time)
        self.assertEqual(re_view.updated_at, date_time)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """Unittests for testing save method of the Review class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        re_view = Review()
        sleep(0.05)
        first_updated_at = re_view.updated_at
        re_view.save()
        self.assertLess(first_updated_at, re_view.updated_at)

    def test_two_saves(self):
        re_view = Review()
        sleep(0.05)
        first_updated_at = re_view.updated_at
        re_view.save()
        second_updated_at = re_view.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        re_view.save()
        self.assertLess(second_updated_at, re_view.updated_at)

    def test_save_with_arg(self):
        re_view = Review()
        with self.assertRaises(TypeError):
            re_view.save(None)

    def test_save_updates_file(self):
        re_view = Review()
        re_view.save()
        rvid = "Review." + re_view.id
        with open("file.json", "r") as f:
            self.assertIn(rvid, f.read())


class TestReview_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Review class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        re_view = Review()
        self.assertIn("id", re_view.to_dict())
        self.assertIn("created_at", re_view.to_dict())
        self.assertIn("updated_at", re_view.to_dict())
        self.assertIn("__class__", re_view.to_dict())

    def test_to_dict_contains_added_attributes(self):
        re_view = Review()
        re_view.middle_name = "ALX"
        re_view.my_number = 98
        self.assertEqual("ALX", re_view.middle_name)
        self.assertIn("my_number", re_view.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        re_view = Review()
        rv_dict = re_view.to_dict()
        self.assertEqual(str, type(rv_dict["id"]))
        self.assertEqual(str, type(rv_dict["created_at"]))
        self.assertEqual(str, type(rv_dict["updated_at"]))

    def test_to_dict_output(self):
        date_time = datetime.today()
        re_view = Review()
        re_view.id = "123456"
        re_view.created_at = re_view.updated_at = date_time
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': date_time.isoformat(),
            'updated_at': date_time.isoformat(),
        }
        self.assertDictEqual(re_view.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        re_view = Review()
        self.assertNotEqual(re_view.to_dict(), re_view.__dict__)

    def test_to_dict_with_arg(self):
        re_view = Review()
        with self.assertRaises(TypeError):
            re_view.to_dict(None)


if __name__ == "__main__":
    unittest.main()
