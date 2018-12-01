from src.Exception import ObjectNotInCollectionException, AlreadySetException, DatesNotOrderedException
from src.Date import Date
from src.repo.inmemory.ClientRepo import ClientRepo
from src.repo.inmemory.MovieRepo import MovieRepo


class RentalDAO:
    """
    Models rental having <rentalID> (int, default = None), <movieId> (int, existing in MovieRepo),
    <clientId> (int, existing in ClientRepo), <rented date> (Date), <due date> (Date), <returned date> (Date, default none).
    """
    def __init__(self, clientId, movieId, rentedDate, dueDate, movieRepo = None, clientRepo = None) -> None:
        self.__rentalId = None
        self.__returnedDate = None

        if type(movieId) == int:
            if movieId >= 0:
                if movieRepo is not None:
                    if movieRepo.hasMovieWithId(movieId):
                        self.__movieId = movieId
                    else:
                        raise ObjectNotInCollectionException("movie with id does not exits")
                else:
                    self.__movieId = movieId
            else:
                raise ValueError
        else:
            raise ValueError("invalid movie id")

        if type(clientId) == int:
            if clientId >= 0:
                if clientRepo is not None:
                    if clientRepo.hasClientWithId(clientId):
                        self.__clientId = clientId
                    else:
                        raise ObjectNotInCollectionException("client with id does not exist")
                else:
                    self.__clientId = clientId
            else:
                raise ValueError
        else:
            raise ValueError("invalid client id")

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

    def setReturnedDateToNone(self):
        self.__returnedDate = None

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

    def getId(self):
        """
        Get rental id

        :return: rental id, if not None
        :raises TypeError: if the rental id is not set
        """
        return self.__rentalId

    def isRented(self):
        if self.__returnedDate is None:
            return True
        else:
            return False

    def getReturnedDate(self):
        return self.__returnedDate

    def getMovieId(self):
        return self.__movieId

    def getClientId(self):
        return self.__clientId

    def getRentedDate(self):
        return self.__rentedDate

    def getDueDate(self):
        return self.__dueDate

    def __eq__(self, other: "RentalDAO"):
        return self.__rentalId == other.getId() and self.__movieId == other.getMovieId() and \
               self.__clientId == other.getClientId() and self.__returnedDate == other.getReturnedDate() and \
               self.__dueDate == other.getDueDate() and self.__rentedDate == other.getRentedDate()

    def __str__(self) -> str:
        return "Rental id: " + str(self.__rentalId) + ", movieId: " + \
               str(self.__movieId) + ", clientId: " + str(self.__clientId) + \
               ", rented date: " + str(self.__rentedDate) + ", due date: " + \
               str(self.__dueDate) + ", returned date: " + str(self.__returnedDate)
