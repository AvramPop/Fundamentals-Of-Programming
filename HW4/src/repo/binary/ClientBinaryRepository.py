from src.repo.Repository import Repository


class ClientBinaryRepository(Repository):

    def __init__(self) -> None:
        super().__init__()

    def hasClientWithId(self, clientId):
        super().hasClientWithId(clientId)

    def addClient(self, client):
        super().addClient(client)

    def getList(self):
        super().getList()

    def addClientWithId(self, client):
        super().addClientWithId(client)

    def getClientWithId(self, clientId):
        super().getClientWithId(clientId)

    def removeClientWithId(self, clientId):
        super().removeClientWithId(clientId)

    def updateClientWithId(self, clientId, updatedClient):
        super().updateClientWithId(clientId, updatedClient)
