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

    def printClient(self, client: "Client"):
        """
        Print client to console

        :param client: The client to print
        """
        print(str(client))

    def printMovie(self, movie: "Movie"):
        """
        Print movie to console

        :param movie: The movie to print
        """
        print(str(movie))

    def printRental(self, rental: "Rental"):
        """
        Print rental to console

        :param rental: The rental to print
        """
        print(str(rental))
