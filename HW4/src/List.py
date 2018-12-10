from collections import MutableSequence


def sortList(listToSort, compareFunction):
    for i in range(len(listToSort) - 1):
        minimumIndex = i
        for j in range(i + 1, len(listToSort)):
            if compareFunction(listToSort[j], listToSort[minimumIndex]):
                minimumIndex = j
        if minimumIndex != i:
            temp = listToSort[minimumIndex]
            listToSort[minimumIndex] = listToSort[i]
            listToSort[i] = temp


def filterList(listToFilter, filterFunction):
    filteredList = []
    for element in listToFilter:
        if filterFunction(element):
            filteredList.append(element)
    return filteredList


class List(MutableSequence):

    def __init__(self, data = None):
        super(List, self).__init__()
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

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, list) and not isinstance(o, List):
            return False

        if len(o) != len(self.__list):
            return False

        for i in range(len(self.__list)):
            if o[i] != self.__list[i]:
                return False

        return True

    def __iter__(self):
        return super().__iter__()
