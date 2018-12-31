from src.Exceptions import RepositoryException


class Repository:
    def __init__(self) -> None:
        self.__data = []

    def add(self, entry):
        if entry not in self.__data:
            self.__data.append(entry)
        else:
            raise RepositoryException

    def getList(self):
        return self.__data
