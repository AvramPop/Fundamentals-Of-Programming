class Validator:
    def __init__(self, userPiecesRepository, aiPiecesRepository) -> None:
        self.__userPiecesRepository = userPiecesRepository
        self.__aiPiecesRepository = aiPiecesRepository

    def isValid(self, piece):
        """
        Check whether piece(x, y) can be placed on board.
        """
        if not 0 <= piece.getX() <= 14 or not 0 <= piece.getY() <= 14:
            return False
        if (piece in self.__userPiecesRepository.getList()) or (piece in self.__aiPiecesRepository.getList()):
            return False
        return True
