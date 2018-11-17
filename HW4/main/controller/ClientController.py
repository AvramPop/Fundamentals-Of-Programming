from main.Constants import Constants
from main.Exception import ClientHasMoviesNotReturnedException
from main.Utils import stringsPartiallyMatch
from main.repo.ClientRepo import ClientRepo
from difflib import SequenceMatcher


class ClientController:

    def __init__(self, clientRepo) -> None:
        self.__clientRepo = clientRepo

    def getRepo(self):
        return self.__clientRepo

    def addClient(self, client):
        self.__clientRepo.addClient(client)

    def getClientWithId(self, clientId):
        return self.__clientRepo.getClientWithId(clientId)

    def hasClientWithId(self, clientId):
        return self.__clientRepo.hasClientWithId(clientId)

    def getClientList(self):
        return self.__clientRepo.getList()

    def removeClientWithId(self, clientId, rentalRepo):
        if not self.clientHasMoviesNotReturned(clientId, rentalRepo):
            self.__clientRepo.removeClientWithId(clientId)
        else:
            raise ClientHasMoviesNotReturnedException

    def updateClientWithId(self, clientId, updatedClient):
        self.__clientRepo.updateClientWithId(clientId, updatedClient)

    def populateRepo(self):
        self.__clientRepo.populate()

    def listOfClientsWithName(self, clientNameToFind):
        clientListWithPartialNameCorresponding = []
        for client in self.getClientList():
            if stringsPartiallyMatch(client.getName(), clientNameToFind):
                clientListWithPartialNameCorresponding.append(client)
        return clientListWithPartialNameCorresponding

    def clientHasMoviesNotReturned(self, clientId, rentalRepo):
        constants = Constants()
        for rental in rentalRepo.getList():
            if rental.getClientId() == clientId:
                if rental.getReturnedDate() is None and rental.getDueDate().isBeforeDate(constants.currentDay()):
                    return True
        return False

