from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException, \
    ObjectAlreadyInCollectionException, IdNotSetException
from main.model.Client import Client


class ClientRepo:

    def __init__(self) -> None:
        self.__clientList = []

    def hasClientWithId(self, clientId):
        """
        Checks whether there is a client having clientId
        """
        for client in self.__clientList:
            if client.getClientId() == clientId:
                return True
        return False

    def addClient(self, client):
        """
        Add client to repo

        :param client: the client to add
        """
        if type(client).__name__ == 'Client':
            if not self.hasClientWithId(client.getClientId()):
                client.setClientId(self.__maximumIndexInClientList() + 1)
                self.__clientList.append(client)
                self.__sortClientList()
            else:
                raise ObjectAlreadyInCollectionException
        else:
            raise TypeError


    def getList(self):
        return self.__clientList

    def __maximumIndexInClientList(self):
        maximumIndex = -1
        for client in self.__clientList:
            if client.getClientId() > maximumIndex:
                maximumIndex = client.getClientId()
        return maximumIndex

    def getClientWithId(self, clientId):
        for client in self.__clientList:
            if client.getClientId() == clientId:
                return client
        raise ObjectNotInCollectionException

    def removeClientWithId(self, clientId):
        """
        Remove client with id
        :param clientId: the clientId to remove client with
        """
        indexOfClientToRemoveInList = -1
        for i in range(0, len(self.__clientList)):
            if (self.__clientList[i]).getClientId() == clientId:
                indexOfClientToRemoveInList = i

        if indexOfClientToRemoveInList == -1:
            raise ObjectNotInCollectionException
        else:
            del self.__clientList[indexOfClientToRemoveInList]


    def updateClientWithId(self, clientId, updatedClient):
        """
        Override client with clientId with updatedClient
        """
        indexOfClientToUpdateInList = -1
        for i in range(0, len(self.__clientList)):
            if (self.__clientList[i]).getClientId() == clientId:
                indexOfClientToUpdateInList = i

        if indexOfClientToUpdateInList == -1:
            raise ObjectNotInCollectionException
        else:
            updatedClient.setClientId(clientId)
            self.__clientList[indexOfClientToUpdateInList] = updatedClient


    def __sortClientList(self):
        for i in range(0, len(self.__clientList) - 1):
            for j in range(i + 1, len(self.__clientList)):
                if (self.__clientList[j]).getClientId() < self.__clientList[i].getClientId():
                    auxClient = self.__clientList[j]
                    self.__clientList[j] = self.__clientList[i]
                    self.__clientList[i] = auxClient

    def populate(self):
        self.addClient(Client("Dani"))
        self.addClient(Client("Ancu"))
        self.addClient(Client("Ana"))
        self.addClient(Client("Betu"))
        self.addClient(Client("Sami"))
        self.addClient(Client("Dave"))
        self.addClient(Client("Mami"))
        self.addClient(Client("Tati"))
        self.addClient(Client("Sergiu"))
        self.addClient(Client("Adi"))
        self.addClient(Client("Cristi"))
        self.addClient(Client("Anisoara"))

    def clean(self):
        self.__clientList = []
