from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException
from main.model.Client import Client


class ClientRepo:
    __shared_state = {}
    __clientList = []

    def __init__(self):
        self.__dict__ = self.__shared_state

    def hasClientWithName(self, name):
        for client in self.__clientList:
            if client.getName() == name:
                return True
        return False

    def getClientWithName(self, name):
        for client in self.__clientList:
            if client.getName() == name:
                return client
        raise ObjectNotInCollectionException

    def hasClientWithId(self, clientId):
        for client in self.__clientList:
            if client.getClientId() == clientId:
                return True
        return False

    def addClient(self, client):
        if type(client).__name__ == 'Client':
            if not client.hasIdSet():
                client.setClientId(len(self.__clientList))
            self.__clientList.append(client)
            self.sortClientList()
        else:
            raise TypeError

    def getClientList(self):
        return self.__clientList

    def getClientWithId(self, clientId):
        for client in self.__clientList:
            if client.getClientId() == clientId:
                return client
        raise ObjectNotInCollectionException

    def removeClientWithId(self, clientId):
        indexOfClientToRemoveInList = -1
        for i in range(0, len(self.__clientList)):
            if (self.__clientList[i]).getClientId() == clientId:
                indexOfClientToRemoveInList = i

        if indexOfClientToRemoveInList == -1:
            raise ObjectNotInCollectionException
        else:
            del self.__clientList[indexOfClientToRemoveInList]

    def removeClientWithName(self, name):
        indexOfClientToRemoveInList = -1
        for i in range(0, len(self.__clientList)):
            if (self.__clientList[i]).getName() == name:
                indexOfClientToRemoveInList = i

        if indexOfClientToRemoveInList == -1:
            raise ObjectNotInCollectionException
        else:
            del self.__clientList[indexOfClientToRemoveInList]

    def updateClientWithId(self, clientId, updatedClient):
        if updatedClient.hasIdSet():
            if updatedClient.getClientId() != clientId:
                raise UpdatingObjectWithDifferentIdException

        try:
            self.removeClientWithId(clientId)
        except ObjectNotInCollectionException as objectNotInCollectionException:
            raise objectNotInCollectionException

        if not updatedClient.hasIdSet():
            updatedClient.setClientId(clientId)
        self.addClient(updatedClient)

    def updateClientName(self, actualName, newName):
        clientFound = False
        for i in range(0, len(self.__clientList)):
            if self.__clientList[i].getName() == actualName:
                self.__clientList[i].setName(newName)
                clientFound = True
        if not clientFound:
            raise ObjectNotInCollectionException

    def sortClientList(self):
        for i in range(0, len(self.__clientList) - 1):
            for j in range(i + 1, len(self.__clientList)):
                if (self.__clientList[j]).getClientId() < self.__clientList[i].getClientId():
                    auxClient = self.__clientList[j]
                    self.__clientList[j] = self.__clientList[i]
                    self.__clientList[i] = auxClient

    def printClientList(self):
        for client in self.__clientList:
            print(str(client))

    def cleanClientList(self):
        self.__clientList = []

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
