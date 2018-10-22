import datetime

expenseTypeEnum = ("housekeeping", "food", "transport", " clothing", "internet", "others")
commandsEnum = ("add", "insert", "remove", "remove", "list", "sum", "max", "sort", "filter", "undo", "exit")
now = datetime.datetime.now()


def test():
    newExpenseTest()
    isValidAddCommandTest()
    isValidInsertCommandTest()
    isValidRemoveCommandTest()
    isValidListCommandTest()
    removeExpensesForDayTest()
    removeExpensesForExpenseTypeTest()
    print("testing done successfully")


def newExpenseTest():
    # TODO check if exception is raised
    assert newExpense(25, 600, 'food') == {"day": 25, "amount": 600, "expenseType": "food"}


def removeExpensesForExpenseType(expenseType, expensesList):
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            expensesList.remove(expense)


def removeExpensesForDay(day, expensesList):
    # TODO write doc
    for expense in expensesList:
        if getDay(expense) == day:
            expensesList.remove(expense)


def removeExpensesForDaysInterval(startDay, endDay, expensesList):
    # TODO test
    for day in range(startDay, endDay + 1):
        removeExpensesForDay(day, expensesList)


def removeExpensesForExpenseTypeTest():  # TODO check clothing error
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "internet"), expensesList)
    addExpenseToList(newExpense(30, 600, "transport"), expensesList)
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    removeExpensesForExpenseType("food", expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(20, 600, "internet"), expensesListCorrect)
    addExpenseToList(newExpense(30, 600, "transport"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def removeExpensesForDayTest():
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "food"), expensesList)
    addExpenseToList(newExpense(30, 600, "food"), expensesList)
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    removeExpensesForDay(25, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(20, 600, "food"), expensesListCorrect)
    addExpenseToList(newExpense(30, 600, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def toString(expense):
    return "day:" + str(getDay(expense)) + " sum:" + str(getAmount(expense)) + " type:" + getExpenseType(expense)


def printExpense(expense):
    print(expense.toString())


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


def isValidDay(day):  # TODO test
    # TODO write doc
    return type(day) == int and 0 <= day <= 30


def isValidAmount(amount):  # TODO test
    # TODO write doc
    return type(amount) == int and amount > 0


def isValidExpenseType(expenseType):  # TODO test
    # TODO write doc
    return expenseType in expenseTypeEnum


def newExpense(day, amount, expenseType):
    # TODO handle exceptions
    # TODO write doc
    expense = {}
    if isValidDay(day):
        setDay(expense, day)
    else:
        raise TypeError
    if isValidAmount(amount):
        setAmount(expense, amount)
    else:
        raise TypeError
    if isValidExpenseType(expenseType):
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
    return isValidAmount(int(addCommand[1])) and \
           isValidExpenseType(addCommand[2])


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
    return isValidDay(int(insertCommand[1])) and \
           isValidAmount(int(insertCommand[2])) and \
           isValidExpenseType(insertCommand[3])


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
    # TODO check second day be greater than start day
    if removeCommand[0] != 'remove':
        return False
    if len(removeCommand) != 2 and len(removeCommand) != 4:
        return False
    elif len(removeCommand) == 4:
        if not removeCommand[1].isdigit() or not removeCommand[3].isdigit():
            return False
    elif len(removeCommand) == 2:
        if removeCommand[1].isdigit():
            if isValidDay(int(removeCommand[1])):
                return True
            else:
                return False
        else:
            return isValidExpenseType(removeCommand[1])

    return isValidDay(int(removeCommand[1])) and removeCommand[2] == "to" and isValidDay(int(removeCommand[3]))


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
        if isValidExpenseType(listCommand[1]):
            return True
        else:
            return False
    if len(listCommand) != 4:
        return False
    if not listCommand[3].isdigit():
        return False
    return isValidExpenseType(listCommand[1]) and \
           (listCommand[2] == "<" or listCommand[2] == "=" or listCommand[2] == ">") and \
           isValidAmount(int(listCommand[3]))


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
    return isValidExpenseType(sumCommand[1])


def isValidMaxCommand(maxCommand):  # TODO test
    # TODO write doc
    if maxCommand[0] != 'max':
        return False
    if len(maxCommand) == 1 or len(maxCommand) > 2:
        return False
    return isValidDay(maxCommand[1])


def isValidSortCommand(sortCommand):  # TODO test
    # TODO write doc
    if sortCommand[0] != 'sort':
        return False
    if len(sortCommand) == 1 or len(sortCommand) > 2:
        return False
    return isValidDay(sortCommand[1]) or \
           isValidExpenseType(sortCommand[1])


def isValidFilterCommand(filterCommand):  # TODO test
    # TODO write doc
    if filterCommand[0] != 'filter':
        return False
    if len(filterCommand) != 2 and len(filterCommand) != 4:
        return False
    return isValidExpenseType(filterCommand[1]) or \
           (isValidExpenseType(filterCommand[1]) and
            (filterCommand[2] == "<" or filterCommand[2] == "=" or filterCommand[2] == ">") and
            isValidAmount(filterCommand[3]))


def launchUI():
    """
    Launch UI, living until user exits via a command
    """
    print("Welcome to Expi!")
    expensesList = []
    # TODO populate list of expenses
    while True:
        consoleInput = input(">")
        consoleInputWordsList = consoleInput.split()
        if isCommand(consoleInputWordsList[0]):
            if consoleInputWordsList[0] == "add":
                if isValidAddCommand(consoleInputWordsList): # TODO fix case when day is 31
                    expenseToAdd = newExpense(now.day, int(consoleInputWordsList[1]), consoleInputWordsList[2])
                    addExpenseToList(expenseToAdd, expensesList)
                    print("\"", toString(expenseToAdd), "\" expense successfully added to the expenses list!")
                else:
                    print("wrong input. try again!")
            elif consoleInputWordsList[0] == "insert":
                if isValidInsertCommand(consoleInputWordsList):
                    expenseToAdd = newExpense(int(consoleInputWordsList[1]), int(consoleInputWordsList[2]), consoleInputWordsList[3])
                    addExpenseToList(expenseToAdd, expensesList)
                    print("\"", toString(expenseToAdd), "\" expense successfully added to the expenses list!")
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
