from main.Exception import SetToNotNoneException


class Client:
    """
    Models a client having <clientId>(int, default None), <name>(string).
    """
    def __init__(self, name) -> None:
        self.__clientId = None

        if type(name) == str:
            self.__name = name
        else:
            raise ValueError

    def getName(self):
        return self.__name

    def getClientId(self):
        clientId = self.__clientId
        if clientId is None:
            raise TypeError("clientId not set. maybe not in list")
        return clientId

    def setClientId(self, clientId):
        """
        Set clientId to clientId, if not previously set. (Default None)

        :param clientId: (int > 0) the id to be set
        :raises ValueError: clientId not int > 0
        :raises SetIdNotNoneException: clientId already set
        """
        if self.__clientId is None:
            if type(clientId) != int or clientId <= 0:
                raise ValueError("invalid id")
            else:
                self.__clientId = clientId
        else:
            raise SetToNotNoneException

    def __eq__(self, otherClient: 'Client') -> bool:
        return self.__name == otherClient.getName() and self.__clientId == otherClient.getClientId()


