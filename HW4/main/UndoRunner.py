class UndoRunner:

    def addOppositeCommandToStack(self, command, controller, stack, typeWorkingWith):
        # for every command add to stack the command + id of element + type
        if typeWorkingWith == "client":
            if command[0] == "add":
                stack.push(self.__addClientOppositeCommand(command, controller))
            elif command[0] == "remove":
                stack.push(self.__removeClientOppositeCommand(command, controller))
            elif command[0] == "update":
                stack.push(self.__updateClientOppositeCommand(command, controller))
            else:
                return
        elif typeWorkingWith == "movie":
            if command[0] == "add":
                stack.push(self.__addMovieOppositeCommand(command, controller))
            elif command[0] == "remove":
                stack.push(self.__removeMovieOppositeCommand(command, controller))
            elif command[0] == "update":
                stack.push(self.__updateMovieOppositeCommand(command, controller))
            else:
                return
        elif typeWorkingWith == "rental":
            if command[0] == "rent":
                stack.push(self.__rentOppositeCommand(command, controller))
            elif command[0] == "return":
                stack.push(self.__returnOppositeCommand(command, controller))
            else:
                return
        else:
            raise TypeError

    def undo(self, clientController, movieController, rentalController, stack):
        self.__runUndoCommand(stack.pop(), clientController, movieController, rentalController)

    def __returnOppositeCommand(self, parsedInputCommand, controller):
        # got "return" "client id" "movie id"
        oppositeCommand = ["rental", "returnedDateToNone"]
        for rental in controller.getRentalList():
            if rental.getMovieId() == int(parsedInputCommand[2]) and rental.getClientId() == int(parsedInputCommand[1]) and rental.getReturnedDate() is None:
                oppositeCommand.append(rental.getId())
                return oppositeCommand
        # return "rental" "returnedDateToNone" "rental id"

    def __rentOppositeCommand(self, controller):
        # got "rent" "client id" "movie id" "day" "month" "year"
        oppositeCommand = ["rental", "remove", len(controller.getRentalList())]  # TODO maybe +1 or -1
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
        oppositeCommand = ["movie", "remove", len(controller.getMovieList)]  # TODO maybe + or - 1
        return oppositeCommand
        # return "movie" "remove" "id of movie to remove"

    def __addClientOppositeCommand(self, controller):
        # got "add" "name"
        oppositeCommand = ["client", "remove", len(controller.getClientList())]  # TODO maybe +1 or -1
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
                self.__removeClient(command, clientController)
            elif operation == "update":
                self.__updateClient(command, clientController)
        elif typeOfOperation == "movie":
            if operation == "add":
                self.__addMovie(command, movieController)
            elif operation == "remove":
                self.__removeMovie(command, movieController)
            elif operation == "update":
                self.__updateMovie(command, movieController)
        elif typeOfOperation == "rental":
            if operation == "returnedDateToNone":
                self.__returnedDateToNone(command, rentalController)
            elif operation == "remove":
                self.__removeRental(command, rentalController)

    def __addClient(self, command, clientController):
        # return "client" "add" "client id" "client name"
        pass

    def __removeClient(self, command, clientController):
        # return "client" "remove" "id of element to remove"
        pass

    def __updateClient(self, command, clientController):
        # return "client" "update" "client id" "old name"
        pass

    def __addMovie(self, command, movieController):
        # return "movie" "add" "movie id" "title" "description" "genre"
        pass

    def __removeMovie(self, command, movieController):
        # return "movie" "remove" "id of movie to remove"
        pass

    def __updateMovie(self, command, movieController):
        # return "movie" "update" "movie id" "old title" "old description" "old genre"
        pass

    def __returnedDateToNone(self, command, rentalController):
        # return "rental" "returnedDateToNone" "rental id"
        pass

    def __removeRental(self, command, rentalController):
        # return "rental" "remove" "rental id"
        pass
