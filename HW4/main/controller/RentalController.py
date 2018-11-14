from main.Constants import Constants
from main.Exception import DatesNotOrderedException, ClientHasMoviesNotReturnedException, MovieNotAvailableException, \
    MovieNotCurrentlyRentedByClientException
from main.model.Rental import Rental
from main.repo.RentalRepo import RentalRepo


class RentalController:
    __constants = Constants()

    def __init__(self, rentalRepo) -> None:
        self.__rentalRepo = rentalRepo

    def getRepo(self):
        return self.__rentalRepo

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
                        Rental(clientId, movieId, self.__constants.currentDay(), dueDate, movieRepo, clientRepo))

    def returnMovieByClient(self, clientId, movieId):
        movieFound = False
        for rental in self.getRentalList():
            if rental.getMovieId() == movieId and rental.getClientId() == clientId and rental.getReturnedDate() is None:
                constants = Constants()
                rental.setReturnedDate(constants.currentDay())
                self.updateRentalWithId(rental.getRentalId(), rental)
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
        self.__rentalRepo.populate(movieRepo, rentalRepo)
