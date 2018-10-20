from datetime import date

expenseTypeEnum = ("housekeeping", "food", "transport", " clothing", "internet", "others")
commandsEnum = ("add", "insert", "remove", "remove", "list", "sum", "max", "sort", "filter", "undo", "exit")


def test():
    newExpenseTest()
    isValidAddCommandTest()
    isValidInsertCommandTest()
    isValidRemoveCommandTest()
    isValidListCommandTest()
    print("testing done successfully")


def newExpenseTest():
    # TODO check if exception is raised
    assert newExpense(25, 600, 'food') == {"day": 25, "amount": 600, "expenseType": "food"}


def printExpense(expense):
    print("day:", getDay(expense), " sum:", getAmount(expense), " type:", getExpenseType(expense))


def isCommand(command):  # TODO test
    # TODO write doc
    return command in commandsEnum


def setDay(expense, day):
    expense["day"] = day


def setAmount(expense, amount):
    expense["amount"] = amount


def setExpenseType(expense, expenseType):
    expense["expenseType"] = expenseType


def getDay(expense):
    return expense.get("day")


def getAmount(expense):
    return expense.get("amount")


def getExpenseType(expense):
    return expense.get("expenseType")


def isDay(day):  # TODO test
    # TODO write doc
    return type(day) == int and 0 <= day <= 30


def isAmount(amount):  # TODO test
    # TODO write doc
    return type(amount) == int and amount > 0


def isExpenseType(expenseType):  # TODO test
    # TODO write doc
    return expenseType in expenseTypeEnum


def newExpense(day, amount, expenseType):
    # TODO write doc
    expense = {}
    if isDay(day):
        setDay(expense, day)
    else:
        raise TypeError
    if isAmount(amount):
        setAmount(expense, amount)
    else:
        raise TypeError
    if isExpenseType(expenseType):
        setExpenseType(expense, expenseType)
    else:
        raise TypeError
    return expense


def addExpenseToList(expense, expensesList):
    # TODO write doc
    expensesList.append(expense)


def isValidAddCommand(addCommand):
    # TODO write doc
    if addCommand[0] != 'add':
        return False
    if len(addCommand) != 3:
        return False
    if not addCommand[1].isdigit():
        return False
    return isAmount(int(addCommand[1])) and \
           isExpenseType(addCommand[2])


def isValidAddCommandTest():
    assert isValidAddCommand(['add']) is False
    assert isValidAddCommand(['asfd']) is False
    assert isValidAddCommand(['add', '-5']) is False
    assert isValidAddCommand(['add', 'sadsd', 'food']) is False
    assert isValidAddCommand(['add', '-5', 'food']) is False
    assert isValidAddCommand(['add', '5.5', 'food']) is False
    assert isValidAddCommand(['add', '5', 'adsda']) is False
    assert isValidAddCommand(['add', '5', '5']) is False
    assert isValidAddCommand(['add', '-5', 'sdadsa']) is False
    assert isValidAddCommand(['add', '-5', 'das', 'das']) is False
    assert isValidAddCommand(['dsa', '5', 'food']) is False
    assert isValidAddCommand(['add', '5', 'food']) is True


def isValidInsertCommand(insertCommand):
    # TODO write doc
    if insertCommand[0] != 'insert':
        return False
    if len(insertCommand) != 4:
        return False
    if not insertCommand[1].isdigit():
        return False
    if not insertCommand[2].isdigit():
        return False
    return isDay(int(insertCommand[1])) and \
           isAmount(int(insertCommand[2])) and \
           isExpenseType(insertCommand[3])


def isValidInsertCommandTest():
    assert isValidInsertCommand(['insert']) is False
    assert isValidInsertCommand(['asfd']) is False
    assert isValidInsertCommand(['insert', '-5']) is False
    assert isValidInsertCommand(['insert', 'sadsd', 'food']) is False
    assert isValidInsertCommand(['insert', 'sadsd', 'food', 'sadsd', 'food']) is False
    assert isValidInsertCommand(['insert', '-5', '100', 'food']) is False
    assert isValidInsertCommand(['insert', '5.5', '100', 'food']) is False
    assert isValidInsertCommand(['insert', 'sad', '100', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '-100', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '100.1', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '-saddsa', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '100', 'asd']) is False
    assert isValidInsertCommand(['insert', '5', '100', '55']) is False
    assert isValidInsertCommand(['sda', '5', '100', 'food']) is False
    assert isValidInsertCommand(['insert', '5', '100', 'food']) is True


def isValidRemoveCommand(removeCommand):
    # TODO write doc
    if removeCommand[0] != 'remove':
        return False
    if len(removeCommand) != 2 and len(removeCommand) != 4:
        return False
    elif len(removeCommand) == 4:
        if not removeCommand[1].isdigit() or not removeCommand[3].isdigit():
            return False
    elif len(removeCommand) == 2:
        if removeCommand[1].isdigit():
            if isDay(int(removeCommand[1])):
                return True
            else:
                return False
        else:
            return isExpenseType(removeCommand[1])

    return isDay(int(removeCommand[1])) and removeCommand[2] == "to" and isDay(int(removeCommand[3]))


