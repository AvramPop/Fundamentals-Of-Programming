import datetime

expenseTypeEnum = ("housekeeping", "food", "transport", "clothing", "internet", "others")
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
    """
    Return updated expenses list without every expense from expensesList that has the expense type attribute expenseType
    :param expenseType: the expense type with which expenses should be popped
    :param expensesList: a list of expenses
    :return: the updated list, without the elements with expenseType attribute set to expenseType
    """
    updatedExpensesList = [expense for expense in expensesList if getExpenseType(expense) != expenseType]
    return updatedExpensesList


def removeExpensesForDay(day, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the day attribute set to day
    :param day: the day with which expenses should be popped
    :param expensesList: a list of expenses
    :return: the updated list, without the elements with day attribute set to day
    """
    updatedExpensesList = [expense for expense in expensesList if getDay(expense) != day]
    return updatedExpensesList


def removeExpensesForDaysInterval(startDay, endDay, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the day attribute set to any day in the closed interval [startDay, endDay]
    :param startDay: the first day of the closed interval of days with which expenses should be popped from the list
    :param endDay: the last day of the closed interval of days with which expenses should be popped from the list
    :param expensesList: a list of expenses
    :return: the updated list, without the elements with day attribute in [startDay, endDay]
    """
    # TODO test
    for day in range(startDay, endDay + 1):
        expensesList = removeExpensesForDay(day, expensesList)
    return expensesList


def removeExpensesForExpenseTypeTest():
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "clothing"), expensesList)
    addExpenseToList(newExpense(30, 600, "transport"), expensesList)
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    expensesList = removeExpensesForExpenseType("food", expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(20, 600, "clothing"), expensesListCorrect)
    addExpenseToList(newExpense(30, 600, "transport"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def removeExpensesForDayTest():
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "food"), expensesList)
    addExpenseToList(newExpense(30, 600, "food"), expensesList)
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    expensesList = removeExpensesForDay(25, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(20, 600, "food"), expensesListCorrect)
    addExpenseToList(newExpense(30, 600, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def toString(expense):
    return "day:" + str(getDay(expense)) + " sum:" + str(getAmount(expense)) + " type:" + getExpenseType(expense)


def printExpense(expense):
    print(toString(expense))


def isCommand(command):  # TODO test
    """
    Check whether the command is a valid one (one of: "add", "insert", "remove", "remove", "list", "sum", "max", "sort", "filter", "undo", "exit")
    :param command: the command to be checked
    :return: True if command is valid, False otherwise
    """
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
    """
    Checks whether day is a valid day (it is a natural number between 1 and 30)
    :param day: the day to be checked
    :return: True if day is valid, False otherwise
    """
    return type(day) == int and 1 <= day <= 30


def isValidAmount(amount):  # TODO test
    """
    Checks whether amount is a valid amount (it is a natural number)
    :param amount: the amount to be checked
    :return: True if amount is valid, False otherwise
    """
    return type(amount) == int and amount > 0


def isValidExpenseType(expenseType):  # TODO test
    """
    Checks whether expenseType is a valid expenseType (one of: housekeeping, food, transport, clothing, internet, others)
    :param expenseType: the expenseType to be checked
    :return: True if expenseType is valid, False otherwise
    """
    return expenseType in expenseTypeEnum


def newExpense(day, amount, expenseType):
    """
    Return a new expense in the format of a dictionary having 'day', 'amount' and 'expenseType' as keys, with the values set accordingly to the function;s params
    :param day: the day value to be set for the new expense
    :param amount: the amount value to be set for the new expense
    :param expenseType: the expenseType value to be set for the new expense
    :return: the dictionary representing the new expense
    :raises TypeError: if one of the params are not rightly formatted
    """
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
    # TODO test
    """
    Add expense to expenseList
    :param expense: the expense to add
    :param expensesList: the list to which expense should be added
    """
    expensesList.append(expense)


def isValidAddCommand(addCommand):
    """
    Check whether addCommand is a valid add command (of format: add <sum> <category>)
    :param addCommand: the command to be checked
    :return: True if addCommand is a valid add command, False otherwise
    """
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
    """
    Check whether insertCommand is a valid insert command (of format: insert <day> <sum> <category>)
    :param insertCommand: the command to be checked
    :return: True if insertCommand is a valid insert command, False otherwise
    """
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
    """
    Check whether removeCommand is a valid remove command (of format: remove <day>, or: remove <start day> to <end day>, or remove <category>)
    :param removeCommand: the command to be checked
    :return: True if removeCommand is a valid remove command, False otherwise
    """
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
    if int(removeCommand[3]) <= int(removeCommand[1]):
        return False
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
    """
    Check whether listCommand is a valid list command (of format: list, or: list <category>, or list <category> [ < | = | > ] <value>)
    :param listCommand: the command to be checked
    :return: True if listCommand is a valid list command, False otherwise
    """
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
    """
    Check whether sumCommand is a valid sum command (of format: sum <category>)
    :param sumCommand: the command to be checked
    :return: True if sumCommand is a valid sum command, False otherwise
    """
    if sumCommand[0] != 'sum':
        return False
    if len(sumCommand) == 1 or len(sumCommand) > 2:
        return False
    return isValidExpenseType(sumCommand[1])


def isValidMaxCommand(maxCommand):  # TODO test
    """
    Check whether maxCommand is a valid max command (of format: max <day>)
    :param maxCommand: the command to be checked
    :return: True if maxCommand is a valid max command, False otherwise
    """
    if maxCommand[0] != 'max':
        return False
    if len(maxCommand) == 1 or len(maxCommand) > 2:
        return False
    return isValidDay(maxCommand[1])


def isValidSortCommand(sortCommand):  # TODO test
    """
    Check whether sortCommand is a valid sort command (of format: sort <day>, or: sort <category>)
    :param sortCommand: the command to be checked
    :return: True if sortCommand is a valid sort command, False otherwise
    """
    if sortCommand[0] != 'sort':
        return False
    if len(sortCommand) == 1 or len(sortCommand) > 2:
        return False
    return isValidDay(sortCommand[1]) or \
           isValidExpenseType(sortCommand[1])


def isValidFilterCommand(filterCommand):  # TODO test
    """
    Check whether filterCommand is a valid filter command (of format: filter <category>, or: filter <category> [ < | = | > ] <value>)
    :param filterCommand: the command to be checked
    :return: True if filterCommand is a valid filter command, False otherwise
    """
    if filterCommand[0] != 'filter':
        return False
    if len(filterCommand) != 2 and len(filterCommand) != 4:
        return False
    return isValidExpenseType(filterCommand[1]) or \
           (isValidExpenseType(filterCommand[1]) and
            (filterCommand[2] == "<" or filterCommand[2] == "=" or filterCommand[2] == ">") and
            isValidAmount(filterCommand[3]))


def populateListOfExpenses(expensesList):
    addExpenseToList(newExpense(2, 25, "food"), expensesList)
    addExpenseToList(newExpense(20, 150, "internet"), expensesList)
    addExpenseToList(newExpense(1, 40, "others"), expensesList)
    addExpenseToList(newExpense(30, 2, "transport"), expensesList)
    addExpenseToList(newExpense(14, 1000, "food"), expensesList)
    addExpenseToList(newExpense(15, 29, "housekeeping"), expensesList)
    addExpenseToList(newExpense(16, 40, "food"), expensesList)
    addExpenseToList(newExpense(17, 250, "transport"), expensesList)
    addExpenseToList(newExpense(24, 2500, "internet"), expensesList)
    addExpenseToList(newExpense(29, 25, "others"), expensesList)
    addExpenseToList(newExpense(30, 250, "food"), expensesList)
    addExpenseToList(newExpense(2, 250, "food"), expensesList)


def printExpensesList(expensesList):
    if len(expensesList) == 0:
        print("expenses list is empty!")
    else:
        for expense in expensesList:
            printExpense(expense)


def printExpensesWithType(expenseType, expensesList):
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            printExpense(expense)


def printExpensesWithTypeWhenAmountGreaterThan(expenseType, amount, expensesList):
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) > amount:
                printExpense(expense)


def printExpensesWithTypeWhenAmountSmallerThan(expenseType, amount, expensesList):
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) < amount:
                printExpense(expense)


