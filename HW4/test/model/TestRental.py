from unittest import TestCase

from main.model.Rental import Rental
from main.model.Date import Date


class TestRental(TestCase):
    def setUp(self):
        self.rental = Rental(5, 9, Date(22, 4, 1995), Date(22, 4, 1996))

    def tearDown(self):
        self.rental = None

    def test_init(self):
        self.assertEqual(self.rental, 5)
        self.assertEqual(self.rental, 7)
        self.assertEqual(self.rental, 2018)
        with self.assertRaises(ValueError):
            testRental = Rental("sa", 5, 25)
        with self.assertRaises(ValueError):
            testRental = Rental(2, [], 6)
        with self.assertRaises(ValueError):
            testRental = Rental(1, 9, -75.5)
        with self.assertRaises(ValueError):
            testRental = Rental(100, 6, 7)
        with self.assertRaises(ValueError):
            testRental = Rental(2, 100, 7)
        with self.assertRaises(ValueError):
            testRental = Rental(5, 6, -7)
