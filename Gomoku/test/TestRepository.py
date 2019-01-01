from unittest import TestCase

from src.Exceptions import RepositoryException
from src.Piece import Piece
from src.Repository import Repository


class TestRepository(TestCase):
    def test_add(self):
        repositoryMock = Repository()
        repositoryMock.add(5)
        repositoryMock.add(Piece(5, 7))
        self.assertEqual(repositoryMock.getList(), [5, Piece(5, 7)])
        with self.assertRaises(RepositoryException):
            repositoryMock.add(5)
