from unittest import TestCase

from main.Utils import stringsPartiallyMatch


class TestUtils(TestCase):
    def test_stringsPartiallyMatch(self):
        self.assertTrue(stringsPartiallyMatch("cement", "cemetery"))
        self.assertTrue(stringsPartiallyMatch("cEMENT", "cemetery"))
        self.assertFalse(stringsPartiallyMatch("iosif", "dani"))
