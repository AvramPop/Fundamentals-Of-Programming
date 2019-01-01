from unittest import TestCase

from src.AIService import AIService
from src.Piece import Piece
from src.Repository import Repository
from src.UserService import UserService
from src.Validator import Validator


class TestAIService(TestCase):
    def test_addPieceToBlock(self):
        userPiecesRepository = Repository()
        userPiecesRepository.add(Piece(0, 0))
        userPiecesRepository.add(Piece(1, 1))
        userPiecesRepository.add(Piece(2, 2))
        userPiecesRepository.add(Piece(3, 3))
        aiPiecesRepository = Repository()
        validator = Validator(userPiecesRepository, aiPiecesRepository)
        aiPiecesService = AIService(aiPiecesRepository, userPiecesRepository, validator)
        aiPiecesService.addPiece()
        self.assertEqual(aiPiecesService.getList(), [Piece(4, 4)])

    def test_addPieceToWin(self):
        userPiecesRepository = Repository()
        aiPiecesRepository = Repository()
        aiPiecesRepository.add(Piece(0, 0))
        aiPiecesRepository.add(Piece(1, 1))
        aiPiecesRepository.add(Piece(2, 2))
        aiPiecesRepository.add(Piece(3, 3))
        validator = Validator(userPiecesRepository, aiPiecesRepository)
        aiPiecesService = AIService(aiPiecesRepository, userPiecesRepository, validator)
        aiPiecesService.addPiece()
        self.assertEqual(aiPiecesService.getList(), [Piece(0, 0), Piece(1, 1), Piece(2, 2), Piece(3, 3), Piece(4, 4)])

    def test_addBestPlayPiece(self):
        userPiecesRepository = Repository()
        aiPiecesRepository = Repository()
        aiPiecesRepository.add(Piece(0, 0))
        aiPiecesRepository.add(Piece(1, 1))
        validator = Validator(userPiecesRepository, aiPiecesRepository)
        aiPiecesService = AIService(aiPiecesRepository, userPiecesRepository, validator)
        aiPiecesService.addPiece()
        self.assertEqual(aiPiecesService.getList(), [Piece(0, 0), Piece(1, 1), Piece(2, 2)])
