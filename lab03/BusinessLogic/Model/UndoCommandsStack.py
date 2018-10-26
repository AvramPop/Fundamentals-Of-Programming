from BusinessLogic.Utils.RepositoryUtils import *


def runUndoCommand(command, expensesList):
    command = command.split()
    if command[0] == "add":
        addExpenseToList(expenseFromCommand(command), expensesList)
    elif command[0] == "remove":
        expensesList = removeExpenseFromList(expenseFromCommand(command), expensesList)
    return expensesList


def expenseFromCommand(command):
    return newExpense(int(command[1]), int(command[2]), command[3])


def addCommandsForListOfExpensesList(expensesList):
    commands = []
    for i in range(0, len(expensesList)):
        commands.append(addExpenseCommand(expensesList[i]))
    return commands


def addExpenseCommand(expense):
    return "add " + str(getDay(expense)) + " " + str(getAmount(expense)) + " " + getExpenseType(expense)


def removeExpenseCommand(expense):
    return "remove " + str(getDay(expense)) + " " + str(getAmount(expense)) + " " + getExpenseType(expense)


def undoCommands(command, expensesList):
    if command[0] == "add":
        return [removeExpenseCommand(newExpense(today, int(command[1]), command[2]))]
    elif command[0] == "insert":
        return [removeExpenseCommand(newExpense(int(command[1]), int(command[2]), command[3]))]
    elif command[0] == "remove":
        if len(command) == 2:
            if command[1].isdigit():
                return addCommandsForListOfExpensesList(expensesWithDayList(int(command[1]), expensesList))
            else:
                return addCommandsForListOfExpensesList(expensesWithTypeList(command[1], expensesList))
        else:
            return addCommandsForListOfExpensesList(expensesWithDayInInterval(int(command[1]), int(command[3]), expensesList))
    elif command[0] == "filter":
        if len(command) == 2:
            return addCommandsForListOfExpensesList(expensesWithoutExpenseTypeList(command[1], expensesList))
        else:
            if command[2] == "<":
                expensesListToAdd = expensesWithTypeWhenAmountGreaterThanList(command[1], int(command[3]) - 1, expensesList)
                expensesListToAdd.extend(expensesWithoutExpenseTypeList(command[1], expensesList))
                return addCommandsForListOfExpensesList(expensesListToAdd)
            if command[2] == ">":
                expensesListToAdd = expensesWithTypeWhenAmountSmallerThanList(command[1], int(command[3]) - 1,
                                                                              expensesList)
                expensesListToAdd.extend(expensesWithoutExpenseTypeList(command[1], expensesList))
                return addCommandsForListOfExpensesList(expensesListToAdd)
            if command[2] == "=":
                return addCommandsForListOfExpensesList(expensesWithTypeWhenAmountDifferentThanList(command[1], int(command[3]), expensesList))


def addCommandToUndoStack(command, stack, expensesList):
    undoCommandsForCommand = undoCommands(command, expensesList)
    stack.append(undoCommandsForCommand)


def undo(stack, expensesList):
    if len(stack) == 0:
        print("no command to undo")
    else:
        lastElement = stack[-1]
        for command in lastElement:
            expensesList = runUndoCommand(command, expensesList)
        del stack[-1]
    return expensesList
