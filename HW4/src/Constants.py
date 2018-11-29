from src.Exception import ConstantNotFoundException
import datetime

from src.Date import Date


class Constants:
    __now = datetime.datetime.now()
    __mainMenuCommandsMenu = ("1. Management Menu - manager", "2. Rentals Menu - rental", "3. Search Menu - search", "4. Statistics Menu - stats", "5. Exit - exit")
    __managerCommandsMenu = ("1. Client List - client", "2. Movie List - movie", "3. Back - back")
    __clientManagementCommandsMenu = ("1. List All - list", "2. List Client With Id - list <client id>", "3. Remove Client With Id - remove <client id>", "4. Update Client With Id - update <client id> <new name>", "5. Add Client - add <client name>", "6. Back - back")
    __movieManagementCommandsMenu = ("1. List All - list", "2. List Movie With Id - list <movie id>", "3. Remove Movie With Id - remove <movie id>", "4. Update Movie With Id - update <movie id> <new title> <new description> <new genre>", "5. Add Movie - add <movie name> <movie description> <movie genre>", "6. Back - back")
    __rentCommandsMenu = ("1. Rent - rent <client id> <movie id> <due date>", "2. Return movie - return <client id> <movie id>", "3. List all - list", "4. Back - back")
    __mainMenuCommands = ("manager", "rental", "search", "exit", "stats")
    __searchCommandsMenu = ("1. Search client by name - search client name <name>", "2. Search movie by title - search movie title <title>", "3. Search movie by genre - search movie genre <genre>", "4. Search movie by description - search movie description <description>")
    __statsCommandsMenu = ("1. List most times rented movies - most rented times", "2. List most days rented movies - most rented days", "3. List most active clients - active clients", "4. List all rented movies - now rented", "5. List all late rentals - late rentals", "6. Back - back")
    __constants = ("mainMenu", "mainMenuCommands", "managerMenu", "clientMenu", "statsMenu", "movieMenu", "rentalMenu", "searchMenu")

    def currentDay(self):
        """
        :return: current day in own Date format (day, month, year)
        """
        return Date(self.__now.day, self.__now.month, self.__now.year)

    def isConstant(self, constant):
        return constant in self.__constants

    def getConstant(self, constantName):
        """
        Return constant with constant name
        """
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
            elif constantName == "searchMenu":
                return self.__searchCommandsMenu
            elif constantName == "statsMenu":
                return self.__statsCommandsMenu
        else:
            raise ConstantNotFoundException
