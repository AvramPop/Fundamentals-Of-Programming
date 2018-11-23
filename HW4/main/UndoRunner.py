from main.Constants import Constants
from main.model.Client import Client
from main.model.Movie import Movie


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
                self.__addClient(command, clientController)
            elif operation == "remove":
                self.__removeClient(command, clientController, rentalController)
            elif operation == "update":
                self.__updateClient(command, clientController)
        elif typeOfOperation == "movie":
            if operation == "add":
                self.__addMovie(command, movieController)
            elif operation == "remove":
                self.__removeMovie(command, movieController, rentalController)
            elif operation == "update":
                self.__updateMovie(command, movieController)
        elif typeOfOperation == "rental":
            if operation == "returnedDateToNone":
                self.__returnedDateToNone(command, rentalController)
            elif operation == "remove":
                self.__removeRental(command, rentalController)

    def __addClient(self, command, clientController):
        # return "client" "add" "client id" "client name"
        client = Client(command[3])
        client.setClientId(int(command[2]))
        clientController.addClientWithId(client)

    def __removeClient(self, command, clientController, rentalController):
        # return "client" "remove" "id of element to remove"
        clientController.removeClientWithId(int(command[2]), rentalController.getRepo())

    def __updateClient(self, command, clientController):
        # return "client" "update" "client id" "old name"
        updatedClient = Client(command[3])
        updatedClient.setClientId(int(command[2]))
        clientController.updateClientWithId(int(command[2]), updatedClient)

    def __addMovie(self, command, movieController):
        # return "movie" "add" "movie id" "title" "description" "genre"
        movie = Movie(command[3], command[4], command[5])
        movie.setMovieId(int(command[2]))
        movieController.addMovieWithId(movie)

    def __removeMovie(self, command, movieController, rentalController):
        # return "movie" "remove" "id of movie to remove"
        movieController.removeMovieWithId(int(command[2]), rentalController.getRepo())

    def __updateMovie(self, command, movieController):
        # return "movie" "update" "movie id" "old title" "old description" "old genre"
        updatedMovie = Movie(command[3], command[4], command[5])
        updatedMovie.setMovieId(int(command[2]))
        movieController.updateMovieWithId(int(command[2]), updatedMovie)

    def __returnedDateToNone(self, command, rentalController):
        # return "rental" "returnedDateToNone" "rental id"
        updatedRental = rentalController.getRentalWithId(int(command[2]))
        updatedRental.setReturnedDateToNone()
        rentalController.updateRentalWithId(int(command[2]), updatedRental)

    def __removeRental(self, command, rentalController):
        # return "rental" "remove" "rental id"
        rentalController.removeRentalWithId(int(command[2]))
