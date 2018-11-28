from main.Constants import Constants
from main.Date import Date
from main.dao.ClientDAO import ClientDAO
from main.dao.MovieDAO import MovieDAO


class UndoRunner:

    def addCommandToUndo(self, command, controller, undoStack, typeWorkingWith, commandsStack):
        # for every command add to stack the command + id of element + type
        if typeWorkingWith == "client":
            if command[0] == "add":
                undoStack.push(self.__addClientOppositeCommand(controller))
                commandsStack.push(command)
            elif command[0] == "remove":
                undoStack.push(self.__removeClientOppositeCommand(command, controller))
                commandsStack.push(command)
            elif command[0] == "update":
                undoStack.push(self.__updateClientOppositeCommand(command, controller))
                commandsStack.push(command)
            else:
                return
        elif typeWorkingWith == "movie":
            if command[0] == "add":
                commandsStack.push(command)
                undoStack.push(self.__addMovieOppositeCommand(controller))
            elif command[0] == "remove":
                commandsStack.push(command)
                undoStack.push(self.__removeMovieOppositeCommand(command, controller))
            elif command[0] == "update":
                commandsStack.push(command)
                undoStack.push(self.__updateMovieOppositeCommand(command, controller))
            else:
                return
        elif typeWorkingWith == "rental":
            if command[0] == "rent":
                commandsStack.push(command)
                undoStack.push(self.__rentOppositeCommand(controller))
            elif command[0] == "return":
                commandsStack.push(command)
                undoStack.push(self.__returnOppositeCommand(command, controller))
            else:
                return
        else:
            raise TypeError

    def undo(self, clientController, movieController, rentalController, stack):
        self.__runUndoCommand(stack.pop(), clientController, movieController, rentalController)

    def redo(self, commandToRedo, clientController, movieController, rentalController):
        if commandToRedo[0] == "rent":
            dueDate = Date(int(commandToRedo[3]),
                           int(commandToRedo[4]),
                           int(commandToRedo[5]))
            self.__doRentForRedo(dueDate, commandToRedo, rentalController, clientController, movieController)
        elif commandToRedo[0] == "return":
            self.__doReturnForRedo(commandToRedo, rentalController)
        elif commandToRedo[0] == "add" and len(commandToRedo) == 2:
            self.__doAddClientForRedo(commandToRedo, clientController)
        elif commandToRedo[0] == "remove" and commandToRedo[2] == "client":
            self.__doRemoveClientForRedo(commandToRedo, clientController, rentalController)
        elif commandToRedo[0] == "update" and len(commandToRedo) == 3:
            self.__doUpdateClientForRedo(commandToRedo, clientController)
        elif commandToRedo[0] == "add" and len(commandToRedo) == 4:
            self.__doAddMovieForRedo(commandToRedo, movieController)
        elif commandToRedo[0] == "remove" and commandToRedo[2] == "movie":
            self.__doRemoveMovieForRedo(commandToRedo, movieController, rentalController)
        elif commandToRedo[0] == "update" and len(commandToRedo) == 5:
            self.__doUpdateMovieForRedo(commandToRedo, movieController)

    def __returnOppositeCommand(self, parsedInputCommand, controller):
        # got "return" "client id" "movie id"
        oppositeCommand = ["rental", "returnedDateToNone"]
        constants = Constants()
        for rental in controller.getRentalList():
            if rental.getMovieId() == int(parsedInputCommand[2]) and rental.getClientId() == int(parsedInputCommand[1]) and rental.getReturnedDate() is None:
                oppositeCommand.append(str(rental.getId()))
                return oppositeCommand
        # return "rental" "returnedDateToNone" "rental id"

    def __rentOppositeCommand(self, controller):
        # got "rent" "client id" "movie id" "day" "month" "year"
        oppositeCommand = ["rental", "remove", str(len(controller.getRentalList()))]
        return oppositeCommand
        # return "rental" "remove" "rental id"

    def __updateMovieOppositeCommand(self, parsedInputCommand, controller):
        # got "update" "movie id" "name" "description" "genre"
        oppositeCommand = ["movie", "update", parsedInputCommand[1],
                           controller.getMovieWithId(int(parsedInputCommand[1])).getTitle(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getDescription(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getGenre()]
        return oppositeCommand
        # return "movie" "update" "movie id" "old title" "old description" "old genre"

    def __removeMovieOppositeCommand(self, parsedInputCommand, controller):
        # got "remove" "movie id"
        oppositeCommand = ["movie", "add", parsedInputCommand[1],
                           controller.getMovieWithId(int(parsedInputCommand[1])).getTitle(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getDescription(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getGenre()]
        return oppositeCommand
        # return "movie" "add" "movie id" "title" "description" "genre"

    def __addMovieOppositeCommand(self, controller):
        # got "add" "name" "description" "genre"
        oppositeCommand = ["movie", "remove", str(len(controller.getMovieList()))]
        return oppositeCommand
        # return "movie" "remove" "id of movie to remove"

    def __addClientOppositeCommand(self, controller):
        # got "add" "name"
        oppositeCommand = ["client", "remove", str(len(controller.getClientList()))]
        return oppositeCommand
        # return "client" "remove" "id of element to remove"

    def __removeClientOppositeCommand(self, parsedInputCommand, controller):
        # got "remove" "client id"
        oppositeCommand = ["client", "add", parsedInputCommand[1], controller.getClientWithId(int(parsedInputCommand[1])).getName()]
        return oppositeCommand
        # return "client" "add" "client id" "client name"

    def __updateClientOppositeCommand(self, parsedInputCommand, controller):
        # got "update" "client id" "new name"
        oppositeCommand = ["client", "update", parsedInputCommand[1],
                           controller.getClientWithId(int(parsedInputCommand[1])).getName()]
        return oppositeCommand
        # return "client" "update" "client id" "old name"

    def __runUndoCommand(self, command, clientController, movieController, rentalController):
        typeOfOperation = command[0]
        operation = command[1]
        if typeOfOperation == "client":
            if operation == "add":
                self.__addClientForUndo(command, clientController)
            elif operation == "remove":
                self.__removeClientForUndo(command, clientController, rentalController)
            elif operation == "update":
                self.__updateClientForUndo(command, clientController)
        elif typeOfOperation == "movie":
            if operation == "add":
                self.__addMovieForUndo(command, movieController)
            elif operation == "remove":
                self.__removeMovieForUndo(command, movieController, rentalController)
            elif operation == "update":
                self.__updateMovieForUndo(command, movieController)
        elif typeOfOperation == "rental":
            if operation == "returnedDateToNone":
                self.__returnedDateToNoneForUndo(command, rentalController)
            elif operation == "remove":
                self.__removeRentalForUndo(command, rentalController)

    def __addClientForUndo(self, command, clientController):
        # return "client" "add" "client id" "client name"
        client = ClientDAO(command[3])
        client.setClientId(int(command[2]))
        clientController.addClientWithId(client)

    def __removeClientForUndo(self, command, clientController, rentalController):
        # return "client" "remove" "id of element to remove"
        clientController.removeClientWithId(int(command[2]), rentalController.getRepo())

    def __updateClientForUndo(self, command, clientController):
        # return "client" "update" "client id" "old name"
        updatedClient = ClientDAO(command[3])
        updatedClient.setClientId(int(command[2]))
        clientController.updateClientWithId(int(command[2]), updatedClient)

    def __addMovieForUndo(self, command, movieController):
        # return "movie" "add" "movie id" "title" "description" "genre"
        movie = MovieDAO(command[3], command[4], command[5])
        movie.setMovieId(int(command[2]))
        movieController.addMovieWithId(movie)

    def __removeMovieForUndo(self, command, movieController, rentalController):
        # return "movie" "remove" "id of movie to remove"
        movieController.removeMovieWithId(int(command[2]), rentalController.getRepo())

    def __updateMovieForUndo(self, command, movieController):
        # return "movie" "update" "movie id" "old title" "old description" "old genre"
        updatedMovie = MovieDAO(command[3], command[4], command[5])
        updatedMovie.setMovieId(int(command[2]))
        movieController.updateMovieWithId(int(command[2]), updatedMovie)

    def __returnedDateToNoneForUndo(self, command, rentalController):
        # return "rental" "returnedDateToNone" "rental id"
        updatedRental = rentalController.getRentalWithId(int(command[2]))
        updatedRental.setReturnedDateToNone()
        rentalController.updateRentalWithId(int(command[2]), updatedRental)

    def __removeRentalForUndo(self, command, rentalController):
        # return "rental" "remove" "rental id"
        rentalController.removeRentalWithId(int(command[2]))

    def __doRentForRedo(self, dueDate, commandToRedo, rentalController, clientController, movieController):
        rentalController.rentMovieByClientUntilDate(int(commandToRedo[1]),
                                                         int(commandToRedo[2]),
                                                         dueDate,
                                                         movieController.getRepo(),
                                                         clientController.getRepo())

    def __doReturnForRedo(self, commandToRedo, rentalController):
        rentalController.returnMovieByClient(int(commandToRedo[1]),
                                                  int(commandToRedo[2]))

    def __doAddClientForRedo(self, commandToRedo, clientController):
        clientController.addClient(ClientDAO(commandToRedo[1]))

    def __doRemoveClientForRedo(self, commandToRedo, clientController, rentalController):
        clientController.removeClientWithId(int(commandToRedo[1]), rentalController.getRepo())

    def __doUpdateClientForRedo(self, commandToRedo, clientController):
        clientController.updateClientWithId(int(commandToRedo[1]),
                                                 ClientDAO(commandToRedo[2]))

    def __doAddMovieForRedo(self, commandToRedo, movieController):
        movieController.addMovie(MovieDAO(commandToRedo[1], commandToRedo[2], commandToRedo[3]))

    def __doRemoveMovieForRedo(self, commandToRedo, movieController, rentalController):
        movieController.removeMovieWithId(int(commandToRedo[1]), rentalController.getRepo())

    def __doUpdateMovieForRedo(self, commandToRedo, movieController):
        movieController.updateMovieWithId(int(commandToRedo[1]),
                                               MovieDAO(commandToRedo[2], commandToRedo[3],
                                                        commandToRedo[4]))
