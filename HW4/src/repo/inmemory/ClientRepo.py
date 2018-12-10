from src.Exception import ObjectNotInCollectionException, ObjectAlreadyInCollectionException
from src.List import List, sortListByObjectAttribute
from src.Utils import sortListById
from src.dao.ClientDAO import ClientDAO
from src.repo.Repository import Repository


class ClientRepo(Repository):

    def __init__(self) -> None:
        self.__clientList = List()

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
        if type(client).__name__ == 'ClientDAO':
            if not ClientRepo.hasClientWithId(self, client.getId()):
                client.setClientId(self.__maximumIndexInClientList() + 1)
                self.__clientList.append(client)
                sortListByObjectAttribute(self.__clientList, lambda a, b: True if a < b else False, lambda a: a.getId())
                # sortListById(self.__clientList)
                # self.__sortClientList()
            else:
                raise ObjectAlreadyInCollectionException
        else:
            raise TypeError

    def getList(self):  # caution use
        return self.__clientList

    def addClientWithId(self, client):
        self.__clientList.append(client)
        sortListByObjectAttribute(self.__clientList, lambda a, b: True if a < b else False, lambda a: a.getId())

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
        self.addClient(ClientDAO("Dani"))
        self.addClient(ClientDAO("Ancu"))
        self.addClient(ClientDAO("Ana"))
        self.addClient(ClientDAO("Betu"))
        self.addClient(ClientDAO("Sami"))
        self.addClient(ClientDAO("Dave"))
        self.addClient(ClientDAO("Mami"))
        self.addClient(ClientDAO("Tati"))
        self.addClient(ClientDAO("Sergiu"))
        self.addClient(ClientDAO("Adi"))
        self.addClient(ClientDAO("Cristi"))
        self.addClient(ClientDAO("Anisoara"))

    def populateWithMany(self):
        self.addClient(ClientDAO("Dani"))
        self.addClient(ClientDAO("Ancu"))
        self.addClient(ClientDAO("Ana"))
        self.addClient(ClientDAO("Betu"))
        self.addClient(ClientDAO("Sami"))
        self.addClient(ClientDAO("Dave"))
        self.addClient(ClientDAO("Mami"))
        self.addClient(ClientDAO("Tati"))
        self.addClient(ClientDAO("Sergiu"))
        self.addClient(ClientDAO("Adi"))
        self.addClient(ClientDAO("Cristi"))
        self.addClient(ClientDAO("Anisoara"))
        self.addClient(ClientDAO("AA"))
        self.addClient(ClientDAO("AA1"))
        self.addClient(ClientDAO("AA2"))
        self.addClient(ClientDAO("AA3"))
        self.addClient(ClientDAO("AA4"))
        self.addClient(ClientDAO("AA5"))
        self.addClient(ClientDAO("AA6"))
        self.addClient(ClientDAO("AA7"))
        self.addClient(ClientDAO("AA8"))
        self.addClient(ClientDAO("AA9"))
        self.addClient(ClientDAO("AA0"))
        self.addClient(ClientDAO("AA12"))
        self.addClient(ClientDAO("AA11"))
        self.addClient(ClientDAO("AA22"))
        self.addClient(ClientDAO("AA33"))
        self.addClient(ClientDAO("AA55"))
        self.addClient(ClientDAO("AA44"))
        self.addClient(ClientDAO("AA66"))
        self.addClient(ClientDAO("AA77"))
        self.addClient(ClientDAO("AA88"))
        self.addClient(ClientDAO("AA99"))
        self.addClient(ClientDAO("AA000"))
        self.addClient(ClientDAO("AA111"))
        self.addClient(ClientDAO("AA222"))
        self.addClient(ClientDAO("AA333"))
        self.addClient(ClientDAO("AA444"))
        self.addClient(ClientDAO("AA555"))
        self.addClient(ClientDAO("AA666"))
        self.addClient(ClientDAO("AA777"))
        self.addClient(ClientDAO("A88A"))
        self.addClient(ClientDAO("AA999"))
        self.addClient(ClientDAO("AA000"))
        self.addClient(ClientDAO("AA11111"))
        self.addClient(ClientDAO("AdAAi"))
        self.addClient(ClientDAO("CriAAsti"))
        self.addClient(ClientDAO("AnisAAoara"))

    def clean(self):
        self.__clientList = List()
