from unittest import TestCase

from src.AIService import AIService
from src.GameService import GameService
from src.Piece import Piece
from src.Repository import Repository
from src.UserService import UserService
from src.Validator import Validator


class TestGameService(TestCase):

    def test_isGameOver(self):
        userPiecesRepository = Repository()
        userPiecesRepository.add(Piece(0, 0))
        userPiecesRepository.add(Piece(1, 1))
        userPiecesRepository.add(Piece(2, 2))
        userPiecesRepository.add(Piece(3, 3))
        userPiecesRepository.add(Piece(4, 4))
        aiPiecesRepository = Repository()
        validator = Validator(userPiecesRepository, aiPiecesRepository)
        userPiecesService = UserService(userPiecesRepository, validator)
        aiPiecesService = AIService(aiPiecesRepository, userPiecesRepository, validator)
        gameService = GameService(userPiecesService, aiPiecesService)
        self.assertEqual(gameService.isGameOver(), True)
        userPiecesRepository = Repository()
        userPiecesRepository.add(Piece(0, 0))
        userPiecesRepository.add(Piece(1, 1))
        userPiecesRepository.add(Piece(3, 3))
        userPiecesRepository.add(Piece(4, 4))
        aiPiecesRepository = Repository()
        validator = Validator(userPiecesRepository, aiPiecesRepository)
        userPiecesService = UserService(userPiecesRepository, validator)
        aiPiecesService = AIService(aiPiecesRepository, userPiecesRepository, validator)
        gameService = GameService(userPiecesService, aiPiecesService)
        self.assertEqual(gameService.isGameOver(), False)

    def test_winner(self):
        userPiecesRepository = Repository()
        userPiecesRepository.add(Piece(0, 0))
        userPiecesRepository.add(Piece(1, 1))
        userPiecesRepository.add(Piece(2, 2))
        userPiecesRepository.add(Piece(3, 3))
        userPiecesRepository.add(Piece(4, 4))
        aiPiecesRepository = Repository()
        validator = Validator(userPiecesRepository, aiPiecesRepository)
        userPiecesService = UserService(userPiecesRepository, validator)
        aiPiecesService = AIService(aiPiecesRepository, userPiecesRepository, validator)
        gameService = GameService(userPiecesService, aiPiecesService)
        self.assertEqual(gameService.winner(), 0)
