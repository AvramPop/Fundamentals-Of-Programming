from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException, \
    ObjectAlreadyInCollectionException, IdNotSetException
from main.model.Client import Client


class ClientRepo:
    __shared_state = {}
    __clientList = []

    def __init__(self):
        self.__dict__ = self.__shared_state

    # def hasClientWithName(self, name):
    #     """
    #     Checks whether there is a client with name
    #     :return: True it exists, False otherwise
    #     """
    #     for client in self.__clientList:
    #         if client.getName() == name:
    #             return True
    #     return False

    # def getClientWithName(self, name):
    #     for client in self.__clientList:
    #         if client.getName() == name:
    #             return client
    #     raise ObjectNotInCollectionException

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
    #
    # def removeClientWithName(self, name):
    #     """
    #     Remove client with name from repo
    #     """
    #     indexOfClientToRemoveInList = -1
    #     for i in range(0, len(self.__clientList)):
    #         if (self.__clientList[i]).getName() == name:
    #             indexOfClientToRemoveInList = i
    #
    #     if indexOfClientToRemoveInList == -1:
    #         raise ObjectNotInCollectionException
    #     else:
    #         del self.__clientList[indexOfClientToRemoveInList]

    def updateClientWithId(self, clientId, updatedClient):
        """
        Override client with clientId with updatedClient
        """
        # if updatedClient.hasIdSet():
        #     if updatedClient.getClientId() != clientId:
        #         raise UpdatingObjectWithDifferentIdException
        indexOfClientToUpdateInList = -1
        for i in range(0, len(self.__clientList)):
            if (self.__clientList[i]).getClientId() == clientId:
                indexOfClientToUpdateInList = i

        if indexOfClientToUpdateInList == -1:
            raise ObjectNotInCollectionException
        else:
            updatedClient.setClientId(clientId)
            self.__clientList[indexOfClientToUpdateInList] = updatedClient

        # try:
        #     self.removeClientWithId(clientId)
        # except ObjectNotInCollectionException as objectNotInCollectionException:
        #     raise objectNotInCollectionException
        #
        # if not updatedClient.hasIdSet():
        #     updatedClient.setClientId(clientId)
        # self.addClient(updatedClient)
    #
    # def updateClientName(self, actualName, newName):
    #     """
    #     Update client with actualName to newName
    #     """
    #     clientFound = False
    #     for i in range(0, len(self.__clientList)):
    #         if self.__clientList[i].getName() == actualName:
    #             self.__clientList[i].setName(newName)
    #             clientFound = True
    #     if not clientFound:
    #         raise ObjectNotInCollectionException

    def __sortClientList(self):
        for i in range(0, len(self.__clientList) - 1):
            for j in range(i + 1, len(self.__clientList)):
                if (self.__clientList[j]).getClientId() < self.__clientList[i].getClientId():
                    auxClient = self.__clientList[j]
                    self.__clientList[j] = self.__clientList[i]
                    self.__clientList[i] = auxClient

    # def printClientList(self):
    #     for client in self.__clientList:
    #         print(str(client))

    # def cleanClientList(self):
    #     self.__clientList = []

    # def getClientIdByName(self, name):
    #     for client in self.__clientList:
    #         if client.getName() == name:
    #             return client.getClientId()
    #     raise ObjectNotInCollectionException

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
