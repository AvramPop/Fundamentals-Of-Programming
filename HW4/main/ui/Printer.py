from main.Constants import Constants
from main.model.Client import Client
from main.model.Movie import Movie
from main.model.Rental import Rental


class Printer:
    """
    Class that prints stuff to console.
    """
    constant = Constants()

    def printMenu(self, menu):
        """
        Print the menu, if it exists in Constants

        :param menu: the menu to print
        """
        print(menu)
        print()
        for menuList in self.constant.getConstant(menu):
            print(menuList)
        print()
        print("Please choose the menu you want to use by inserting its command")

    def printSubmenu(self, submenu):
        """
        Print the menu, if it exists in Constants

        :param submenu: the submenu to print
        """
        print(submenu)
        print()
        for submenuList in self.constant.getConstant(submenu):
            print(submenuList)
        print()
        print("Command:")

    def printObject(self, plainObject):
        print(str(plainObject))

    def printList(self, listToPrint):
        for plainObject in listToPrint:
            self.printObject(plainObject)
