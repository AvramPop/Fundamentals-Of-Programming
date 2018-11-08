from main.Constants import Constants
from main.Exception import ObjectNotInCollectionException, DatesNotOrderedException, InvalidDateFormatException
from main.controller.ClientController import ClientController
from main.controller.MovieController import MovieController
from main.controller.RentalController import RentalController
from main.model.Client import Client
from main.model.Date import Date
from main.model.Movie import Movie
from main.model.Rental import Rental
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.repo.RentalRepo import RentalRepo
from main.ui.Printer import Printer


class Console:
    printer = Printer()
    constants = Constants()
    clientController = ClientController()
    movieController = MovieController()
    rentalController = RentalController()

    def run(self):

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
                                if len(optionInputWordList) == 2:
                                    try:
                                        if optionInputWordList[1].isdigit():
                                            self.clientController.removeClientWithId(int(optionInputWordList[1]))
                                        else:
                                            print("wrong input")
                                    except ObjectNotInCollectionException as objectNotInCollectionException:
                                        print("Client with id", optionInputWordList[1], "not found")
                                    else:
                                        print("Successfully removed client #", optionInputWordList[1])
                                else:
                                    print("wrong input")
                            elif optionInputWordList[0] == "update":
                                if len(optionInputWordList) == 3:
                                    try:
                                        if optionInputWordList[1].isdigit():
                                            self.clientController.updateClientWithId(int(optionInputWordList[1]), Client(optionInputWordList[2]))
                                        else:
                                            print("wrong input")
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
                    elif menuChosen == "movie":
                        while True:
                            self.printer.printSubmenu("movieMenu")
                            optionInput = input(">")
                            optionInputWordList = optionInput.split()
                            if optionInputWordList[0] == "list":
                                if len(optionInputWordList) == 1:
                                    # self.movieRepo.printMovieList()
                                    self.printer.printList(self.movieController.getMovieList())
                                elif len(optionInputWordList) == 2:
                                    try:
                                        # self.printer.printMovie(
                                            # self.movieRepo.getMovieWithTitle(optionInputWordList[1]))
                                        if optionInputWordList[1].isdigit():
                                            self.printer.printObject(self.movieController.getMovieWithId(int(optionInputWordList[1])))
                                        else:
                                            print("wrong input")
                                    except ObjectNotInCollectionException as objectNotInCollectionException:
                                        print("Movie with id", optionInputWordList[1], "not found")
                                else:
                                    print("Wrong input")
                            elif optionInputWordList[0] == "remove":
                                if len(optionInputWordList) == 2:
                                    try:
                                        # self.movieRepo.removeMovieWithTitle(optionInputWordList[1])
                                        if optionInputWordList[1].isdigit():
                                            self.movieController.removeMovieWithId(int(optionInputWordList[1]))
                                        else:
                                            print("wrong input")
                                    except ObjectNotInCollectionException as objectNotInCollectionException:
                                        print("Movie with id", optionInputWordList[1], "not found")
                                    else:
                                        print("Successfully removed movie #", optionInputWordList[1])
                                else:
                                    print("wrong input")
                            elif optionInputWordList[0] == "update":
                                if len(optionInputWordList) == 5:
                                    try:
                                        # self.movieRepo.updateMovieWithTitle(optionInputWordList[1], Movie(optionInputWordList[2], optionInputWordList[3], optionInputWordList[4]))
                                        if optionInputWordList[1].isdigit():
                                            self.movieController.updateMovieWithId(int(optionInputWordList[1]), Movie(optionInputWordList[2], optionInputWordList[3], optionInputWordList[4]))
                                        else:
                                            print("wrong input")
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
                    elif menuChosen == "back":
                        break
                    else:
                        print("Wrong input!")
            elif menuChosen == "rental":  # TODO refactoring done up until here
                print("rental")
                # while True:
                #     self.printer.printSubmenu("rentalMenu")
                #     optionInput = input(">")
                #     optionInputWordList = optionInput.split()
                #     if optionInputWordList:
                #         if optionInputWordList[0] == "rent":
                #             if len(optionInputWordList) == 6:
                #                 try:
                #                     clientId = self.clientRepo.getClientIdByName(optionInputWordList[1])
                #                 except ObjectNotInCollectionException as objectNotInCollectionException:
                #                     print("Client with name", optionInputWordList[1], "not found")
                #                 else:
                #                     if not self.rentalRepo.clientHasMoviesNotReturned(clientId):
                #                         try:
                #                             movieId = self.movieRepo.getMovieIdByTitle(optionInputWordList[2])
                #                         except ObjectNotInCollectionException as objectNotInCollectionException:
                #                             print("Movie with title", optionInputWordList[2], "not found")
                #                         else:
                #                             if not self.rentalRepo.isMovieRented(movieId):
                #                                 try:
                #                                     dueDate = Date(int(optionInputWordList[3]), int(optionInputWordList[4]), int(optionInputWordList[5]))
                #                                 except InvalidDateFormatException as invalidDateFormatException:
                #                                     print("Invalid date format")
                #                                 else:
                #                                     try:
                #                                         rentalToAdd = Rental(movieId, clientId, self.constants.currentDay(), dueDate)
                #                                     except DatesNotOrderedException as datesNotOrderedException:
                #                                         print("The due date cannot be before the rental date")
                #                                     else:
                #                                         rentalToAdd.getMovie().rent()
                #                                         self.rentalRepo.addRental(rentalToAdd)
                #                                         print("Movie", optionInputWordList[2], "successfully rented by", optionInputWordList[1], "until", str(dueDate))
                #                                         self.rentalRepo.printRentalList()
                #                             else:
                #                                 print("Movie", optionInputWordList[2], "is rented")
                #                     else:
                #                         print("Client", optionInputWordList[1], "has passed due date for movies")
                #             else:
                #                 print("wrong input")
                #         elif optionInputWordList[0] == "return":
                #             try:
                #                 clientId = self.clientRepo.getClientIdByName(optionInputWordList[1])
                #             except ObjectNotInCollectionException as objectNotInCollectionException:
                #                 print("Client with name", optionInputWordList[1], "not found")
                #             else:
                #                 try:
                #                     movieId = self.movieRepo.getMovieIdByTitle(optionInputWordList[2])
                #                 except ObjectNotInCollectionException as objectNotInCollectionException:
                #                     print("movie with title", optionInputWordList[2], "not found")
                #                 else:
                #                     if self.rentalRepo.clientHasMovieRented(clientId, movieId):
                #                         self.rentalRepo.returnMovie(clientId, movieId)
                #                         print("Movie", optionInputWordList[2], "successfully returned by client", optionInputWordList[1])
                #                         self.rentalRepo.printRentalList()
                #                     else:
                #                         print("Client", optionInputWordList[1], "doesn't have the movie", optionInputWordList[2], "rented")
                #         elif optionInputWordList[0] == "back":
                #             break
                #         else:
                #             print("wrong input")
                #     else:
                #         print("wrong input")
            elif menuChosen == "search":
                print("search")
            elif menuChosen == "stats":
                print("stats")
            elif menuChosen == "exit":
                return
            else:
                print("Wrong input!")

