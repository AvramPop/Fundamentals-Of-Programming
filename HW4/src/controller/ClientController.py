from src.Constants import Constants
from src.Exception import ClientHasMoviesNotReturnedException
from src.List import List
from src.Utils import stringsPartiallyMatch


class ClientController:

    def __init__(self, clientRepo) -> None:
        self.__clientRepo = clientRepo

    def getRepo(self):
        """
        Get Controller Repo (Client Repo)
        """
        return self.__clientRepo

    def addClientWithId(self, client):
        """
        Add client to repo.
        """
        self.__clientRepo.addClientWithId(client)

    def addClient(self, client):
        """
        Add client to repo.
        """
        self.__clientRepo.addClient(client)

    def getClientWithId(self, clientId):
        """
        Get client having id clientId
        """
        return self.__clientRepo.getClientWithId(clientId)

    def hasClientWithId(self, clientId):
        """
        Checks whether there is a client with sought id
        """
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

    def populateRepoWithFew(self):
        self.__clientRepo.populateWithFew()

    def populateRepoWithMany(self):
        self.__clientRepo.populateWithMany()

    def listOfClientsWithName(self, clientNameToFind):
        clientListWithPartialNameCorresponding = List()
        for client in self.getClientList():
            if stringsPartiallyMatch(client.getName(), clientNameToFind):
                clientListWithPartialNameCorresponding.append(client)
        return clientListWithPartialNameCorresponding

    def clientHasMoviesNotReturned(self, clientId, rentalRepo):
        """
        Checks whether client has movies not returned
        """
        constants = Constants()
        for rental in rentalRepo.getList():
            if rental.getClientId() == clientId:
                if rental.getReturnedDate() is None and rental.getDueDate().isBeforeDate(constants.currentDay()):
                    return True
        return False
