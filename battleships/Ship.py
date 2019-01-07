class Ship:

    def __init__(self, x, y, l, direction) -> None:
        self.__x = x
        self.__y = y
        self.__l = l
        self.__direction = direction

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getLength(self):
        return self.__l

    def getDirection(self):
        return self.__direction

    def __hits(self, x, y):
        print(self.__direction)
        print(self.getX(), self.getY())
        if self.__direction == 0:

            print(self.getX(), self.getY() - self.getLength())
            if self.getX() == x and y <= self.getY() and y > self.getY() - self.getLength():

                return True
        elif self.__direction == 1:
            print(self.getX() + self.getLength(), self.getY())
            if self.getY() == y and x >= self.getX() and x < self.getX() + self.getLength():

                return True
        elif self.__direction == 2:
            print(self.getX(), self.getY() + self.getLength())
            if self.getX() == x and y >= self.getY() and y < self.getY() + self.getLength():

                return True
        elif self.__direction == 3:
            print(self.getX() - self.getLength(), self.getY())
            if self.getY() == y and x <= self.getX() and x > self.getX() - self.getLength():

                return True
        return False

    def __eq__(self, ship: object) -> bool:
        shipX = ship.getX()
        shipY = ship.getY()
        c = 0
        while c < ship.getLength():
            if self.__hits(shipX, shipY):
                return True
            print(shipX, shipY)
            if ship.getDirection() == 0:
                shipX -= 1
            elif ship.getDirection() == 1:
                shipY += 1
            elif ship.getDirection() == 2:
                shipX += 1
            elif ship.getDirection() == 3:
                shipY -= 1
            c += 1
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)



