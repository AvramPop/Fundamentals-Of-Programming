def addComplexNumberToList(complexNumberToAdd, complexNumbersList):
    complexNumbersList.append(complexNumberToAdd)


def printComplexNumberToConsole(complexNumber):
    if complexNumber["realPart"] == 0 and complexNumber["complexPart"] == 0:
        print('0')
        return
    if complexNumber["realPart"] != 0:
        print(complexNumber["realPart"], end = '')
    if complexNumber["complexPart"] < 0:
        print(' - ', (complexNumber["complexPart"] * -1), 'i', end = '', sep = '')
    elif complexNumber["complexPart"] > 0:
        if complexNumber["realPart"] != 0:
            print(' + ', complexNumber["complexPart"], 'i', end = '', sep='')
        else:
            print(complexNumber["complexPart"], 'i', end = '', sep='')
    print()


def printComplexNumbersListToConsole(complexNumbersList):
    for complexNumber in complexNumbersList:
        printComplexNumberToConsole(complexNumber)


def populateComplexNumberList(complexNumbersList):
    complexNumber = {"realPart": 2, "complexPart": 5}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 7, "complexPart": -1}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 5, "complexPart": 3}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 0, "complexPart": 4}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 4, "complexPart": 0}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 125, "complexPart": 555222111}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": -25, "complexPart": 5}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 20, "complexPart": 50}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 25, "complexPart": -5}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 0, "complexPart": 0}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 7, "complexPart": 5}
    addComplexNumberToList(complexNumber, complexNumbersList)


def isDigit(c):
    return '0' <= c <= '9'


def setRealPart(complexNumber, realPart):
    complexNumber["realPart"] = realPart


def setComplexPart(complexNumber, complexPart):
    complexNumber["complexPart"] = complexPart


def complexNumberFromConsole():
    print("please insert the real part of your number, then hit \"ENTER\", then the complex part, or \"done\", "
          "if done :)")
    realPart = input("real part = ")
    if realPart == "done":
        return False
    complexPart = input("complex part = ")
    return newComplexNumber(realPart, complexPart)
    # consoleInput = input("please insert your complex number in the format a + bi, or \"done\", if done :)\n")
    # realPartNegative = False
    # complexPartUnitary = True
    # realPart = 0
    # complexPart = 0
    # i = 0
    # realPartDone = False
    # complexPartNegative = False
    # if consoleInput == "done":
    #     return False
    # if consoleInput[0] == '-':
    #     realPartNegative = True
    #     i = 1
    # while i < len(consoleInput):
    #     if isDigit(consoleInput[i]) and not realPartDone:
    #         realPart = realPart * 10 + int(consoleInput[i])
    #     elif consoleInput[i] == 'i' and not realPartDone:
    #         realPart = 1
    #         realPartDone = True
    #     elif consoleInput[i] == '+':
    #         realPartDone = True
    #     elif consoleInput[i] == '-':
    #         realPartDone = True
    #         complexPartNegative = True
    #     elif realPartDone and consoleInput[i] == 'i' and complexPartUnitary:
    #         complexPart = 1
    #     elif realPartDone and isDigit(consoleInput[i]):
    #         complexPart = complexPart * 10 + int(consoleInput[i])
    #         complexPartUnitary = False
    #     i += 1
    # if realPartNegative:
    #     realPart *= -1
    # if complexPartNegative:
    #     complexPart *= -1


def newComplexNumber(realPart, complexPart):
    complexNumber = {}
    setRealPart(complexNumber, int(realPart))
    setComplexPart(complexNumber, int(complexPart))
    # printComplexNumberToConsole(complexNumber)
    return complexNumber


def getRealPart(complexNumber):
    return complexNumber["realPart"]


def getComplexPart(complexNumber):
    return complexNumber["complexPart"]


def complexNumbersListFromConsole(complexNumbersList):
    complexNumber = complexNumberFromConsole()
    while complexNumber:
        addComplexNumberToList(complexNumber, complexNumbersList)
        complexNumber = complexNumberFromConsole()
    return complexNumbersList


def longestSequenceWithStrictlyIncreasingRealPart(complexNumbersList):
    """
    Return the longest sequence of complex numbers with increasing real parts.
    :param complexNumbersList: a list of complex numbers
    :return: a list containing the longest strictly increasing sequence of the complexNumbersList,
    by the real part of its components
    """
    longestSequence = []
    actualSequence = [complexNumbersList[0]]
    # print(complexNumbersList)
    i = 0
    while i < len(complexNumbersList) - 1:
        i += 1
        if getRealPart(actualSequence[-1]) < getRealPart(complexNumbersList[i]):
            actualSequence.append(complexNumbersList[i])

        else:
            if len(actualSequence) > len(longestSequence):
                longestSequence = actualSequence
            actualSequence = [complexNumbersList[i]]
    if len(actualSequence) > len(longestSequence):
        longestSequence = actualSequence
    return longestSequence


def digitsInBase10(number):
    digits = [False] * 10
    if number == 0:
        digits.insert(0, True)
        return
    if number < 0:
        number = number * -1
    while number > 0:
        digits[number % 10] = True
        number = int(number / 10)
    return digits


def areRealAndComplexPartsWithSameDigits(complexNumber):
    return digitsInBase10(getRealPart(complexNumber)) == digitsInBase10(getComplexPart(complexNumber))


def sequenceOfComplexNumbersWithSameDigitsOfRealAndComplexPart(complexNumbersList):
    """
    Print the sequence of numbers from complexNumberList of whom both real and complex part
    are written with the same digits
    :param complexNumbersList: a list of complex numbers
    :return: the sequence of the input list of complex numbers with real and complex part written with the same digits
    """
    sequence = []
    for complexNumber in complexNumbersList:
        if areRealAndComplexPartsWithSameDigits(complexNumber):
            sequence.append(complexNumber)
    return sequence


def main():
    complexNumbersList = []
    populateComplexNumberList(complexNumbersList)
    print("Welcome to Complex!")
    while True:
        userInput = input('$')
        if userInput == "read":
            # print("reading list")
            complexNumbersList = complexNumbersListFromConsole(complexNumbersList)
        elif userInput == "print":
            # print("printing list")
            printComplexNumbersListToConsole(complexNumbersList)
        elif userInput == "increasing":
            # print("printing longest sequence with strictly increasing real part")
            printComplexNumbersListToConsole(longestSequenceWithStrictlyIncreasingRealPart(complexNumbersList))
        elif userInput == "digits":
            # print("printing numbers of which real and complex parts can be written with same base 10 digits")
            printComplexNumbersListToConsole(
                sequenceOfComplexNumbersWithSameDigitsOfRealAndComplexPart(complexNumbersList))
        elif userInput == "exit":
            print("Have a nice day!")
            return
        else:
            print("Invalid command. Please insert your command again!")


main()
