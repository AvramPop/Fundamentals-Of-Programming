from main.repo.ClientRepo import ClientRepo


class ClientController:
    __clientRepo = ClientRepo()
    __clientRepo.populate()

    def addClient(self, client):
        self.__clientRepo.addClient(client)

    def getClientWithId(self, clientId):
        return self.__clientRepo.getClientWithId(clientId)

    def getClientList(self):
        return self.__clientRepo.getList()

    def removeClientWithId(self, clientId):
        self.__clientRepo.removeClientWithId(clientId)

    def updateClientWithId(self, clientId, updatedClient):
        self.__clientRepo.updateClientWithId(clientId, updatedClient)
