class Console:

    def __init__(self, shipService, gameService) -> None:
        self.__shipService = shipService
        self.__gameService = gameService
        self.__commandsDictionary = {"add": self.__UIAddShip}

    def __UIAddShip(self, parts):
        x = int(parts[0])
        y = int(parts[1])
        l = int(parts[2])
        direction = int(parts[3])
        self.__shipService.addShip(x, y, l, direction)

    def run(self):
        while True:
            userInput = input(">")
            userInput = userInput.strip()
            parts = userInput.split()
            if userInput == "exit":
                print("exit")
                return
            elif parts[0] in self.__commandsDictionary:
                try:
                    self.__commandsDictionary[parts[0]](parts[1:])
                except ValueError:
                    print("Invalid numerical format")
            else:
                print("wrong input")
