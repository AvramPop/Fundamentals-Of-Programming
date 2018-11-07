from unittest import TestCase
from main.model.Date import Date
from main.Exception import InvalidDateFormatException


class TestDate(TestCase):
    def setUp(self):
        self.date = Date(5, 7, 2018)

    def tearDown(self):
        self.date = None

    def test_init(self):
        self.assertEqual(self.date.day, 5)
        self.assertEqual(self.date.month, 7)
        self.assertEqual(self.date.year, 2018)
        with self.assertRaises(InvalidDateFormatException):
            testDate = Date("sa", 5, 25)
        with self.assertRaises(InvalidDateFormatException):
            testDate = Date(2, [], 6)
        with self.assertRaises(InvalidDateFormatException):
            testDate = Date(1, 9, -75.5)
        with self.assertRaises(InvalidDateFormatException):
            testDate = Date(100, 6, 7)
        with self.assertRaises(InvalidDateFormatException):
            testDate = Date(2, 100, 7)
        with self.assertRaises(InvalidDateFormatException):
            testDate = Date(5, 6, -7)

    def test_equals(self):
        self.assertTrue(self.date == Date(5, 7, 2018))

    def test_comparison(self):
        self.assertTrue(self.date.isBeforeDate(Date(6, 7, 2018)))
        self.assertTrue(self.date.isBeforeDate(Date(5, 8, 2018)))
        self.assertTrue(self.date.isBeforeDate(Date(5, 7, 2019)))
        self.assertFalse(self.date.isBeforeDate(Date(4, 7, 2018)))
        self.assertFalse(self.date.isBeforeDate(Date(5, 7, 202)))
