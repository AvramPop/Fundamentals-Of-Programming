import random

from src.Piece import Piece


class AIService:
    def __init__(self, aiPiecesRepository, userPiecesRepository, validator) -> None:
        self.aiPiecesRepository = aiPiecesRepository
        self.validator = validator
        self.userPiecesRepository = userPiecesRepository

    def addPiece(self):
        if not self.canBlockUserWin()[0]:
            # block user win
            self.moveToWin()
        else:
            # move to win
            self.blockUserWin(self.canBlockUserWin()[1], self.canBlockUserWin()[2], self.canBlockUserWin()[3])


    def canBlockUserWin(self):
        directionX = [-1, -1, -1, 0, 1, 1, 1, 0]
        directionY = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(0, 15):
            for j in range(0, 15):
                for k in range(0, 8):
                    temporaryI = i + directionX[k]
                    temporaryJ = j + directionY[k]
                    count = 0
                    moves = 5
                    while moves > 0:
                        if Piece(temporaryI, temporaryJ) in self.userPiecesRepository.getList():
                            count += 1
                        temporaryI += directionX[k]
                        temporaryJ += directionY[k]
                        moves -= 1
                    print(i, j, k, count)
                    if count == 4:
                        for temp in range(0, 5):
                            if (Piece(i + temp * directionX[k], j + temp * directionY[k]) not in self.aiPiecesRepository.getList() and Piece(i + temp * directionX[k], j + temp * directionY[k]) not in self.userPiecesRepository.getList()) and (Piece(i + temp * directionX[k], j + temp * directionY[k]) not in self.aiPiecesRepository.getList() and Piece(i + temp * directionX[k], j + temp * directionY[k]) not in self.userPiecesRepository.getList()):
                                return True, i, j, k
        return False, None

    def blockUserWin(self, startX, startY, direction):
        directionX = [-1, -1, -1, 0, 1, 1, 1, 0]
        directionY = [-1, 0, 1, 1, 1, 0, -1, -1]
        for k in range(0, 5):
            if self.validator.isValid(Piece(startX + k * directionX[direction], startY + k * directionY[direction])):
                self.aiPiecesRepository.add(Piece(startX + k * directionX[direction], startY + k * directionY[direction]))
                return
            elif self.validator.isValid(Piece(startX + k * directionX[abs(4 - direction)], startY + k * directionY[abs(4 - direction)])):
                self.aiPiecesRepository.add(Piece(startX + k * directionX[abs(4 - direction)], startY + k * directionY[abs(4 - direction)]))
                return

    def moveToWin(self):
        directionX = [-1, -1, -1, 0, 1, 1, 1, 0]
        directionY = [-1, 0, 1, 1, 1, 0, -1, -1]
        if self.aiPiecesRepository.getList():
            piecesSorted = self.aiPiecesRepository.getList()
            self.sortListByObjectAttribute(piecesSorted, lambda a, b: True if a < b else False,
                                           lambda pieceTemporary: self.lengthFromPiece(pieceTemporary)[0])
            for piece in piecesSorted:
                maximumLength = self.lengthFromPiece(piece)[0]
                maximumDirection = self.lengthFromPiece(piece)[1]
                print(str(piece))
                print(self.lengthFromPiece(piece))
                print(maximumLength)
                newX = piece.getX() + maximumLength * directionX[maximumDirection]
                newY = piece.getY() + maximumLength * directionY[maximumDirection]
                if self.validator.isValid(Piece(newX, newY)):
                    self.aiPiecesRepository.add(Piece(newX, newY))
                    return
                newX = piece.getX() - maximumLength * directionX[maximumDirection]
                newY = piece.getY() - maximumLength * directionY[maximumDirection]
                if self.validator.isValid(Piece(newX, newY)):
                    self.aiPiecesRepository.add(Piece(newX, newY))
                    return

        xPool, yPool = self.generatePools()

        x = random.choice(xPool)
        y = random.choice(yPool)

        self.aiPiecesRepository.add(Piece(x, y))

    def lengthFromPiece(self, piece):
        directionX = [-1, -1, -1, 0, 1, 1, 1, 0]
        directionY = [-1, 0, 1, 1, 1, 0, -1, -1]
        maximumConsecutivePoints = 0
        direction = -1
        for k in range(0, 8):
            temporaryI = piece.getX()
            temporaryJ = piece.getY()
            consecutivePoints = 1
            consecutive = True
            inside = True
            while inside and consecutive:
                temporaryI += directionX[k]
                temporaryJ += directionY[k]
                if 0 > temporaryI or 0 > temporaryJ or 14 < temporaryI or 14 < temporaryJ:
                    inside = False
                elif not Piece(temporaryI, temporaryJ) in self.aiPiecesRepository.getList():
                    consecutive = False
                else:
                    consecutivePoints += 1
            if consecutivePoints > maximumConsecutivePoints:
                maximumConsecutivePoints = consecutivePoints
                direction = k
        return maximumConsecutivePoints, direction

    def generatePools(self):
        xPool = []
        yPool = []
        for i in range(0, 15):
            for j in range(0, 15):
                if self.validator.isValid(Piece(i, j)):
                    xPool.append(i)
                    yPool.append(j)
        return xPool, yPool

    def getList(self):
        return self.aiPiecesRepository.getList()

    def sortListByObjectAttribute(self, listToSort, compareFunction, getAttribute):
        for i in range(len(listToSort) - 1):
            minimumIndex = i
            for j in range(i + 1, len(listToSort)):
                if compareFunction(getAttribute(listToSort[j]), getAttribute(listToSort[minimumIndex])):
                    minimumIndex = j
            if minimumIndex != i:
                temp = listToSort[minimumIndex]
                listToSort[minimumIndex] = listToSort[i]
                listToSort[i] = temp