def printExpensesWithTypeWhenAmountEquals(expenseType, amount, expensesList):
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) == amount:
                printExpense(expense)


def launchUI():
    """
    Launch UI, living until user exits via a command
    """
    print("Welcome to Expi!")
    expensesList = []
    populateListOfExpenses(expensesList)
    # printExpensesList(expensesList)
    while True:
        consoleInput = input(">")
        consoleInputWordsList = consoleInput.split()
        if consoleInputWordsList:
            if isCommand(consoleInputWordsList[0]):
                if consoleInputWordsList[0] == "add":
                    if isValidAddCommand(consoleInputWordsList):
                        today = now.day if now.day <= 30 else 1
                        expenseToAdd = newExpense(today, int(consoleInputWordsList[1]), consoleInputWordsList[2])
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
                        if isValidExpenseType(consoleInputWordsList[1]):
                            expensesList = removeExpensesForExpenseType(consoleInputWordsList[1], expensesList)
                        elif isValidDay(int(consoleInputWordsList[1])) and len(consoleInputWordsList) == 2:
                            expensesList = removeExpensesForDay(int(consoleInputWordsList[1]), expensesList)
                        elif isValidDay(int(consoleInputWordsList[1])) and consoleInputWordsList[2] == "to":
                            expensesList = removeExpensesForDaysInterval(int(consoleInputWordsList[1]), int(consoleInputWordsList[3]), expensesList)
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "list":
                    if isValidListCommand(consoleInputWordsList):
                        if len(consoleInputWordsList) == 1:
                            printExpensesList(expensesList)
                        elif len(consoleInputWordsList) == 2:
                            printExpensesWithType(consoleInputWordsList[1], expensesList)
                        else:
                            if consoleInputWordsList[2] == ">":
                                printExpensesWithTypeWhenAmountGreaterThan(consoleInputWordsList[1], int(consoleInputWordsList[3]), expensesList)
                            elif consoleInputWordsList[2] == "=":
                                printExpensesWithTypeWhenAmountEquals(consoleInputWordsList[1], int(consoleInputWordsList[3]), expensesList)
                            elif consoleInputWordsList[2] == "<":
                                printExpensesWithTypeWhenAmountSmallerThan(consoleInputWordsList[1], int(consoleInputWordsList[3]), expensesList)
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
        else:
            print("wrong input. try again!")


def main():
    launchUI()
    print("have a nice day!")


test()
main()
