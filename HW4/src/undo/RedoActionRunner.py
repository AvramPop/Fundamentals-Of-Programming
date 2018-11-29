from src.dao.ClientDAO import ClientDAO
from src.dao.MovieDAO import MovieDAO


class RedoActionRunner:
    def rent(self, dueDate, commandToRedo, rentalController, clientController, movieController):
        rentalController.rentMovieByClientUntilDate(int(commandToRedo[1]),
                                                         int(commandToRedo[2]),
                                                         dueDate,
                                                         movieController.getRepo(),
                                                         clientController.getRepo())

    def doReturn(self, commandToRedo, rentalController):
        rentalController.returnMovieByClient(int(commandToRedo[1]),
                                                  int(commandToRedo[2]))

    def addClient(self, commandToRedo, clientController):
        clientController.addClient(ClientDAO(commandToRedo[1]))

    def removeClient(self, commandToRedo, clientController, rentalController):
        clientController.removeClientWithId(int(commandToRedo[1]), rentalController.getRepo())

    def updateClient(self, commandToRedo, clientController):
        clientController.updateClientWithId(int(commandToRedo[1]),
                                                 ClientDAO(commandToRedo[2]))

    def addMovie(self, commandToRedo, movieController):
        movieController.addMovie(MovieDAO(commandToRedo[1], commandToRedo[2], commandToRedo[3]))

    def removeMovie(self, commandToRedo, movieController, rentalController):
        movieController.removeMovieWithId(int(commandToRedo[1]), rentalController.getRepo())

    def updateMovie(self, commandToRedo, movieController):
        movieController.updateMovieWithId(int(commandToRedo[1]),
                                               MovieDAO(commandToRedo[2], commandToRedo[3],
                                                        commandToRedo[4]))