def isValidRemoveCommandTest():
    assert isValidRemoveCommand(['remove']) is False
    assert isValidRemoveCommand(['asd']) is False
    assert isValidRemoveCommand(['remove', 'sadasasd']) is False
    assert isValidRemoveCommand(['remove', '4.5']) is False
    assert isValidRemoveCommand(['remove', '-4']) is False
    assert isValidRemoveCommand(['remove', '4', 'ds']) is False
    assert isValidRemoveCommand(['remove', '4', 'to', '-5']) is False
    assert isValidRemoveCommand(['remove', '4', 'to', 'food']) is False
    assert isValidRemoveCommand(['remove', '-4', 'to', '5']) is False
    assert isValidRemoveCommand(['remove', '4', 'to', '5.5']) is False
    assert isValidRemoveCommand(['remove', '4.5', 'to', '5']) is False
    assert isValidRemoveCommand(['remove', '4', 'ton', '5']) is False
    assert isValidRemoveCommand(['remove', '4', '5', '-5']) is False
    assert isValidRemoveCommand(['remove', 'food', '55']) is False
    assert isValidRemoveCommand(['remove', 'foode']) is False
    assert isValidRemoveCommand(['remove', '6']) is True
    assert isValidRemoveCommand(['remove', '6', 'to', '9']) is True
    assert isValidRemoveCommand(['remove', 'food']) is True


def isValidListCommand(listCommand):
    # TODO write doc
    if listCommand[0] != 'list':
        return False
    if len(listCommand) == 1:
        return True
    if len(listCommand) == 2:
        if isExpenseType(listCommand[1]):
            return True
        else:
            return False
    if len(listCommand) != 4:
        return False
    print(isExpenseType(listCommand[1]))
    print((listCommand[2] == "<" or listCommand[2] == "=" or listCommand[2] == ">"))
    # print(isAmount(int(listCommand[3])))
    print()
    if not listCommand[3].isdigit():
        return False
    return isExpenseType(listCommand[1]) and \
            (listCommand[2] == "<" or listCommand[2] == "=" or listCommand[2] == ">") and \
            isAmount(int(listCommand[3]))


def isValidListCommandTest():
    assert isValidListCommand(['fads', 'food', '>', '5']) is False
    assert isValidListCommand(['fads']) is False
    assert isValidListCommand(['list', 'foodss', '>', '5']) is False
    assert isValidListCommand(['list', '6', '>', '5']) is False
    assert isValidListCommand(['list', 'food', '!', '5']) is False
    assert isValidListCommand(['list', 'food', '55', '5']) is False
    assert isValidListCommand(['list', 'food', '>', 'sad']) is False
    assert isValidListCommand(['list', 'food', '>', '5.5']) is False
    assert isValidListCommand(['list', 'food', '>', '-55']) is False
    assert isValidListCommand(['list', 'internet', '>', 'sad']) is False
    assert isValidListCommand(['list']) is True
    assert isValidListCommand(['list', 'food']) is True
    assert isValidListCommand(['list', 'food', '>', '5']) is True


def isValidSumCommand(sumCommand):  # TODO test
    # TODO write doc
    if sumCommand[0] != 'sum':
        return False
    if len(sumCommand) == 1 or len(sumCommand) > 2:
        return False
    return isExpenseType(sumCommand[1])


def isValidMaxCommand(maxCommand):  # TODO test
    # TODO write doc
    if maxCommand[0] != 'max':
        return False
    if len(maxCommand) == 1 or len(maxCommand) > 2:
        return False
    return isDay(maxCommand[1])


def isValidSortCommand(sortCommand):  # TODO test
    # TODO write doc
    if sortCommand[0] != 'sort':
        return False
    if len(sortCommand) == 1 or len(sortCommand) > 2:
        return False
    return isDay(sortCommand[1]) or \
           isExpenseType(sortCommand[1])


def isValidFilterCommand(filterCommand):  # TODO test
    # TODO write doc
    if filterCommand[0] != 'filter':
        return False
    if len(filterCommand) != 2 and len(filterCommand) != 4:
        return False
    return isExpenseType(filterCommand[1]) or \
           (isExpenseType(filterCommand[1]) and
            (filterCommand[2] == "<" or filterCommand[2] == "=" or filterCommand[2] == ">") and
            isAmount(filterCommand[3]))


def launchUI():
    """
    Launch UI, living until user exits via a command
    """
    print("Welcome to Expi!")
    expensesList = []
    expense = newExpense(2, 5, "food")
    printExpense(expense)
    while True:
        consoleInput = input(">")
        consoleInputWordsList = consoleInput.split()
        if isCommand(consoleInputWordsList[0]):
            if consoleInputWordsList[0] == "add":
                if isValidAddCommand(consoleInputWordsList):
                    addExpenseToList(newExpense(date.day, consoleInputWordsList[1], consoleInputWordsList[1]), expensesList)
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "insert":
                if isValidInsertCommand(consoleInputWordsList):
                    print("insert")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "remove":
                if isValidRemoveCommand(consoleInputWordsList):
                    print("remove")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "list":
                if isValidListCommand(consoleInputWordsList):
                    print("list")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "sum":
                if isValidSumCommand(consoleInputWordsList):
                    print("sum")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "max":
                if isValidMaxCommand(consoleInputWordsList):
                    print("max")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "sort":
                if isValidSortCommand(consoleInputWordsList):
                    print("sort")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "filter":
                if isValidFilterCommand(consoleInputWordsList):
                    print("filter")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "exit":
                return
        else:
            print("wrong input. try again!")


def main():
    launchUI()
    print("have a nice day!")


test()
main()
