class RentalRepo:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.__rentalList = []

    def hasRentalWithId(self, rentalId):
        return True  # TODO rally change this please
