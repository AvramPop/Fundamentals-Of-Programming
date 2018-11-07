from main.Constants import Constants
from main.model.Rental import Rental
from main.model.Date import Date


class RentalRepo:
    __shared_state = {}
    __rentalList = []
    __constants = Constants()

    def __init__(self):
        self.__dict__ = self.__shared_state

    def hasRentalWithId(self, rentalId):
        """
        Checks whether there is a rental in the repo with rentalId
        """
        for rental in self.__rentalList:
            if rental.getRentalId() == rentalId:
                return True
        return False

    def addRental(self, rental):  # TODO check unicity
        if type(rental).__name__ == 'Rental':

            rental.setRentalId(len(self.__rentalList))
            self.__rentalList.append(rental)
        else:
            raise TypeError

    def getRentalList(self):
        return self.__rentalList

    def printRentalList(self):
        for rental in self.__rentalList:
            print(str(rental))

    def clientHasMoviesNotReturned(self, clientId):
        """
        Checks whether client with clientId has at least one movie not returned
        """
        moviesRentedOvertime = False
        for rental in self.__rentalList:
            if rental.getClientId() == clientId:
                if rental.getDueDate().isBeforeDate(self.__constants.currentDay()) and rental.getMovie().isRented():
                    moviesRentedOvertime = True
        return moviesRentedOvertime

    def isMovieRented(self, movieId):
        """
        Checks whether the movie is rented
        """
        for rental in self.__rentalList:
            if rental.getMovieId() == movieId:
                return rental.getMovie().isRented()

    def clientHasMovieRented(self, clientId, movieId):
        """
        Checks whether client with clientId has movie with movieId rented
        """
        for rental in self.__rentalList:
            if rental.getMovieId() == movieId and rental.getClientId() == clientId and rental.getMovie().isRented():
                return True
        return False

    def returnMovie(self, clientId, movieId):
        """
        Set rental of movie with movieId by client with clientId returned date to today
        """
        for rental in self.__rentalList:
            if rental.getMovieId() == movieId and rental.getClientId() == clientId and rental.getMovie().isRented():
                rental.setReturnedDate(self.__constants.currentDay())
                rental.getMovie().returnMovie()

    def populate(self):  # TODO add missing attributes
        self.addRental(Rental(0, 0, Date(12, 5, 2011), Date(13, 6, 2012)))
        self.__rentalList[0].getMovie().rent()
        self.addRental(Rental(1, 1, Date(12, 5, 2012), Date(13, 6, 2019)))
        self.__rentalList[1].setReturnedDate(Date(12, 6, 2013))
        self.addRental(Rental(2, 2, Date(12, 5, 2013), Date(13, 6, 2013)))
        self.__rentalList[2].setReturnedDate(Date(12, 6, 2014))
        self.addRental(Rental(3, 3, Date(12, 5, 2014), Date(13, 6, 2014)))
        self.__rentalList[3].setReturnedDate(Date(12, 6, 2015))
        self.addRental(Rental(4, 4, Date(12, 5, 2015), Date(13, 6, 2015)))
        self.__rentalList[4].setReturnedDate(Date(12, 6, 2016))
        self.addRental(Rental(5, 5, Date(12, 5, 2016), Date(13, 6, 2016)))
        self.__rentalList[5].setReturnedDate(Date(12, 6, 2017))
        self.addRental(Rental(6, 6, Date(12, 5, 2001), Date(13, 6, 2001)))
        self.__rentalList[6].setReturnedDate(Date(12, 6, 2002))
        self.addRental(Rental(7, 7, Date(12, 5, 2002), Date(13, 6, 2002)))
        self.__rentalList[7].setReturnedDate(Date(12, 6, 2003))
        self.addRental(Rental(8, 8, Date(12, 5, 2003), Date(13, 6, 2003)))
        self.__rentalList[8].setReturnedDate(Date(12, 6, 2004))
        self.addRental(Rental(9, 9, Date(12, 5, 2004), Date(13, 6, 2004)))
        self.addRental(Rental(10, 10, Date(12, 5, 2000), Date(13, 6, 2000)))
        self.__rentalList[10].setReturnedDate(Date(12, 6, 2006))

