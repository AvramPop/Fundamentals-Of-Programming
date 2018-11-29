from src.Constants import Constants
from src.Exception import DatesNotOrderedException, ClientHasMoviesNotReturnedException, MovieNotAvailableException, \
    MovieNotCurrentlyRentedByClientException
from src.dao.RentalDAO import RentalDAO
import operator


class RentalController:
    __constants = Constants()

    def __init__(self, rentalRepo) -> None:
        self.__rentalRepo = rentalRepo

    def getRepo(self):
        return self.__rentalRepo

    def addRentalWithId(self, rental):
        self.__rentalRepo.addRentalWithId(rental)

    def addRental(self, rental):  # TODO check if exceptions should be handled
        self.__rentalRepo.addRental(rental)

    def getRentalWithId(self, rentalId):
        return self.__rentalRepo.getRentalWithId(rentalId)

    def getRentalList(self):
        return self.__rentalRepo.getList()

    def removeRentalWithId(self, rentalId):
        self.__rentalRepo.removeRentalWithId(rentalId)

    def hasRentalWithId(self, rentalId):
        return self.__rentalRepo.hasRentalWithId(rentalId)

    def updateRentalWithId(self, rentalId, updatedRental):
        self.__rentalRepo.updateRentalWithId(rentalId, updatedRental)

    def rentMovieByClientUntilDate(self, clientId, movieId, dueDate, movieRepo, clientRepo):
        """
        Create a new rental between client and movie from today until due date
        """
        if dueDate.isBeforeDate(self.__constants.currentDay()):
            raise DatesNotOrderedException
        else:
            if self.__clientHasPassedDueDateMovies(clientId):
                raise ClientHasMoviesNotReturnedException
            else:
                if not self.__isMovieAvailable(movieId):
                    raise MovieNotAvailableException
                else:
                    self.addRental(
                        RentalDAO(clientId, movieId, self.__constants.currentDay(), dueDate, movieRepo, clientRepo))

    def returnMovieByClient(self, clientId, movieId):
        """
        Return movie if rented by client
        """
        movieFound = False
        for rental in self.getRentalList():
            if rental.getMovieId() == movieId and rental.getClientId() == clientId and rental.getReturnedDate() is None:
                constants = Constants()
                rental.setReturnedDate(constants.currentDay())
                self.updateRentalWithId(rental.getId(), rental)
                movieFound = True
        if not movieFound:
            raise MovieNotCurrentlyRentedByClientException

    def __clientHasPassedDueDateMovies(self, clientId):
        clientRentalList = []
        for rental in self.getRentalList():
            if rental.getClientId() == clientId:
                clientRentalList.append(rental)

        for rental in clientRentalList:
            if rental.getReturnedDate() is None and rental.getDueDate().isBeforeDate(self.__constants.currentDay()):
                return True
        return False

    def __isMovieAvailable(self, movieId):  # TODO check if have to check if movie exist (probably handled in ui)
        movieRentalList = []
        for rental in self.getRentalList():
            if rental.getMovieId() == movieId:
                movieRentalList.append(rental)

        if len(movieRentalList) == 0:  # movie never rented
            return True

        for rental in movieRentalList:
            if rental.getReturnedDate() is None:
                return False
        return True

    def populateRepo(self, movieRepo, rentalRepo):
        self.__rentalRepo.populateWithFew(movieRepo, rentalRepo)

    def moviesMostRentedByTimesRented(self, movieRepo):
        """
        Get list of movies most rented by times rented
        """
        rentals = self.getRentalList()
        movies = movieRepo.getList()
        moviesDictionary = {}
        for movie in movies:
            moviesDictionary[movie.getId()] = 0
        for rental in rentals:
            if rental.getMovieId() in moviesDictionary:
                moviesDictionary[rental.getMovieId()] += 1
        sortedMovies = sorted(moviesDictionary.items(), key=operator.itemgetter(1))
        sortedMovies.reverse()
        sortedMovieList = []
        for movie in sortedMovies:
            sortedMovieList.append(movieRepo.getMovieWithId(movie[0]))
        return sortedMovieList

    def moviesMostRentedByDays(self, movieRepo):
        """
        Get list of movies most rented by days rented
        """
        constants = Constants()
        rentals = self.getRentalList()
        movies = movieRepo.getList()
        moviesDictionary = {}
        for movie in movies:
            moviesDictionary[movie.getId()] = 0
        for rental in rentals:
            if rental.getMovieId() in moviesDictionary:
                if rental.getReturnedDate() is None:
                    daysToAdd = constants.currentDay().daysUntilDate(rental.getRentedDate())
                else:
                    daysToAdd = rental.getRentedDate().daysUntilDate(rental.getReturnedDate())
                moviesDictionary[rental.getMovieId()] += daysToAdd
        sortedMovies = sorted(moviesDictionary.items(), key=operator.itemgetter(1))
        sortedMovies.reverse()
        sortedMovieList = []
        for movie in sortedMovies:
            sortedMovieList.append(movieRepo.getMovieWithId(movie[0]))
        return sortedMovieList

    def mostActiveClients(self, clientRepo):
        """
        Get list of most active clients by days rented
        """
        constants = Constants()
        rentals = self.getRentalList()
        clients = clientRepo.getList()
        clientsDictionary = {}
        for client in clients:
            clientsDictionary[client.getId()] = 0
        for rental in rentals:
            if rental.getClientId() in clientsDictionary:
                if rental.getReturnedDate() is None:
                    daysToAdd = constants.currentDay().daysUntilDate(rental.getRentedDate())
                else:
                    daysToAdd = rental.getRentedDate().daysUntilDate(rental.getReturnedDate())
                clientsDictionary[rental.getClientId()] += daysToAdd
        sortedClients = sorted(clientsDictionary.items(), key=operator.itemgetter(1))
        sortedClients.reverse()
        sortedClientList = []
        for client in sortedClients:
            sortedClientList.append(clientRepo.getClientWithId(client[0]))
        return sortedClientList

    def moviesCurrentlyRented(self, movieRepo):
        """
        Get list of movie currently rented
        """
        moviesRentedNow = []
        for rental in self.getRentalList():
            if rental.getReturnedDate() is None:
                moviesRentedNow.append(movieRepo.getMovieWithId(rental.getMovieId()))
        return moviesRentedNow

    def moviesPastDueDate(self, movieRepo):
        """
        Get list of movies past due date
        """
        rentalsPassedDueDate = []
        constants = Constants()
        for rental in self.getRentalList():
            if rental.getReturnedDate() is None and rental.getDueDate().isBeforeDate(self.__constants.currentDay()):
                rentalsPassedDueDate.append(rental)

        for i in range(0, len(rentalsPassedDueDate) - 1):
            for j in range(i + 1, len(rentalsPassedDueDate)):
                if constants.currentDay().daysUntilDate(rentalsPassedDueDate[i].getRentedDate()) < constants.currentDay().daysUntilDate(rentalsPassedDueDate[j].getRentedDate()):
                    aux = rentalsPassedDueDate[i]
                    rentalsPassedDueDate[i] = rentalsPassedDueDate[j]
                    rentalsPassedDueDate[j] = aux

        moviesPassedDueDateSorted = []
        for rental in rentalsPassedDueDate:
            moviesPassedDueDateSorted.append(movieRepo.getMovieWithId(rental.getMovieId()))
        return moviesPassedDueDateSorted
