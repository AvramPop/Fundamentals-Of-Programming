import random

from src.Piece import Piece


class AIService:
    def __init__(self, aiPiecesRepository, userPiecesRepository, validator) -> None:
        self.aiPiecesRepository = aiPiecesRepository
        self.validator = validator
        self.userPiecesRepository = userPiecesRepository
        self.directionX = [-1, -1, -1, 0, 1, 1, 1, 0]
        self.directionY = [-1, 0, 1, 1, 1, 0, -1, -1]

    def addPiece(self):
        """
        Add piece to board in best place, in the following order.
        First, move to win. If not, but user can win, block.
        Otherwise, continue the longest line done yet.
        """
        if self.__canMoveToWin():
            self.__moveToWin()
        elif self.__canBlockUserWin():
            self.__blockUserWin()
        else:
            self.__moveBestPiece()

    def __moveBestPiece(self):
        """
        Move piece following the longest line already done.
        """
        if self.aiPiecesRepository.getList():
            piecesSorted = self.aiPiecesRepository.getList()
            self.__sortListByObjectAttribute(piecesSorted, lambda a, b: True if a < b else False,
                                             lambda pieceTemporary: self.__maximumLengthFromPiece(pieceTemporary)[0])
            for piece in piecesSorted:
                maximumDirection = self.__maximumLengthFromPiece(piece)[1]
                newX = piece.getX() + self.directionX[maximumDirection]
                newY = piece.getY() + self.directionY[maximumDirection]
                if self.validator.isValid(Piece(newX, newY)):
                    self.aiPiecesRepository.add(Piece(newX, newY))
                    return
                newX = piece.getX() - self.directionX[maximumDirection]
                newY = piece.getY() - self.directionY[maximumDirection]
                if self.validator.isValid(Piece(newX, newY)):
                    self.aiPiecesRepository.add(Piece(newX, newY))
                    return

            for piece in piecesSorted:
                for direction in range(0, 8):
                    newX = piece.getX() + self.directionX[direction]
                    newY = piece.getY() + self.directionY[direction]
                    if self.validator.isValid(Piece(newX, newY)):
                        self.aiPiecesRepository.add(Piece(newX, newY))
                        return
        xPool, yPool = self.__generatePools()
        x = random.choice(xPool)
        y = random.choice(yPool)
        self.aiPiecesRepository.add(Piece(x, y))

    def __maximumLengthFromPiece(self, piece):
        """
        Find the maximum line that can be done starting from piece.
        """
        maximumLength = 0
        directionOfMaximum = None
        startX = piece.getX()
        startY = piece.getY()
        count = 0
        for k in range(0, 8):
            while Piece(startX, startY) in self.aiPiecesRepository.getList():
                count += 1
                startX += self.directionX[k]
                startY += self.directionY[k]
            if count > maximumLength:
                maximumLength = count
                directionOfMaximum = k
        return maximumLength, directionOfMaximum

    def __generatePools(self):
        """
        Generate the pools of available empty positions.1
        """
        xPool = []
        yPool = []
        for i in range(0, 15):
            for j in range(0, 15):
                if self.validator.isValid(Piece(i, j)):
                    xPool.append(i)
                    yPool.append(j)
        return xPool, yPool

    def __canBlockUserWin(self):
        """
        Check whether user win can be blocked.
        """
        for i in range(0, 15):
            for j in range(0, 15):
                for k in range(0, 8):
                    if self.__areFiveConsecutiveWithOneEmpty(i, j, k, 0):
                        return True
        return False

    def __canMoveToWin(self):
        """
        Check whether can move to win.
        :return:
        """
        for i in range(0, 15):
            for j in range(0, 15):
                for k in range(0, 8):
                    if self.__areFiveConsecutiveWithOneEmpty(i, j, k, 1):
                        return True
        return False

    def __moveToWin(self):
        """
        Put piece to complete 5 length row.
        """
        for i in range(0, 15):
            for j in range(0, 15):
                for k in range(0, 8):
                    if self.__areFiveConsecutiveWithOneEmpty(i, j, k, 1):
                        self.aiPiecesRepository.add(Piece(self.__emptyPlaceInLine(i, j, k)[0], self.__emptyPlaceInLine(i, j, k)[1]))
                        return

    def __blockUserWin(self):
        """
        Block user win by placing piece to block row.
        """
        for i in range(0, 15):
            for j in range(0, 15):
                for k in range(0, 8):
                    if self.__areFiveConsecutiveWithOneEmpty(i, j, k, 0):
                        self.aiPiecesRepository.add(Piece(self.__emptyPlaceInLine(i, j, k)[0], self.__emptyPlaceInLine(i, j, k)[1]))
                        return

    def __areFiveConsecutiveWithOneEmpty(self, x, y, direction, value):
        """
        Checks whether there is a line of values value starting from (x, y) in direction of length 5 having a empty space.
        """
        moves = 5
        piecesWithValue = 0
        neutralPieces = 0
        while moves > 0:
            if x < 0 or x > 14 or y < 0 or y > 14:
                return False
            if value == 0:
                if Piece(x, y) in self.userPiecesRepository.getList():
                    piecesWithValue += 1
                elif Piece(x, y) not in self.aiPiecesRepository.getList():
                    neutralPieces += 1
            else:
                if Piece(x, y) in self.aiPiecesRepository.getList():
                    piecesWithValue += 1
                elif Piece(x, y) not in self.userPiecesRepository.getList():
                    neutralPieces += 1
            x += self.directionX[direction]
            y += self.directionY[direction]
            moves -= 1
        if piecesWithValue == 4 and neutralPieces == 1:
            return True
        else:
            return False

    def __emptyPlaceInLine(self, startX, startY, direction):
        """
        Find the empty place in line of 5 from (startX, startY) in direction.
        """
        while True:
            if Piece(startX, startY) not in self.userPiecesRepository.getList() and Piece(startX, startY) not in self.aiPiecesRepository.getList():
                return startX, startY
            startX += self.directionX[direction]
            startY += self.directionY[direction]

    def getList(self):
        return self.aiPiecesRepository.getList()

    def __sortListByObjectAttribute(self, listToSort, compareFunction, getAttribute):
        """
        Sort listToSort via compareFunction by getAttribute.
        """
        for i in range(len(listToSort) - 1):
            minimumIndex = i
            for j in range(i + 1, len(listToSort)):
                if compareFunction(getAttribute(listToSort[j]), getAttribute(listToSort[minimumIndex])):
                    minimumIndex = j
            if minimumIndex != i:
                temp = listToSort[minimumIndex]
                listToSort[minimumIndex] = listToSort[i]
                listToSort[i] = temp
