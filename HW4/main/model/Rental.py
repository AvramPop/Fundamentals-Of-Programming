from main.Exception import ObjectNotInCollectionException, AlreadySetException, DatesNotOrderedException, \
    IdNotSetException
from main.model.Date import Date
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo


class Rental:
    """
    Models rental having <rentalID> (int, default = None), <movieId> (int, existing in MovieRepo),
    <clientId> (int, existing in ClientRepo), <rented date> (Date), <due date> (Date), <returned date> (Date, default none).
    """
    def __init__(self, movieId, clientId, rentedDate, dueDate) -> None:
        self.__rentalId = None
        self.__returnedDate = None

        movieRepo = MovieRepo()
        if type(movieId) == int:
            if movieId >= 0:
                if movieRepo.hasMovieWithId(movieId):
                    self.__movieId = movieId
                else:
                    raise ObjectNotInCollectionException("movie with id does not exits")
            else:
                raise ValueError
        else:
            raise ValueError("invalid movie id")
        del movieRepo

        clientRepo = ClientRepo()
        if type(clientId) == int:
            if clientId >= 0:
                if clientRepo.hasClientWithId(clientId):
                    self.__clientId = clientId
                else:
                    raise ObjectNotInCollectionException("client with id does not exist")
            else:
                raise ValueError
        else:
            raise ValueError("invalid client id")
        del clientRepo  # TODO potentially harmful?

        if type(rentedDate) == Date:
            self.__rentedDate = rentedDate
        else:
            raise ValueError

        if type(dueDate) == Date:
            if not dueDate.isBeforeDate(rentedDate):
                self.__dueDate = dueDate
            else:
                raise DatesNotOrderedException
        else:
            raise ValueError

    def setRentalId(self, rentalId):
        """
        Set rentalId to rentalId, if not previously set. (Default None)

        :param rentalId: (int > 0) the id to be set
        :raises ValueError: rentalId not int > 0
        :raises SetIdNotNoneException: rentalId already set
        """
        if self.__rentalId is None:
            if type(rentalId) != int:
                raise ValueError("invalid id")
            elif rentalId < 0:
                raise ValueError
            else:
                self.__rentalId = rentalId
        else:
            raise AlreadySetException

    def setReturnedDate(self, returnedDate):
        """
        Set returned date

        :param returnedDate: the returned date to set
        :raises ValueError: if returnedDate is not a Date
        :raises AlreadySetException: if the returned date is already set
        """
        if self.__returnedDate is None:
            if type(returnedDate) == Date:
                self.__returnedDate = returnedDate
            else:
                raise ValueError
        else:
            raise AlreadySetException

    # def getMovie(self):
    #     movieRepo = MovieRepo()
    #     for movie in movieRepo.getMovieList():
    #         if movie.getMovieId() == self.__movieId:
    #             return movie
    #     del movieRepo

    def getRentalId(self):
        """
        Get rental id

        :return: rental id, if not None
        :raises TypeError: if the rental id is not set
        """
        rentalId = self.__rentalId
        if rentalId is None:
            raise IdNotSetException
        return rentalId

    def isRented(self):
        if self.__returnedDate is None:
            return True
        else:
            return False

    def getReturnedDate(self):
        returnedDate = self.__returnedDate
        if returnedDate is None:
            raise TypeError("returnedDate not set. maybe not in list")
        return returnedDate

    def getMovieId(self):
        return self.__movieId

    def getClientId(self):
        return self.__clientId

    def getRentedDate(self):
        return self.__rentedDate

    def getDueDate(self):
        return self.__dueDate

    # def setDueDate(self, dueDate):
    #     self.__dueDate = dueDate

    def __eq__(self, other: "Rental"):
        return self.__rentalId == other.getRentalId() and self.__movieId == other.getMovieId() and \
               self.__clientId == other.getClientId() and self.__returnedDate == other.getReturnedDate() and \
               self.__dueDate == other.getDueDate() and self.__rentedDate == other.getRentedDate()

    def __str__(self) -> str:
        return "Rental id: " + str(self.__rentalId) + ", movieId: " + \
               str(self.__movieId) + ", clientId: " + str(self.__clientId) + \
               ", rented date: " + str(self.__rentedDate) + ", due date: " + \
               str(self.__dueDate) + ", returned date: " + str(self.__returnedDate)
