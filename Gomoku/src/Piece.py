class Piece:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __eq__(self, otherPiece) -> bool:
        if not isinstance(otherPiece, Piece):
            return False
        if self.__x != otherPiece.getX() or self.__y != otherPiece.getY():
            return False
        return True

    def __str__(self) -> str:
        return "Piece: " + str(self.getX()) + " " + str(self.getY())



