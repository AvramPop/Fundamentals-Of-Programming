from Exception import ValidException


class ShipValidator:
    def validateShip(self, ship):
        if ship.getX() > 7 or ship.getX() < 0 or ship.getY() > 7 or ship.getY() < 0:
            raise ValidException
