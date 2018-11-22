class Stack:
    def __init__(self) -> None:
        self.__stack = []

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        return self.__stack.pop()
