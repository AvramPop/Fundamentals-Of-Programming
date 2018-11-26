from main.Exception import ObjectNotInCollectionException, UpdatingObjectWithDifferentIdException, \
    ObjectAlreadyInCollectionException, IdNotSetException
from main.Utils import sortListById
from main.model.Client import Client


class ClientRepo:

    def __init__(self) -> None:
        self.__clientList = []

    def hasClientWithId(self, clientId):
        """
        Checks whether there is a client having clientId
        """
        for client in self.__clientList:
            if client.getId() == clientId:
                return True
        return False

    def addClient(self, client):
        """
        Add client to repo

        :param client: the client to add
        """
        if type(client).__name__ == 'Client':
            if not self.hasClientWithId(client.getId()):
                client.setClientId(self.__maximumIndexInClientList() + 1)
                self.__clientList.append(client)
                sortListById(self.__clientList)
                # self.__sortClientList()
            else:
                raise ObjectAlreadyInCollectionException
        else:
            raise TypeError

    def getList(self):
        return self.__clientList

    def addClientWithId(self, client):
        self.__clientList.append(client)
        sortListById(self.__clientList)

    def __maximumIndexInClientList(self):
        maximumIndex = -1
        for client in self.__clientList:
            if client.getId() > maximumIndex:
                maximumIndex = client.getId()
        return maximumIndex

    def getClientWithId(self, clientId):
        for client in self.__clientList:
            if client.getId() == clientId:
                return client
        raise ObjectNotInCollectionException

    def removeClientWithId(self, clientId):
        """
        Remove client with id
        :param clientId: the clientId to remove client with
        """
        indexOfClientToRemoveInList = -1
        for i in range(0, len(self.__clientList)):
            if (self.__clientList[i]).getId() == clientId:
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
            if (self.__clientList[i]).getId() == clientId:
                indexOfClientToUpdateInList = i

        if indexOfClientToUpdateInList == -1:
            raise ObjectNotInCollectionException
        else:
            if updatedClient.getId() is None:
                updatedClient.setClientId(clientId)
            self.__clientList[indexOfClientToUpdateInList] = updatedClient

    def populateWithFew(self):
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

    def populateWithMany(self):
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
        self.addClient(Client("AA"))
        self.addClient(Client("AA1"))
        self.addClient(Client("AA2"))
        self.addClient(Client("AA3"))
        self.addClient(Client("AA4"))
        self.addClient(Client("AA5"))
        self.addClient(Client("AA6"))
        self.addClient(Client("AA7"))
        self.addClient(Client("AA8"))
        self.addClient(Client("AA9"))
        self.addClient(Client("AA0"))
        self.addClient(Client("AA12"))
        self.addClient(Client("AA11"))
        self.addClient(Client("AA22"))
        self.addClient(Client("AA33"))
        self.addClient(Client("AA55"))
        self.addClient(Client("AA44"))
        self.addClient(Client("AA66"))
        self.addClient(Client("AA77"))
        self.addClient(Client("AA88"))
        self.addClient(Client("AA99"))
        self.addClient(Client("AA000"))
        self.addClient(Client("AA111"))
        self.addClient(Client("AA222"))
        self.addClient(Client("AA333"))
        self.addClient(Client("AA444"))
        self.addClient(Client("AA555"))
        self.addClient(Client("AA666"))
        self.addClient(Client("AA777"))
        self.addClient(Client("A88A"))
        self.addClient(Client("AA999"))
        self.addClient(Client("AA000"))
        self.addClient(Client("AA11111"))
        self.addClient(Client("AdAAi"))
        self.addClient(Client("CriAAsti"))
        self.addClient(Client("AnisAAoara"))

    def clean(self):
        self.__clientList = []
