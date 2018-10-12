import math


def isPrime(x):
    """
    Function that tests whether an integer is prime or not
    :param x:
    :return: True if x is prime, False else
    """
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    d = 3
    while d <= int(math.sqrt(x)) + 1:
        if x % d == 0:
            return False
        d += 2
    return True


def addIntToList(inputList, valueInserted):
    """
    Function that appends an int value valueInserted to bottom of list inputList
    input: valueInserted, inputList
    preconditions: l = [10, 11, ..., ln], li, i = 0, n - 1, li - integers, x - integer
    output: l'
    postconditions: l' = l U (valueInserted) = [10, 11, ..., ln-1, valueInserted]
    """
    inputList.append(valueInserted)


def listOfPrimes(inputList):
    '''
    Function that returns a list of primes from the input list of integers inputList
    :param inputList: input list
    :return: listOfPrimesFromInputList: the list of primes in inputList
    '''

    listOfPrimesFromInputList = []
    for i in inputList:
        if isPrime(i):
            listOfPrimesFromInputList.append(i)
    print(listOfPrimesFromInputList)
    return listOfPrimesFromInputList


def isPrimeTest():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(4) is False
    assert isPrime(55) is False
    assert isPrime(49) is False
    assert isPrime(2) is True
    assert isPrime(3) is True


def addIntToListTest():
    l = []
    assert len(l) == 0
    addIntToList(l, 1)
    assert l == [1]
    addIntToList(l, 2)
    assert l == [1, 2]


def listOfPrimesTest():
    l = [23, 2, 5, 24]
    assert listOfPrimes(l) is [23, 2, 5]


def printListToConsole(inputList):
    s = ""
    for el in inputList:
        s += str(el) + " "
    print(s)


def UIPrint(inputList):
    if len(inputList) > 0:
        print("The elements in the list: ")
        printListToConsole(inputList)
    else:
        print("empty list!")


def UIAdd(inputList):
    valueInserted = input("please insert a int value: ")
    # while not type(valueInserted):
    while True:
        try:
            valueInserted = int(valueInserted)
            addIntToList(inputList, valueInserted)
            return
            # valueInserted = input("please insert a int value")
        except ValueError as ve:
            print("invalid integer input. please input again")
            return


def runTests():
    addIntToListTest()
    isPrimeTest()
    listOfPrimesTest()


def UIPrintListOfPrimes(inputList):
    listOfPrime = listOfPrimes(inputList)
    print("Your list of primes:")
    print(listOfPrime)


def main():
    inputList = []
    commands = {"add": UIAdd(inputList), "prime": UIPrintListOfPrimes(inputList), "print": UIPrint(inputList)}
    while True:
        userInput = input(">")
        if userInput in commands:
            commands[userInput](inputList)
        elif userInput == "exit":
            return
        else:
            print("invalid command!")


runTests()
main()
