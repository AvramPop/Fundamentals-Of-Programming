from main.model.Client import Client


class ClientRepo:
    __shared_state = {}
    __clientList = []

    def __init__(self):
        self.__dict__ = self.__shared_state

    def hasClientWithId(self, clientId):
        for client in self.__clientList:
            if client.getClientId() == clientId:
                return True
        return False

    def addClient(self, client):
        client.setClientId(len(self.__clientList))
        self.__clientList.append(client)

    def getClientList(self):
        return self.__clientList
