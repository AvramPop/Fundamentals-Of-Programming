from unittest import TestCase

from src.Exceptions import ValidException
from src.UserService import UserService
from src.Piece import Piece
from src.Repository import Repository
from src.Validator import Validator


class TestUserService(TestCase):
    def test_addPiece(self):
        repository1 = Repository()
        repository1.add(Piece(0, 0))
        repository1.add(Piece(1, 1))
        repository2 = Repository()
        repository2.add(Piece(13, 13))
        repository2.add(Piece(14, 14))
        validator = Validator(repository1, repository2)
        userService = UserService(repository1, validator)
        userService.addPiece(5, 5)
        self.assertEqual(userService.getList(), [Piece(0, 0), Piece(1, 1), Piece(5, 5)])
        with self.assertRaises(ValidException):
            userService.addPiece(0, 0)
        with self.assertRaises(ValidException):
            userService.addPiece(13, 13)
        with self.assertRaises(ValidException):
            userService.addPiece(-1, 0)
        with self.assertRaises(ValidException):
            userService.addPiece(0, 199)
