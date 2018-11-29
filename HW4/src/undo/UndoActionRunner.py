from src.dao.ClientDAO import ClientDAO
from src.dao.MovieDAO import MovieDAO


class UndoActionRunner:
    def addClient(self, command, clientController):
        # return "client" "add" "client id" "client name"
        client = ClientDAO(command[3])
        client.setClientId(int(command[2]))
        clientController.addClientWithId(client)

    def removeClient(self, command, clientController, rentalController):
        # return "client" "remove" "id of element to remove"
        clientController.removeClientWithId(int(command[2]), rentalController.getRepo())

    def updateClient(self, command, clientController):
        # return "client" "update" "client id" "old name"
        updatedClient = ClientDAO(command[3])
        updatedClient.setClientId(int(command[2]))
        clientController.updateClientWithId(int(command[2]), updatedClient)

    def addMovie(self, command, movieController):
        # return "movie" "add" "movie id" "title" "description" "genre"
        movie = MovieDAO(command[3], command[4], command[5])
        movie.setMovieId(int(command[2]))
        movieController.addMovieWithId(movie)

    def removeMovie(self, command, movieController, rentalController):
        # return "movie" "remove" "id of movie to remove"
        movieController.removeMovieWithId(int(command[2]), rentalController.getRepo())

    def updateMovie(self, command, movieController):
        # return "movie" "update" "movie id" "old title" "old description" "old genre"
        updatedMovie = MovieDAO(command[3], command[4], command[5])
        updatedMovie.setMovieId(int(command[2]))
        movieController.updateMovieWithId(int(command[2]), updatedMovie)

    def returnedDateToNone(self, command, rentalController):
        # return "rental" "returnedDateToNone" "rental id"
        updatedRental = rentalController.getRentalWithId(int(command[2]))
        updatedRental.setReturnedDateToNone()
        rentalController.updateRentalWithId(int(command[2]), updatedRental)

    def removeRental(self, command, rentalController):
        # return "rental" "remove" "rental id"
        rentalController.removeRentalWithId(int(command[2]))
