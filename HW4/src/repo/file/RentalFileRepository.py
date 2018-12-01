from src.Date import Date
from src.dao.RentalDAO import RentalDAO
from src.repo.inmemory.RentalRepo import RentalRepo


class RentalFileRepository(RentalRepo):

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

    def __loadFileReadMode(self):
        self.__file = open(self.__fileName, "r")

    def __loadFileWriteMode(self):
        self.__file = open(self.__fileName, "w")

    def __closeFile(self):
        self.__file.close()

    def __loadRepo(self):
        self.__loadFileReadMode()
        for line in self.__file:
            splitLine = line.split()
            rentalToAdd = RentalDAO(int(splitLine[1]), int(splitLine[2]), Date(int(splitLine[3]), int(splitLine[4]), int(splitLine[5])), Date(int(splitLine[6]), int(splitLine[7]), int(splitLine[8])))
            rentalToAdd.setRentalId(int(splitLine[0]))
            if len(splitLine) >= 10:
                rentalToAdd.setReturnedDate(Date(int(splitLine[9]), int(splitLine[10]), int(splitLine[11])))
            super().addRentalWithId(rentalToAdd)
        self.__closeFile()

    def __storeRepo(self):
        self.__loadFileWriteMode()
        self.__file.write("")
        for rental in super().getList():
            self.__file.write(self.rentalToString(rental))
        self.__closeFile()

    def rentalToString(self, rentalDAO):
        string = str(rentalDAO.getId()) + " " + str(rentalDAO.getClientId()) + " " + str(rentalDAO.getMovieId()) + " "\
                 + str(rentalDAO.getRentedDate().day) + " " + str(rentalDAO.getRentedDate().month) + " " + str(rentalDAO.getRentedDate().year) + " "\
                 + str(rentalDAO.getDueDate().day) + " " + str(rentalDAO.getDueDate().month) + " " + str(rentalDAO.getDueDate().year) + " "
        if rentalDAO.getReturnedDate():
            string += str(rentalDAO.getReturnedDate().day) + " " + str(rentalDAO.getReturnedDate().month) + " " + str(rentalDAO.getReturnedDate().year)
        string += "\n"
        return string

    def cleanFile(self):
        self.__loadFileWriteMode()
        self.__file.write("")
        self.__closeFile()
