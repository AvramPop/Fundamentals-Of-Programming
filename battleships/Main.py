from Console import Console
from GameService import GameService
from HitRepo import HitRepo
from HitValidator import HitValidator
from ShipRepo import ShipRepo
from ShipService import ShipService
from ShipValidator import ShipValidator
from Test import Test


class Main:
    def __init__(self) -> None:
        super().__init__()
        shipRepo0 = ShipRepo()
        shipRepo1 = ShipRepo()
        hitRepo = HitRepo()
        shipValidator = ShipValidator()
        hitValidator = HitValidator()
        shipService0 = ShipService(shipRepo0, shipValidator)
        shipService1 = ShipService(shipRepo1, shipValidator)
        gameService = GameService(shipRepo0, shipRepo1,
                                  hitRepo, shipValidator, hitValidator)
        console0 = Console(shipService0, gameService)
        console1 = Console(shipService1, gameService)

    def run(self):
        print("Hello, World!")

test = Test()
test.runTests()

main = Main()
main.run()
