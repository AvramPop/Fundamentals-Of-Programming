from unittest import TestCase

from src.Utils import stringsPartiallyMatch


class TestUtils(TestCase):
    def test_stringsPartiallyMatch(self):
        self.assertTrue(stringsPartiallyMatch("cemetery", "cem"))
        self.assertTrue(stringsPartiallyMatch("cem", "c"))
        self.assertFalse(stringsPartiallyMatch("iosif", "dani"))
