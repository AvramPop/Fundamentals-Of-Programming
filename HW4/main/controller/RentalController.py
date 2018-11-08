from main.repo.RentalRepo import RentalRepo


class RentalController:
    __rentalRepo = RentalRepo()
    __rentalRepo.populate()

    def addRental(self, rental):
        self.__rentalRepo.addRental(rental)

    def getRentalWithId(self, rentalId):
        return self.__rentalRepo.getRentalWithId(rentalId)

    def getRentalList(self):
        return self.__rentalRepo.getList()

    def removeRentalWithId(self, rentalId):
        self.__rentalRepo.removeRentalWithId(rentalId)

    def updateRentalWithId(self, rentalId, updatedRental):
        self.__rentalRepo.updateRentalWithId(rentalId, updatedRental)
