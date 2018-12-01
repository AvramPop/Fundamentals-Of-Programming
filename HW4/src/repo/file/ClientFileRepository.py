from src.dao.ClientDAO import ClientDAO
from src.repo.inmemory.ClientRepo import ClientRepo


class ClientFileRepository(ClientRepo):

    def __init__(self, fileName) -> None:
        super().__init__()
        self.__fileName = fileName
        self.__file = None

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
            clientToAdd = ClientDAO(splitLine[1])
            clientToAdd.setClientId(int(splitLine[0]))
            super().addClientWithId(clientToAdd)
        self.__closeFile()

    def __storeRepo(self):
        self.__loadFileWriteMode()
        self.__file.write("")
        for client in super().getList():
            self.__file.write(self.clientToString(client))
        self.__closeFile()

    def clientToString(self, clientDAO):
        return str(clientDAO.getId()) + " " + clientDAO.getName() + "\n"

    def cleanFile(self):
        self.__loadFileWriteMode()
        self.__file.write("")
        self.__closeFile()
