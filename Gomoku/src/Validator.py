class Validator:
    def __init__(self, userPiecesRepository, aiPiecesRepository) -> None:
        self.userPiecesRepository = userPiecesRepository
        self.aiPiecesRepository = aiPiecesRepository

    def isValid(self, piece):
        if not 0 <= piece.getX() <= 14 or not 0 <= piece.getY() <= 14:
            return False
        if piece in self.userPiecesRepository.getList() or piece in self.aiPiecesRepository.getList():
            return False
        return True
