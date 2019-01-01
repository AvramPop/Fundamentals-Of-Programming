from src.Piece import Piece


class GameService:
    def __init__(self, userPiecesService, aiPiecesService) -> None:
        self.userPiecesService = userPiecesService
        self.aiPiecesService = aiPiecesService

    def isGameOver(self):
        """
        Checks whether game is over.
        """
        if self.winner() is None:
            return False
        return True

    def winner(self):
        """
        Return the winner.
        """
        for i in range(0, 15):
            for j in range(0, 15):
                value = None
                pool = None
                if Piece(i, j) in self.userPiecesService.getList():
                    value = 0
                    pool = self.userPiecesService.getList()
                if Piece(i, j) in self.aiPiecesService.getList():
                    value = 1
                    pool = self.aiPiecesService.getList()
                if value is not None:
                    if self.__isLineFromPoint(i, j, pool):
                        return value
        return None

    def __isLineFromPoint(self, i, j, pool):
        """
        Checks whether line starting from Piece(i, j) is a winner.
        """
        directionX = [-1, -1, -1, 0, 1, 1, 1, 0]
        directionY = [-1, 0, 1, 1, 1, 0, -1, -1]
        for k in range(0, 8):
            temporaryI = i
            temporaryJ = j
            consecutivePoints = 1
            consecutive = True
            inside = True
            while inside and consecutive and consecutivePoints != 5:
                temporaryI += directionX[k]
                temporaryJ += directionY[k]
                if 0 > temporaryI or 0 > temporaryJ or 14 < temporaryI or 14 < temporaryJ:
                    inside = False
                elif not Piece(temporaryI, temporaryJ) in pool:
                    consecutive = False
                else:
                    consecutivePoints += 1
            if consecutivePoints == 5:
                return True
        return False

