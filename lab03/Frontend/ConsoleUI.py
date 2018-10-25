from BusinessLogic.Utils import *


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
                        expenseToAdd = newExpense(int(consoleInputWordsList[1]), int(consoleInputWordsList[2]),
                                                  consoleInputWordsList[3])
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
                            expensesList = removeExpensesForDaysInterval(int(consoleInputWordsList[1]),
                                                                         int(consoleInputWordsList[3]), expensesList)
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
                                printExpensesWithTypeWhenAmountGreaterThan(consoleInputWordsList[1],
                                                                           int(consoleInputWordsList[3]), expensesList)
                            elif consoleInputWordsList[2] == "=":
                                printExpensesWithTypeWhenAmountEquals(consoleInputWordsList[1],
                                                                      int(consoleInputWordsList[3]), expensesList)
                            elif consoleInputWordsList[2] == "<":
                                printExpensesWithTypeWhenAmountSmallerThan(consoleInputWordsList[1],
                                                                           int(consoleInputWordsList[3]), expensesList)
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "sum":
                    if isValidSumCommand(consoleInputWordsList):
                        printSumOfExpensesWithExpenseType(consoleInputWordsList[1], expensesList)
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "max":
                    if isValidMaxCommand(consoleInputWordsList):
                        # TODO ask someone about the assignment
                        printDayWithMaximumExpenses(expensesList)
                        print("max")
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "sort":
                    if isValidSortCommand(consoleInputWordsList):
                        printExpensesForDayInAscendingOrder(int(consoleInputWordsList[1]), expensesList)
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
