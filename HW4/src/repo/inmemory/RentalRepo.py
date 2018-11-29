from src.Constants import Constants
from src.Exception import ObjectAlreadyInCollectionException, ObjectNotInCollectionException
from src.Utils import sortListById
from src.dao.RentalDAO import RentalDAO
from src.Date import Date


class RentalRepo:
    __constants = Constants()

    def __init__(self) -> None:
        self.__rentalList = []

    def hasRentalWithId(self, rentalId):
        """
        Checks whether there is a rental in the repo with rentalId
        """
        for rental in self.__rentalList:
            if rental.getId() == rentalId:
                return True
        return False

    def addRental(self, rental):
        if type(rental).__name__ == 'RentalDAO':
            if not self.hasRentalWithId(rental.getId()):
                rental.setRentalId(self.__maximumIndexInRentalList() + 1)
                self.__rentalList.append(rental)
                # self.__sortRentalList()
                sortListById(self.__rentalList)
            else:
                raise ObjectAlreadyInCollectionException
        else:
            raise TypeError

    def __maximumIndexInRentalList(self):
        maximumIndex = -1
        for rental in self.__rentalList:
            if rental.getId() > maximumIndex:
                maximumIndex = rental.getId()
        return maximumIndex

    def getList(self):  # caution use
        return self.__rentalList

    def getRentalWithId(self, rentalId):
        for rental in self.__rentalList:
            if rental.getId() == rentalId:
                return rental
        raise ObjectNotInCollectionException

    def removeRentalWithId(self, rentalId):
        """
        Remove rental with rentalId from repo
        """
        indexOfRentalToRemoveInList = -1
        for i in range(0, len(self.__rentalList)):
            if (self.__rentalList[i]).getId() == rentalId:
                indexOfRentalToRemoveInList = i

        if indexOfRentalToRemoveInList == -1:
            raise ObjectNotInCollectionException
        else:
            del self.__rentalList[indexOfRentalToRemoveInList]

    def updateRentalWithId(self, rentalId, updatedRental):
        """
        Update rental with rentalId to updatedRental
        """
        indexOfRentalToUpdateInList = -1
        for i in range(0, len(self.__rentalList)):
            if (self.__rentalList[i]).getId() == rentalId:
                indexOfRentalToUpdateInList = i

        if indexOfRentalToUpdateInList == -1:
            raise ObjectNotInCollectionException
        else:
            if updatedRental.getId() is None:
                updatedRental.setRentalId(rentalId)
            self.__rentalList[indexOfRentalToUpdateInList] = updatedRental

    def populateWithFew(self, movieRepo, rentalRepo):
        self.addRental(RentalDAO(0, 0, Date(12, 5, 2011), Date(13, 6, 2012), movieRepo, rentalRepo))
        self.addRental(RentalDAO(1, 1, Date(12, 5, 2012), Date(13, 6, 2019), movieRepo, rentalRepo))
        self.__rentalList[1].setReturnedDate(Date(12, 6, 2013))
        self.addRental(RentalDAO(2, 2, Date(12, 5, 2013), Date(13, 6, 2013), movieRepo, rentalRepo))
        self.__rentalList[2].setReturnedDate(Date(12, 6, 2014))
        self.addRental(RentalDAO(3, 3, Date(12, 5, 2014), Date(13, 6, 2014), movieRepo, rentalRepo))
        self.__rentalList[3].setReturnedDate(Date(12, 6, 2015))
        self.addRental(RentalDAO(4, 4, Date(12, 5, 2015), Date(13, 6, 2015), movieRepo, rentalRepo))
        self.__rentalList[4].setReturnedDate(Date(12, 6, 2016))
        self.addRental(RentalDAO(5, 5, Date(12, 5, 2016), Date(13, 6, 2016), movieRepo, rentalRepo))
        self.__rentalList[5].setReturnedDate(Date(12, 6, 2017))
        self.addRental(RentalDAO(6, 6, Date(12, 5, 2001), Date(13, 6, 2001), movieRepo, rentalRepo))
        self.__rentalList[6].setReturnedDate(Date(12, 6, 2002))
        self.addRental(RentalDAO(7, 7, Date(12, 5, 2002), Date(13, 6, 2002), movieRepo, rentalRepo))
        self.__rentalList[7].setReturnedDate(Date(12, 6, 2003))
        self.addRental(RentalDAO(8, 8, Date(12, 5, 2003), Date(13, 6, 2003), movieRepo, rentalRepo))
        self.__rentalList[8].setReturnedDate(Date(12, 6, 2004))
        self.addRental(RentalDAO(9, 9, Date(12, 5, 2004), Date(13, 6, 2004), movieRepo, rentalRepo))
        self.addRental(RentalDAO(10, 10, Date(12, 5, 2000), Date(13, 6, 2000), movieRepo, rentalRepo))
        self.__rentalList[10].setReturnedDate(Date(12, 6, 2006))

    def addRentalWithId(self, rental):
        self.__rentalList.append(rental)
        sortListById(self.__rentalList)

    def clean(self):
        self.__rentalList = []

