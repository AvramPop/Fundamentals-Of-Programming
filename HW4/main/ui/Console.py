from main.Constants import Constants
from main.Exception import ObjectNotInCollectionException, DatesNotOrderedException, InvalidDateFormatException, \
    ClientHasMoviesNotReturnedException, MovieNotAvailableException, MovieNotCurrentlyRentedByClientException, \
    MovieCurrentlyRentedException
from main.Stack import Stack
from main.Validator import Validator
from main.controller.ClientController import ClientController
from main.controller.MovieController import MovieController
from main.controller.RentalController import RentalController
from main.model.Client import Client
from main.model.Date import Date
from main.model.Movie import Movie
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo
from main.ui.Printer import Printer


class Console:
    printer = Printer()
    validator = Validator()
    constants = Constants()
    # clientRepo = ClientRepo()
    # movieRepo = MovieRepo()
    # rentalRepo = RentalRepo()
    clientController = ClientController(ClientRepo())
    movieController = MovieController(MovieRepo())
    rentalController = RentalController(RentalRepo())
    clientController.populateRepo()
    movieController.populateRepo()
    rentalController.populateRepo(movieController.getRepo(), clientController.getRepo())  # TODO do these really update as they should?
    undoStack = Stack()
    redoStack = Stack()
    # commandsGenerator = CommandsGenerator()

    def run(self):

        while True:
            self.printer.printMenu("mainMenu")
            menuChosen = input(">")
            if menuChosen == "manager":
                self.__managerMenu()
            elif menuChosen == "rental":
                self.__rentalMenu()
            elif menuChosen == "search":
                self.__searchMenu()
            elif menuChosen == "stats":
                self.__statsMenu()
            elif menuChosen == "exit":
                return
            else:
                print("Wrong input!")

    def __managerMenu(self):
        while True:
            self.printer.printMenu("managerMenu")
            menuChosen = input(">")
            if menuChosen == "client":
                self.__clientManager()
            elif menuChosen == "movie":
                self.__movieManager()
            elif menuChosen == "back":
                break
            else:
                print("Wrong input!")

    def __statsMenu(self):
        while True:
            self.printer.printSubmenu("statsMenu")
            optionInput = input(">")
            optionInputWordList = optionInput.split()
            if self.validator.isValidStatsQuery(optionInputWordList):
                self.__stats(optionInputWordList)
            elif optionInputWordList[0] == "back":
                break
            else:
                print("wrong input")

    def __searchMenu(self):
        while True:
            self.printer.printSubmenu("searchMenu")
            optionInput = input(">")
            optionInputWordList = optionInput.split()
            if self.validator.isValidSearchQuery(optionInputWordList):
                self.__search(optionInputWordList)
            elif optionInputWordList[0] == "back":
                break
            else:
                print("wrong input")

    def __rentalMenu(self):
        while True:
            self.printer.printSubmenu("rentalMenu")
            optionInput = input(">")
            optionInputWordList = optionInput.split()
            if optionInputWordList:
                if optionInputWordList[0] == "rent":
                    self.__rentMovie(optionInputWordList)
                elif optionInputWordList[0] == "return":
                    self.__returnMovie(optionInputWordList)
                elif optionInputWordList[0] == "list":
                    self.printer.printList(self.rentalController.getRentalList())
                elif optionInputWordList[0] == "back":
                    break
                else:
                    print("wrong input")
            else:
                print("wrong input")

    def __movieManager(self):
        while True:
            self.printer.printSubmenu("movieMenu")
            optionInput = input(">")
            optionInputWordList = optionInput.split()
            if optionInputWordList[0] == "list":
                self.__listMovie(optionInputWordList)
            elif optionInputWordList[0] == "remove":
                self.__removeMovie(optionInputWordList)
            elif optionInputWordList[0] == "update":
                self.__updateMovie(optionInputWordList)
            elif optionInputWordList[0] == "add":
                self.__addMovie(optionInputWordList)
            elif optionInputWordList[0] == "back":
                break
            else:
                print("wrong input")

    def __clientManager(self):
        while True:
            self.printer.printSubmenu("clientMenu")
            optionInput = input(">")
            optionInputWordList = optionInput.split()
            if optionInputWordList[0] == "list":
                self.__listClient(optionInputWordList)
            elif optionInputWordList[0] == "remove":
                self.__removeClient(optionInputWordList)
            elif optionInputWordList[0] == "update":
                self.__updateClient(optionInputWordList)
            elif optionInputWordList[0] == "add":
                self.__addClient(optionInputWordList)
            elif optionInputWordList[0] == "back":
                break
            else:
                print("wrong input")

    def __stats(self, optionInputWordList):
        if optionInputWordList[0] == "active":
            print("Most active clients:")
            self.printer.printList(
                self.rentalController.mostActiveClients(self.clientController.getRepo()))
        elif optionInputWordList[0] == "now":
            print("Movies now rented:")
            self.printer.printList(
                self.rentalController.moviesCurrentlyRented(self.movieController.getRepo()))
        elif optionInputWordList[0] == "late":
            print("Movies most passed due date:")
            self.printer.printList(self.rentalController.moviesPastDueDate(self.movieController.getRepo()))
        elif optionInputWordList[0] == "most" and optionInputWordList[2] == "times":
            print("Most rented movies by times rented:")
            self.printer.printList(self.rentalController.moviesMostRentedByTimesRented(self.movieController.getRepo()))
        elif optionInputWordList[0] == "most" and optionInputWordList[2] == "days":
            print("Most rented movies by times rented:")
            self.printer.printList(self.rentalController.moviesMostRentedByDays(self.movieController.getRepo()))

    def __search(self, optionInputWordList):
        if optionInputWordList[2] == "name":
            self.printer.printList(self.clientController.listOfClientsWithName(optionInputWordList[3]))
        elif optionInputWordList[2] == "title":
            self.printer.printList(self.movieController.listOfMoviesWithTitle(optionInputWordList[3]))
        elif optionInputWordList[2] == "description":
            self.printer.printList(self.movieController.listOfMoviesWithDescription(optionInputWordList[3]))
        elif optionInputWordList[2] == "genre":
            self.printer.printList(self.movieController.listOfMoviesWithGenre(optionInputWordList[3]))

    def __returnMovie(self, optionInputWordList):
        if optionInputWordList[1].isdigit():
            if self.clientController.hasClientWithId(int(optionInputWordList[1])):
                if optionInputWordList[2].isdigit():
                    if self.movieController.hasMovieWithId(int(optionInputWordList[2])):
                        try:
                            self.rentalController.returnMovieByClient(int(optionInputWordList[1]),
                                                                      int(optionInputWordList[2]))
                        except MovieNotCurrentlyRentedByClientException as movieNotCurrentlyRentedByClientException:
                            print("movie with id #", optionInputWordList[2], "not rented by client with #",
                                  optionInputWordList[1])
                        else:
                            print("Movie with id #", optionInputWordList[2],
                                  "successfully returned by client with id #", optionInputWordList[1])
                    else:
                        print("movie with id #", optionInputWordList[2], "not found")
                else:
                    print("wrong input")
            else:
                print("client with id #", optionInputWordList[1], "not found")
        else:
            print("wrong input")

    def __rentMovie(self, optionInputWordList):
        if len(optionInputWordList) == 6:
            if optionInputWordList[1].isdigit():
                if self.clientController.hasClientWithId(int(optionInputWordList[1])):
                    if optionInputWordList[2].isdigit():
                        if self.movieController.hasMovieWithId(int(optionInputWordList[2])):
                            if optionInputWordList[3].isdigit() and optionInputWordList[4].isdigit() and \
                                    optionInputWordList[5].isdigit():
                                try:
                                    dueDate = Date(int(optionInputWordList[3]),
                                                   int(optionInputWordList[4]),
                                                   int(optionInputWordList[5]))
                                except InvalidDateFormatException as invalidDateFormatException:
                                    print("Invalid date format")
                                else:
                                    try:
                                        self.rentalController.rentMovieByClientUntilDate(int(optionInputWordList[1]),
                                                                                         int(optionInputWordList[2]),
                                                                                         dueDate,
                                                                                         self.movieController.getRepo(),
                                                                                         self.clientController.getRepo())
                                    except DatesNotOrderedException as datesNotOrderedException:
                                        print("The due date cannot be before the rental date")
                                    except ClientHasMoviesNotReturnedException as clientHasMoviesNotReturnedException:
                                        print("Client #", optionInputWordList[1], "has passed due date for movies")
                                    except MovieNotAvailableException as movieNotAvailableException:
                                        print("Movie #", optionInputWordList[2], "is not available")
                                    else:
                                        print("Movie #", optionInputWordList[2], "successfully rented by client #",
                                              optionInputWordList[1], "until", str(dueDate))
                            else:
                                print("wrong input")
                        else:
                            print("Movie with id", optionInputWordList[2], "not found")
                    else:
                        print("wrong input")
                else:
                    print("Client with id", optionInputWordList[1], "not found")
            else:
                print("wrong input")
        else:
            print("wrong input")

    def __addMovie(self, optionInputWordList):
        self.movieController.addMovie(Movie(optionInputWordList[1], optionInputWordList[2], optionInputWordList[3]))
        print("Successfully added movie", optionInputWordList[1])

    def __updateMovie(self, optionInputWordList):
        if self.validator.isValidUpdateQueryWithNumberOfElements(optionInputWordList, 5):
            try:
                self.movieController.updateMovieWithId(int(optionInputWordList[1]),
                                                       Movie(optionInputWordList[2], optionInputWordList[3],
                                                             optionInputWordList[4]))
            except ObjectNotInCollectionException as objectNotInCollectionException:
                print("Movie with id", optionInputWordList[1], "not found")
            else:
                print("Successfully updated movie #", optionInputWordList[1])
        else:
            print("wrong input")

    def __removeMovie(self, optionInputWordList):
        if self.validator.isValidRemoveQuery(optionInputWordList):
            try:
                self.movieController.removeMovieWithId(int(optionInputWordList[1]), self.rentalController.getRepo())
            except ObjectNotInCollectionException as objectNotInCollectionException:
                print("Movie with id", optionInputWordList[1], "not found")
            except MovieCurrentlyRentedException as movieCurrentlyRentedException:
                print("Movie with id #", optionInputWordList[1], "is currently rented. Couldn't delete")
            else:
                print("Successfully removed movie #", optionInputWordList[1])
        else:
            print("wrong input")

    def __listMovie(self, optionInputWordList):
        if len(optionInputWordList) == 1:
            self.printer.printList(self.movieController.getMovieList())
        elif len(optionInputWordList) == 2:
            try:
                if optionInputWordList[1].isdigit():
                    self.printer.printObject(self.movieController.getMovieWithId(int(optionInputWordList[1])))
                else:
                    print("wrong input")
            except ObjectNotInCollectionException as objectNotInCollectionException:
                print("Movie with id", optionInputWordList[1], "not found")
        else:
            print("Wrong input")

    def __addClient(self, optionInputWordList):
        self.clientController.addClient(Client(optionInputWordList[1]))
        print("Successfully added client", optionInputWordList[1])

    def __updateClient(self, optionInputWordList):
        if self.validator.isValidUpdateQueryWithNumberOfElements(optionInputWordList, 3):
            try:
                self.clientController.updateClientWithId(int(optionInputWordList[1]),
                                                         Client(optionInputWordList[2]))
            except ObjectNotInCollectionException as objectNotInCollectionException:
                print("Client with id", optionInputWordList[1], "not found")
            else:
                print("Successfully updated client #", optionInputWordList[1])
        else:
            print("wrong input")

    def __removeClient(self, optionInputWordList):
        if self.validator.isValidRemoveQuery(optionInputWordList):
            try:
                self.clientController.removeClientWithId(int(optionInputWordList[1]), self.rentalController.getRepo())
            except ClientHasMoviesNotReturnedException as clientHasMoviesNotReturnedException:
                print("Client with id #", optionInputWordList[1], "has movies not returned. Couldn't delete")
            except ObjectNotInCollectionException as objectNotInCollectionException:
                print("Client with id", optionInputWordList[1], "not found")
            else:
                print("Successfully removed client #", optionInputWordList[1])
        else:
            print("wrong input")

    def __listClient(self, optionInputWordList):
        if len(optionInputWordList) == 1:
            self.printer.printList(self.clientController.getClientList())
        elif len(optionInputWordList) == 2:
            try:
                if optionInputWordList[1].isdigit():
                    self.printer.printObject(self.clientController.getClientWithId(int(optionInputWordList[1])))
                else:
                    print("wrong input")
            except ObjectNotInCollectionException as objectNotInCollectionException:
                print("Client with id #", optionInputWordList[1], "not found")
        else:
            print("Wrong input")

