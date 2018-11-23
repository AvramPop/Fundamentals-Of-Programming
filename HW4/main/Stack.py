from main.Exception import EmptyStackException


class Stack:
    def __init__(self) -> None:
        self.__stack = []

    def push(self, element):
        self.__stack.append(element)

    def lastElement(self):
        lastIndex = len(self.__stack) - 1
        if lastIndex >= 0:
            return self.__stack[lastIndex]
        else:
            return None

    def deleteLastElement(self):
        self.__stack.pop()

    def pop(self):
        if len(self.__stack) == 0:
            raise EmptyStackException
        else:
            return self.__stack.pop()
