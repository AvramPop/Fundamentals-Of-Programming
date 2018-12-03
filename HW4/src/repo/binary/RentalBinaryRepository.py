import pickle

from src.Date import Date
from src.dao.RentalDAO import RentalDAO
from src.repo.inmemory.RentalRepo import RentalRepo


class RentalBinaryRepository(RentalRepo):
    def __init__(self, fileName) -> None:
        super().__init__()
        self.__fileName = fileName
        self.__file = None

    def hasRentalWithId(self, rentalId):
        self.__loadRepo()
        hasRentalWithId = super().hasRentalWithId(rentalId)
        super().clean()
        return hasRentalWithId

    def addRental(self, rental):
        self.__loadRepo()
        super().addRental(rental)
        self.__storeRepo()
        super().clean()

    def getList(self):
        self.__loadRepo()
        rentalList = super().getList()
        super().clean()
        return rentalList

    def addRentalWithId(self, rental):
        self.__loadRepo()
        super().addRentalWithId(rental)
        self.__storeRepo()
        super().clean()

    def getRentalWithId(self, rentalId):
        self.__loadRepo()
        rental = super().getRentalWithId(rentalId)
        super().clean()
        return rental

    def removeRentalWithId(self, rentalId):
        self.__loadRepo()
        super().removeRentalWithId(rentalId)
        self.__storeRepo()
        super().clean()

    def updateRentalWithId(self, rentalId, updatedRental):
        self.__loadRepo()
        super().updateRentalWithId(rentalId, updatedRental)
        self.__storeRepo()
        super().clean()

    def __loadRepo(self):
        file = open(self.__fileName, "rb")
        try:
            readRepo = pickle.load(file)
        except EOFError:
            readRepo = []
        for rental in readRepo:
            super().addRentalWithId(rental)
        file.close()

    def __storeRepo(self):
        file = open(self.__fileName, "wb")
        pickle.dump(super().getList(), file)
        file.close()

    def cleanFile(self):
        file = open(self.__fileName, "wb")
        pickle.dump([], file)
        file.close()
