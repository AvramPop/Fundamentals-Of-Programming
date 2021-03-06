from src.Constants import Constants
from src.Date import Date
from src.Exception import ObjectNotInCollectionException, DatesNotOrderedException, InvalidDateFormatException, \
    ClientHasMoviesNotReturnedException, MovieNotAvailableException, MovieNotCurrentlyRentedByClientException, \
    MovieCurrentlyRentedException, EmptyStackException
from src.Validator import Validator
from src.dao.ClientDAO import ClientDAO
from src.dao.MovieDAO import MovieDAO
from src.ui.Printer import Printer


class Console:

    def __init__(self, clientController, movieController, rentalController, undoStack, commandsStack, redoStack, undoRunner) -> None:
        self.printer = Printer()
        self.validator = Validator()
        self.constants = Constants()
        self.clientController = clientController
        self.movieController = movieController
        self.rentalController = rentalController
        self.undoStack = undoStack
        self.commandsStack = commandsStack
        self.redoStack = redoStack
        self.undoRunner = undoRunner

    def run(self):
        while True:
            self.printer.printMenu("mainMenu")
            menuChosen = input(">")
            if menuChosen == "manager":
                self.__showManagerMenu()
            elif menuChosen == "rental":
                self.__showRentalMenu()
            elif menuChosen == "search":
                self.__showSearchMenu()
            elif menuChosen == "stats":
                self.__showStatsMenu()
            elif menuChosen == "exit":
                return
            else:
                print("Wrong input!")

    def __undo(self):
        try:
            lastElement = self.commandsStack.lastElement()
            self.undoRunner.undo(self.clientController, self.movieController, self.rentalController, self.undoStack)
        except EmptyStackException:
            print("nothing to undo")
        else:
            self.redoStack.push(lastElement)
            self.commandsStack.deleteLastElement()

    def __redo(self):
        try:
            commandToRedo = self.redoStack.pop()
        except EmptyStackException:
            print("nothing to redo")
        else:
            self.undoRunner.redo(commandToRedo, self.clientController, self.movieController, self.rentalController)

    def __showManagerMenu(self):
        while True:
            self.printer.printMenu("managerMenu")
            menuChosen = input(">")
            if menuChosen == "client":
                self.__showClientManager()
            elif menuChosen == "movie":
                self.__showMovieManager()
            elif menuChosen == "back":
                break
            else:
                print("Wrong input!")

    def __showStatsMenu(self):
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

    def __showSearchMenu(self):
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

    def __showRentalMenu(self):
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
                elif optionInputWordList[0] == "undo":
                    self.__undo()
                elif optionInputWordList[0] == "redo":
                    self.__redo()
                else:
                    print("wrong input")
            else:
                print("wrong input")

    def __showMovieManager(self):
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
            elif optionInputWordList[0] == "undo":
                self.__undo()
            elif optionInputWordList[0] == "redo":
                self.__redo()
            else:
                print("wrong input")

    def __showClientManager(self):
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
            elif optionInputWordList[0] == "undo":
                self.__undo()
            elif optionInputWordList[0] == "redo":
                self.__redo()
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
                            self.undoRunner.addCommandToUndo(optionInputWordList, self.rentalController, self.undoStack, "rental", self.commandsStack)
                            self.__doReturn(optionInputWordList)
                        except MovieNotCurrentlyRentedByClientException:
                            print("movie with id #", optionInputWordList[2], "not rented by client with #",
                                  optionInputWordList[1])
                            self.__popUndoStacks()
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

    def __popUndoStacks(self):
        self.undoStack.pop()
        self.commandsStack.pop()

    def __doReturn(self, optionInputWordList):
        self.rentalController.returnMovieByClient(int(optionInputWordList[1]),
                                                  int(optionInputWordList[2]))

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
                                except InvalidDateFormatException:
                                    print("Invalid date format")
                                else:
                                    try:
                                        self.undoRunner.addCommandToUndo(optionInputWordList, self.rentalController,
                                                                         self.undoStack, "rental", self.commandsStack)
                                        self.__doRent(dueDate, optionInputWordList)
                                    except DatesNotOrderedException:
                                        print("The due date cannot be before the rental date")
                                        self.__popUndoStacks()
                                    except ClientHasMoviesNotReturnedException:
                                        print("Client #", optionInputWordList[1], "has passed due date for movies")
                                        self.__popUndoStacks()
                                    except MovieNotAvailableException:
                                        print("Movie #", optionInputWordList[2], "is not available")
                                        self.__popUndoStacks()
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

    def __doRent(self, dueDate, optionInputWordList):
        self.rentalController.rentMovieByClientUntilDate(int(optionInputWordList[1]),
                                                         int(optionInputWordList[2]),
                                                         dueDate,
                                                         self.movieController.getRepo(),
                                                         self.clientController.getRepo())

    def __addMovie(self, optionInputWordList):
        if len(optionInputWordList) == 4:
            self.undoRunner.addCommandToUndo(optionInputWordList, self.movieController, self.undoStack, "movie", self.commandsStack)
            self.__doAddMovie(optionInputWordList)
            print("Successfully added movie", optionInputWordList[1])
        else:
            print("wrong input")

    def __doAddMovie(self, optionInputWordList):
        self.movieController.addMovie(MovieDAO(optionInputWordList[1], optionInputWordList[2], optionInputWordList[3]))

    def __updateMovie(self, optionInputWordList):
        if self.validator.isValidUpdateQueryWithNumberOfElements(optionInputWordList, 5):
            try:
                self.undoRunner.addCommandToUndo(optionInputWordList, self.movieController, self.undoStack, "movie", self.commandsStack)
                self.__doUpdateMovie(optionInputWordList)
            except ObjectNotInCollectionException:
                print("Movie with id", optionInputWordList[1], "not found")
                self.__popUndoStacks()
            else:
                print("Successfully updated movie #", optionInputWordList[1])
        else:
            print("wrong input")

    def __doUpdateMovie(self, optionInputWordList):
        self.movieController.updateMovieWithId(int(optionInputWordList[1]),
                                               MovieDAO(optionInputWordList[2], optionInputWordList[3],
                                                        optionInputWordList[4]))

    def __removeMovie(self, optionInputWordList):
        if self.validator.isValidRemoveQuery(optionInputWordList):
            try:
                optionInputWordList.append("movie")  # caution use
                self.undoRunner.addCommandToUndo(optionInputWordList, self.movieController, self.undoStack, "movie", self.commandsStack)
                self.__doRemoveMovie(optionInputWordList)
            except ObjectNotInCollectionException:
                print("Movie with id", optionInputWordList[1], "not found")
                self.__popUndoStacks()
            except MovieCurrentlyRentedException:
                print("Movie with id #", optionInputWordList[1], "is currently rented. Couldn't delete")
                self.__popUndoStacks()
            else:
                print("Successfully removed movie #", optionInputWordList[1])
        else:
            print("wrong input")

    def __doRemoveMovie(self, optionInputWordList):
        self.movieController.removeMovieWithId(int(optionInputWordList[1]), self.rentalController.getRepo())

    def __listMovie(self, optionInputWordList):
        if len(optionInputWordList) == 1:
            self.printer.printList(self.movieController.getMovieList())
        elif len(optionInputWordList) == 2:
            try:
                if optionInputWordList[1].isdigit():
                    self.printer.printObject(self.movieController.getMovieWithId(int(optionInputWordList[1])))
                else:
                    print("wrong input")
            except ObjectNotInCollectionException:
                print("Movie with id", optionInputWordList[1], "not found")
        else:
            print("Wrong input")

    def __addClient(self, optionInputWordList):
        if len(optionInputWordList) == 2:
            self.undoRunner.addCommandToUndo(optionInputWordList, self.clientController, self.undoStack, "client", self.commandsStack)
            self.__doAddClient(optionInputWordList)
            print("Successfully added client", optionInputWordList[1])
        else:
            print("wrong input")

    def __doAddClient(self, optionInputWordList):
        self.clientController.addClient(ClientDAO(optionInputWordList[1]))

    def __updateClient(self, optionInputWordList):
        if self.validator.isValidUpdateQueryWithNumberOfElements(optionInputWordList, 3):
            try:
                self.undoRunner.addCommandToUndo(optionInputWordList, self.clientController, self.undoStack, "client", self.commandsStack)
                self.__doUpdateClient(optionInputWordList)
            except ObjectNotInCollectionException:
                print("Client with id", optionInputWordList[1], "not found")
                self.__popUndoStacks()
            else:
                print("Successfully updated client #", optionInputWordList[1])
        else:
            print("wrong input")

    def __doUpdateClient(self, optionInputWordList):
        self.clientController.updateClientWithId(int(optionInputWordList[1]),
                                                 ClientDAO(optionInputWordList[2]))

    def __removeClient(self, optionInputWordList):
        if self.validator.isValidRemoveQuery(optionInputWordList):
            try:
                optionInputWordList.append("client")  # caution use
                self.undoRunner.addCommandToUndo(optionInputWordList, self.clientController, self.undoStack, "client", self.commandsStack)
                self.__doRemoveClient(optionInputWordList)
            except ClientHasMoviesNotReturnedException:
                print("Client with id #", optionInputWordList[1], "has movies not returned. Couldn't delete")
                self.__popUndoStacks()
            except ObjectNotInCollectionException:
                print("Client with id", optionInputWordList[1], "not found")
                self.__popUndoStacks()
            else:
                print("Successfully removed client #", optionInputWordList[1])
        else:
            print("wrong input")

    def __doRemoveClient(self, optionInputWordList):
        self.clientController.removeClientWithId(int(optionInputWordList[1]), self.rentalController.getRepo())

    def __listClient(self, optionInputWordList):
        if len(optionInputWordList) == 1:
            self.printer.printList(self.clientController.getClientList())
        elif len(optionInputWordList) == 2:
            try:
                if optionInputWordList[1].isdigit():
                    self.printer.printObject(self.clientController.getClientWithId(int(optionInputWordList[1])))
                else:
                    print("wrong input")
            except ObjectNotInCollectionException:
                print("Client with id #", optionInputWordList[1], "not found")
        else:
            print("Wrong input")
