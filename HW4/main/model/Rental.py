from main.Exception import InvalidDateFormatException, ObjectNotInCollectionException, SetToNotNoneException, DatesNotOrderedException
from main.repo.ClientRepo import ClientRepo
from main.repo.MovieRepo import MovieRepo
from main.model.Date import Date


class Rental:
    """
    Models rental having <rentalID> (int, default = None), <movieId> (int, existing in MovieRepo),
    <clientId> (int, existing in ClientRepo), <rented date> (Date), <due date> (Date), <returned date> (Date, default none).
    """
    def __init__(self, movieId, clientId, rentedDate, dueDate) -> None:
        self.__rentalId = None
        self.__returnedDate = None

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

        movieRepo = MovieRepo()
        if movieRepo.hasMovieWithId(movieId):
            self.__movieId = movieId
        else:
            raise ObjectNotInCollectionException("movie with id does not exits")
        del movieRepo

        clientRepo = ClientRepo()
        if clientRepo.hasClientWithId(clientId):
            self.__clientId = clientId
        else:
            raise ObjectNotInCollectionException("client with id does not exist")
        del clientRepo  # TODO potentially harmful?

    def setRentalId(self, rentalId):
        """
        Set rentalId to rentalId, if not previously set. (Default None)

        :param rentalId: (int > 0) the id to be set
        :raises ValueError: rentalId not int > 0
        :raises SetIdNotNoneException: rentalId already set
        """
        if self.__rentalId is None:
            if type(rentalId) != int or rentalId <= 0:
                raise ValueError("invalid id")
            else:
                self.__rentalId = rentalId
        else:
            raise SetToNotNoneException

    def setReturnedDate(self, returnedDate):
        if self.__returnedDate is None:
            try:
                self.__returnedDate = returnedDate
            except InvalidDateFormatException as invalidDateFormatException:
                raise invalidDateFormatException
        else:
            raise SetToNotNoneException

    def getRentalId(self):
        rentalId = self.__rentalId
        if rentalId is None:
            raise TypeError("rentalId not set. maybe not in list")
        return rentalId

    def getReturnedDate(self):
        returnedDate = self.__returnedDate
        if returnedDate is None:
            raise TypeError("returnedDate not set. maybe not in list")
        return returnedDate

    def getMovieId(self):
        return self.__movieId

