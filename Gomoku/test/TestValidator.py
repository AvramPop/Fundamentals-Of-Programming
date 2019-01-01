from unittest import TestCase

from src.Piece import Piece
from src.Repository import Repository
from src.Validator import Validator


class TestValidator(TestCase):
    def test_isValid(self):
        repository1 = Repository()
        repository1.add(Piece(0, 0))
        repository1.add(Piece(1, 1))
        repository2 = Repository()
        repository2.add(Piece(13, 13))
        repository2.add(Piece(14, 14))
        validator = Validator(repository1, repository2)
        self.assertTrue(validator.isValid(Piece(3, 3)))
        self.assertTrue(validator.isValid(Piece(3, 8)))
        self.assertFalse(validator.isValid(Piece(-1, 5)))
        self.assertFalse(validator.isValid(Piece(-1, -9)))
        self.assertFalse(validator.isValid(Piece(21, 5)))
        self.assertFalse(validator.isValid(Piece(1, 55)))
        self.assertFalse(validator.isValid(Piece(0, 0)))
        self.assertFalse(validator.isValid(Piece(14, 14)))
