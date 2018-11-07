from main.Constants import Constants
from main.model.Client import Client
from main.model.Movie import Movie
from main.model.Rental import Rental


class Printer:
    constant = Constants()

    def printMenu(self, menu):
        print(menu)
        print()
        for menuList in self.constant.getConstant(menu):
            print(menuList)
        print()
        print("Please choose the menu you want to use by inserting its command")

    def printSubmenu(self, submenu):
        print(submenu)
        print()
        for submenuList in self.constant.getConstant(submenu):
            print(submenuList)
        print()
        print("Command:")

    def printClient(self, client: "Client"):
        print(str(client))

    def printMovie(self, movie: "Movie"):
        print(str(movie))

    def printRental(self, rental: "Rental"):
        print(str(rental))
