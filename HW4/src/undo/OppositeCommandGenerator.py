from src.Constants import Constants


class OppositeCommandGenerator:
    def returnOppositeCommand(self, parsedInputCommand, controller):
        # got "return" "client id" "movie id"
        oppositeCommand = ["rental", "returnedDateToNone"]
        constants = Constants()
        for rental in controller.getRentalList():
            if rental.getMovieId() == int(parsedInputCommand[2]) and rental.getClientId() == int(parsedInputCommand[1]) and rental.getReturnedDate() is None:
                oppositeCommand.append(str(rental.getId()))
                return oppositeCommand
        # return "rental" "returnedDateToNone" "rental id"

    def rentOppositeCommand(self, controller):
        # got "rent" "client id" "movie id" "day" "month" "year"
        oppositeCommand = ["rental", "remove", str(len(controller.getRentalList()))]
        return oppositeCommand
        # return "rental" "remove" "rental id"

    def updateMovieOppositeCommand(self, parsedInputCommand, controller):
        # got "update" "movie id" "name" "description" "genre"
        oppositeCommand = ["movie", "update", parsedInputCommand[1],
                           controller.getMovieWithId(int(parsedInputCommand[1])).getTitle(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getDescription(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getGenre()]
        return oppositeCommand
        # return "movie" "update" "movie id" "old title" "old description" "old genre"

    def removeMovieOppositeCommand(self, parsedInputCommand, controller):
        # got "remove" "movie id"
        oppositeCommand = ["movie", "add", parsedInputCommand[1],
                           controller.getMovieWithId(int(parsedInputCommand[1])).getTitle(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getDescription(),
                           controller.getMovieWithId(int(parsedInputCommand[1])).getGenre()]
        return oppositeCommand
        # return "movie" "add" "movie id" "title" "description" "genre"

    def addMovieOppositeCommand(self, controller):
        # got "add" "name" "description" "genre"
        oppositeCommand = ["movie", "remove", str(len(controller.getMovieList()))]
        return oppositeCommand
        # return "movie" "remove" "id of movie to remove"

    def addClientOppositeCommand(self, controller):
        # got "add" "name"
        oppositeCommand = ["client", "remove", str(len(controller.getClientList()))]
        return oppositeCommand
        # return "client" "remove" "id of element to remove"

    def removeClientOppositeCommand(self, parsedInputCommand, controller):
        # got "remove" "client id"
        oppositeCommand = ["client", "add", parsedInputCommand[1], controller.getClientWithId(int(parsedInputCommand[1])).getName()]
        return oppositeCommand
        # return "client" "add" "client id" "client name"

    def updateClientOppositeCommand(self, parsedInputCommand, controller):
        # got "update" "client id" "new name"
        oppositeCommand = ["client", "update", parsedInputCommand[1],
                           controller.getClientWithId(int(parsedInputCommand[1])).getName()]
        return oppositeCommand
        # return "client" "update" "client id" "old name"
