from unittest import TestCase

from src.Piece import Piece


class TestPiece(TestCase):
    def test_eq(self):
        self.assertEqual(Piece(5, 7), Piece(5, 7))
        self.assertNotEqual(Piece(5, 7), Piece(5, 8))
        self.assertNotEqual(Piece(5, 7), "aa")
