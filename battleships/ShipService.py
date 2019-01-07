from Ship import Ship


class ShipService:

    def __init__(self, shipRepo, shipValidator) -> None:
        self.__shipRepo = shipRepo
        self.__shipValidator = shipValidator

    def addShip(self, x, y, l, direction):
        ship = Ship(x, y, l, direction)
        self.__shipValidator.validateShip(ship)
        self.__shipRepo.add(ship)

