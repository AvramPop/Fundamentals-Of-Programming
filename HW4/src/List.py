def sortList(listToSort, compareFunction):
    """
    Sort listToSort by the compareFunction given
    """
    for i in range(len(listToSort) - 1):
        minimumIndex = i
        for j in range(i + 1, len(listToSort)):
            if compareFunction(listToSort[j], listToSort[minimumIndex]):
                minimumIndex = j
        if minimumIndex != i:
            temp = listToSort[minimumIndex]
            listToSort[minimumIndex] = listToSort[i]
            listToSort[i] = temp


def sortListByObjectAttribute(listToSort, compareFunction, getAttribute):
    """
    Sort listToSort by the compareFunction given, by attribute from getAttribute(listToSort[i])
    """
    for i in range(len(listToSort) - 1):
        minimumIndex = i
        for j in range(i + 1, len(listToSort)):
            if compareFunction(getAttribute(listToSort[j]), getAttribute(listToSort[minimumIndex])):
                minimumIndex = j
        if minimumIndex != i:
            temp = listToSort[minimumIndex]
            listToSort[minimumIndex] = listToSort[i]
            listToSort[i] = temp


def filterList(listToFilter, filterFunction):
    """
    Filter list by filterFunction
    """
    filteredList = []
    for element in listToFilter:
        if filterFunction(element):
            filteredList.append(element)
    return filteredList


class List:
    """
    Wrapper around the basic List with full compatibility
    """
    def __init__(self, data = None):
        self.__index = 0
        if data is not None:
            self.__list = list(data)
        else:
            self.__list = list()

    def insert(self, index, value):
        self.__list.insert(index, value)

    def append(self, value):
        self.insert(len(self.__list), value)

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, index):
        return self.__list[index]

    def __delitem__(self, index):
        del self.__list[index]

    def __setitem__(self, index, value):
        self.__list[index] = value

    def __str__(self):
        return str(self.__list)

    def __eq__(self, objectToCompareTo: object) -> bool:
        if not isinstance(objectToCompareTo, list) and not isinstance(objectToCompareTo, List):
            return False

        if len(objectToCompareTo) != len(self.__list):
            return False

        for i in range(len(self.__list)):
            if objectToCompareTo[i] != self.__list[i]:
                return False

        return True

    def __iter__(self):
        return self.__list.__iter__()

    def __next__(self):
        if self.__index > len(self.__list) - 1:
            raise StopIteration
        else:
            self.__index += 1
        return self.__list[self.__index]
