def addComplexNumberToList(complexNumberToAdd, complexNumbersList):
    complexNumbersList.update({len(complexNumbersList): complexNumberToAdd})
    # complexNumbersList[len(complexNumbersList)] = complexNumberToAdd


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
    for complexNumber in complexNumbersList.values():
        printComplexNumberToConsole(complexNumber)


def populateComplexNumberList(complexNumbersList):
    complexNumber = {"realPart": 2, "complexPart": 5}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 7, "complexPart": 77}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 5, "complexPart": 3}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 0, "complexPart": 4}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 4, "complexPart": 0}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 125, "complexPart": 555222111}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": -25, "complexPart": 25}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 20, "complexPart": 50}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 1, "complexPart": -11}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 0, "complexPart": 0}
    addComplexNumberToList(complexNumber, complexNumbersList)
    complexNumber = {"realPart": 75, "complexPart": 577}
    addComplexNumberToList(complexNumber, complexNumbersList)


def isDigit(c):
    return '0' <= c <= '9'


def setRealPart(complexNumber, realPart):
    complexNumber['realPart'] = realPart


def setComplexPart(complexNumber, complexPart):
    complexNumber['complexPart'] = complexPart


def complexNumberFromConsole():
    print("please insert the real part of your number, then hit \"ENTER\", then the complex part, or \"done\", "
          "if done :)")
    realPart = input("real part = ")
    if realPart == "done":
        return False
    complexPart = input("complex part = ")
    return newComplexNumber(realPart, complexPart)


def newComplexNumber(realPart, complexPart):
    complexNumber = {}
    setRealPart(complexNumber, int(realPart))
    setComplexPart(complexNumber, int(complexPart))
    return complexNumber


def getRealPart(complexNumber):
    realPart = dict(complexNumber).get('realPart')
    return realPart


def getComplexPart(complexNumber):
    complexPart = dict(complexNumber).get('complexPart')
    return complexPart


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
    longestSequence = {}
    actualSequence = {0: complexNumbersList.get(0)}
    i = 0
    while i < len(complexNumbersList) - 1:
        i += 1
        if getRealPart(actualSequence.get(len(actualSequence) - 1)) < getRealPart(complexNumbersList.get(i)):
            addComplexNumberToList(complexNumbersList.get(i), actualSequence)
        else:
            if len(actualSequence) > len(longestSequence):
                longestSequence = actualSequence
            actualSequence = {0: complexNumbersList.get(i)}
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
    actualSequence = {}
    longestSequence = {}
    i = 0
    while i < len(complexNumbersList):
        if areRealAndComplexPartsWithSameDigits(complexNumbersList.get(i)):
            addComplexNumberToList(complexNumbersList.get(i), actualSequence)
        else:
            if len(actualSequence) > len(longestSequence):
                longestSequence = actualSequence
            actualSequence = {}
        i += 1
    if len(actualSequence) > len(longestSequence):
        longestSequence = actualSequence
    return longestSequence


def main():
    complexNumbersList = {}
    populateComplexNumberList(complexNumbersList)
    print("Welcome to Complex!")
    while True:
        userInput = input('$')
        if userInput == "read":
            complexNumbersList = complexNumbersListFromConsole(complexNumbersList)
        elif userInput == "print":
            printComplexNumbersListToConsole(complexNumbersList)
        elif userInput == "increasing":
            printComplexNumbersListToConsole(longestSequenceWithStrictlyIncreasingRealPart(complexNumbersList))
        elif userInput == "digits":
            printComplexNumbersListToConsole(
                sequenceOfComplexNumbersWithSameDigitsOfRealAndComplexPart(complexNumbersList))
        elif userInput == "exit":
            print("Have a nice day!")
            return
        else:
            print("Invalid command. Please insert your command again!")


main()
