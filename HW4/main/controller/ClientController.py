from main.repo.ClientRepo import ClientRepo


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

    def removeClientWithId(self, clientId):
        self.__clientRepo.removeClientWithId(clientId)

    def updateClientWithId(self, clientId, updatedClient):
        self.__clientRepo.updateClientWithId(clientId, updatedClient)

    def populateRepo(self):
        self.__clientRepo.populate()
