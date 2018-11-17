from main.Constants import Constants
from main.Exception import ObjectNotInCollectionException, DatesNotOrderedException, InvalidDateFormatException, \
    ClientHasMoviesNotReturnedException, MovieNotAvailableException, MovieNotCurrentlyRentedByClientException, \
    MovieCurrentlyRentedException
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
    clientRepo = ClientRepo()
    movieRepo = MovieRepo()
    rentalRepo = RentalRepo()
    clientController = ClientController(clientRepo)
    movieController = MovieController(movieRepo)
    rentalController = RentalController(rentalRepo)
    clientController.populateRepo()
    movieController.populateRepo()
    rentalController.populateRepo(movieController.getRepo(), clientController.getRepo())

    def run(self):  # TODO refactor this ugly thing

        while True:
            self.printer.printMenu("mainMenu")
            menuChosen = input(">")
            if menuChosen == "manager":
                while True:
                    self.printer.printMenu("managerMenu")
                    menuChosen = input(">")
                    if menuChosen == "client":
                        while True:
                            self.printer.printSubmenu("clientMenu")
                            optionInput = input(">")
                            optionInputWordList = optionInput.split()
                            if optionInputWordList[0] == "list":
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
                            elif optionInputWordList[0] == "remove":
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
                            elif optionInputWordList[0] == "update":
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
                            elif optionInputWordList[0] == "add":
                                self.clientController.addClient(Client(optionInputWordList[1]))
                                print("Successfully added client", optionInputWordList[1])
                            elif optionInputWordList[0] == "back":
                                break
                            else:
                                print("wrong input")
                    elif menuChosen == "movie":
                        while True:
                            self.printer.printSubmenu("movieMenu")
                            optionInput = input(">")
                            optionInputWordList = optionInput.split()
                            if optionInputWordList[0] == "list":
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
                            elif optionInputWordList[0] == "remove":
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
                            elif optionInputWordList[0] == "update":
                                if self.validator.isValidUpdateQueryWithNumberOfElements(optionInputWordList, 5):
                                    try:
                                        self.movieController.updateMovieWithId(int(optionInputWordList[1]), Movie(optionInputWordList[2], optionInputWordList[3], optionInputWordList[4]))
                                    except ObjectNotInCollectionException as objectNotInCollectionException:
                                        print("Movie with id", optionInputWordList[1], "not found")
                                    else:
                                        print("Successfully updated movie #", optionInputWordList[1])
                                else:
                                    print("wrong input")
                            elif optionInputWordList[0] == "add":
                                self.movieController.addMovie(Movie(optionInputWordList[1], optionInputWordList[2], optionInputWordList[3]))
                                print("Successfully added movie", optionInputWordList[1])
                            elif optionInputWordList[0] == "back":
                                break
                            else:
                                print("wrong input")
                    elif menuChosen == "back":
                        break
                    else:
                        print("Wrong input!")
            elif menuChosen == "rental":
                while True:
                    self.printer.printSubmenu("rentalMenu")
                    optionInput = input(">")
                    optionInputWordList = optionInput.split()
                    if optionInputWordList:
                        if optionInputWordList[0] == "rent":
                            if len(optionInputWordList) == 6:
                                if optionInputWordList[1].isdigit():
                                    if self.clientController.hasClientWithId(int(optionInputWordList[1])):
                                        if optionInputWordList[2].isdigit():
                                            if self.movieController.hasMovieWithId(int(optionInputWordList[2])):
                                                if optionInputWordList[3].isdigit() and optionInputWordList[4].isdigit() and optionInputWordList[5].isdigit():
                                                    try:
                                                        dueDate = Date(int(optionInputWordList[3]),
                                                                       int(optionInputWordList[4]),
                                                                       int(optionInputWordList[5]))
                                                    except InvalidDateFormatException as invalidDateFormatException:
                                                        print("Invalid date format")
                                                    else:
                                                        try:
                                                            self.rentalController.rentMovieByClientUntilDate(int(optionInputWordList[1]), int(optionInputWordList[2]), dueDate, self.movieController.getRepo(), self.clientController.getRepo())
                                                        except DatesNotOrderedException as datesNotOrderedException:
                                                            print("The due date cannot be before the rental date")
                                                        except ClientHasMoviesNotReturnedException as clientHasMoviesNotReturnedException:
                                                            print("Client #", optionInputWordList[1], "has passed due date for movies")
                                                        except MovieNotAvailableException as movieNotAvailableException:
                                                            print("Movie #", optionInputWordList[2], "is not available")
                                                        else:
                                                            print("Movie #", optionInputWordList[2], "successfully rented by client #", optionInputWordList[1], "until", str(dueDate))
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
                        elif optionInputWordList[0] == "return":
                            if optionInputWordList[1].isdigit():
                                if self.clientController.hasClientWithId(int(optionInputWordList[1])):
                                    if optionInputWordList[2].isdigit():
                                        if self.movieController.hasMovieWithId(int(optionInputWordList[2])):
                                            try:
                                                self.rentalController.returnMovieByClient(int(optionInputWordList[1]), int(optionInputWordList[2]))
                                            except MovieNotCurrentlyRentedByClientException as movieNotCurrentlyRentedByClientException:
                                                print("movie with id #", optionInputWordList[2], "not rented by client with #", optionInputWordList[1])
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
                        elif optionInputWordList[0] == "list":
                            self.printer.printList(self.rentalController.getRentalList())
                        elif optionInputWordList[0] == "back":
                            break
                        else:
                            print("wrong input")
                    else:
                        print("wrong input")
            elif menuChosen == "search":
                while True:
                    self.printer.printSubmenu("searchMenu")
                    optionInput = input(">")
                    optionInputWordList = optionInput.split()
                    if self.validator.isValidSearchQuery(optionInputWordList):
                        if optionInputWordList[2] == "name":
                            self.printer.printList(self.clientController.listOfClientsWithName(optionInputWordList[3]))
                        elif optionInputWordList[2] == "title":
                            self.printer.printList(self.movieController.listOfMoviesWithTitle(optionInputWordList[3]))
                        elif optionInputWordList[2] == "description":
                            self.printer.printList(self.movieController.listOfMoviesWithDescription(optionInputWordList[3]))
                        elif optionInputWordList[2] == "genre":
                            self.printer.printList(self.movieController.listOfMoviesWithGenre(optionInputWordList[3]))
                    elif optionInputWordList[0] == "back":
                        break
                    else:
                        print("wrong input")
            elif menuChosen == "stats":
                while True:
                    self.printer.printSubmenu("statsMenu")
                    optionInput = input(">")
                    optionInputWordList = optionInput.split()
                    if self.validator.isValidStatsQuery(optionInputWordList):
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
                    elif optionInputWordList[0] == "back":
                        break
                    else:
                        print("wrong input")
            elif menuChosen == "exit":
                return
            else:
                print("Wrong input!")

