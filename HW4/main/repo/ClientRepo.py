class ClientRepo:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.__clientList = []

    def hasClientWithId(self, clientId):
        return True  # TODO rally change this please

    def addClient(self, client):
        self.__clientList.append(client)

    def getClientList(self):
        return self.__clientList
