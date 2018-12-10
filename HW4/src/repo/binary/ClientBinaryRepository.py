import pickle

from src.List import List
from src.repo.inmemory.ClientRepo import ClientRepo


class ClientBinaryRepository(ClientRepo):

    def __init__(self, fileName) -> None:
        super().__init__()
        self.__fileName = fileName

    def hasClientWithId(self, clientId):
        self.__loadRepo()
        hasClientWithId = super().hasClientWithId(clientId)
        super().clean()
        return hasClientWithId

    def addClient(self, client):
        self.__loadRepo()
        super().addClient(client)
        self.__storeRepo()
        super().clean()

    def getList(self):
        self.__loadRepo()
        clientList = super().getList()
        super().clean()
        return clientList

    def addClientWithId(self, client):
        self.__loadRepo()
        super().addClientWithId(client)
        self.__storeRepo()
        super().clean()

    def getClientWithId(self, clientId):
        self.__loadRepo()
        client = super().getClientWithId(clientId)
        super().clean()
        return client

    def removeClientWithId(self, clientId):
        self.__loadRepo()
        super().removeClientWithId(clientId)
        self.__storeRepo()
        super().clean()

    def updateClientWithId(self, clientId, updatedClient):
        self.__loadRepo()
        super().updateClientWithId(clientId, updatedClient)
        self.__storeRepo()
        super().clean()

    def __loadRepo(self):
        file = open(self.__fileName, "rb")
        try:
            readRepo = pickle.load(file)
        except EOFError:
            readRepo = List()
        for client in readRepo:
            super().addClientWithId(client)
        file.close()

    def __storeRepo(self):
        file = open(self.__fileName, "wb")
        pickle.dump(super().getList(), file)
        file.close()

    def cleanFile(self):
        file = open(self.__fileName, "wb")
        pickle.dump(List(), file)
        file.close()
