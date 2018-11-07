from main.model import Rental


class RentalRepo:
    __shared_state = {}
    __rentalList = []

    def __init__(self):
        self.__dict__ = self.__shared_state

    def hasRentalWithId(self, rentalId):
        for rental in self.__rentalList:
            if rental.getRentalId() == rentalId:
                return True
        return False

    def addRental(self, rental):
        # print(type(rental).__name__ == 'Rental')
        if type(rental).__name__ == 'Rental':
            rental.setRentalId(len(self.__rentalList))
            self.__rentalList.append(rental)
        else:
            raise TypeError

    def getRentalList(self):
        return self.__rentalList
