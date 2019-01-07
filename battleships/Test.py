from Ship import Ship


class Test:
    def runTests(self):
        self.testShipsAreEqual()
        print("Tests ran successfully")

    def testShipsAreEqual(self):
        ship1 = Ship(3, 3, 3, 1)
        ship2 = Ship(2, 4, 2, 2)
        assert ship1 != ship2
        ship1 = Ship(0, 3, 2, 1)
        ship2 = Ship(2, 4, 2, 2)
        assert ship1 == ship2

