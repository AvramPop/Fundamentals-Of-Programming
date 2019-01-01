from src.Exceptions import ValidException
from src.Piece import Piece


class UserService:
    def __init__(self, userPiecesRepository, validator) -> None:
        self.userPiecesRepository = userPiecesRepository
        self.validator = validator

    def addPiece(self, x, y):
        """
        Add Piece(x, y) if not already on board.
        """
        newPiece = Piece(x, y)
        if self.validator.isValid(newPiece):
            self.userPiecesRepository.add(newPiece)
        else:
            raise ValidException

    def isValidMove(self, x, y):
        return self.validator.isValid(Piece(x, y))

    def getList(self):
        return self.userPiecesRepository.getList()
