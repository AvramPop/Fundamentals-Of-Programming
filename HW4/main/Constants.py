from main.Exception import ConstantNotFoundException
import datetime

from main.model.Date import Date


class Constants:
    __now = datetime.datetime.now()
    __mainMenuCommandsMenu = ("1. Management Menu - manager", "2. Rentals Menu - rental", "3. Search Menu - search", "4. Statistics Menu - stats", "5. Exit - exit")
    __managerCommandsMenu = ("1. Client List - client", "2. Movie List - movie", "3. Back - back")
    __clientManagementCommandsMenu = ("1. List All - list", "2. List Client With Name - list <name>", "3. Remove Client With Name - remove <name>", "4. Update Client With Name - update <name> <new name>", "5. Add Client - add <client name>", "6. Back - back")
    __movieManagementCommandsMenu = ("1. List All - list", "2. List Movie With Title - list <title>", "3. Remove Movie With Title - remove <title>", "4. Update Movie With Title - update <title> <new title> <new description> <new genre>", "5. Add Movie - add <movie name> <movie description> <movie genre>", "6. Back - back")
    __rentCommandsMenu = ("1. Rent - rent <client name> <movie title> <due date>", "2. Return movie - return <client name> <movie title>", "3. Back - back")
    __mainMenuCommands = ("manager", "rental", "search", "exit", "stats")
    __constants = ("mainMenu", "mainMenuCommands", "managerMenu", "clientMenu", "movieMenu", "rentalMenu")

    def currentDay(self):
        return Date(self.__now.day, self.__now.month, self.__now.year)

    def isConstant(self, constant):
        return constant in self.__constants

    def getConstant(self, constantName):
        if self.isConstant(constantName):
            if constantName == "mainMenu":
                return self.__mainMenuCommandsMenu
            if constantName == "mainMenuCommands":
                return self.__mainMenuCommands
            elif constantName == "managerMenu":
                return self.__managerCommandsMenu
            elif constantName == "clientMenu":
                return self.__clientManagementCommandsMenu
            elif constantName == "movieMenu":
                return self.__movieManagementCommandsMenu
            elif constantName == "rentalMenu":
                return self.__rentCommandsMenu
        else:
            raise ConstantNotFoundException
