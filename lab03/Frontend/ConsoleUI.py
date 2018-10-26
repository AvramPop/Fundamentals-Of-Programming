from BusinessLogic.Utils.PrintUtils import *


def launchUI():
    """
    Launch UI, living until user exits via a command
    """
    print("Welcome to Expi!")
    expensesList = []
    populateExpensesList(expensesList)
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
                        print(toString(expenseToAdd), "expense successfully added to the expenses list!")
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "insert":
                    if isValidInsertCommand(consoleInputWordsList):
                        expenseToAdd = newExpense(int(consoleInputWordsList[1]), int(consoleInputWordsList[2]),
                                                  consoleInputWordsList[3])
                        addExpenseToList(expenseToAdd, expensesList)
                        print(toString(expenseToAdd), "expense successfully added to the expenses list!")
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "remove":
                    if isValidRemoveCommand(consoleInputWordsList):
                        if isValidExpenseType(consoleInputWordsList[1]):
                            expensesList = expensesWithoutExpenseTypeList(consoleInputWordsList[1], expensesList)
                            print("removed expenses with type", consoleInputWordsList[1], "from list")
                        elif isValidDay(int(consoleInputWordsList[1])) and len(consoleInputWordsList) == 2:
                            expensesList = expensesWithoutDayList(int(consoleInputWordsList[1]), expensesList)
                            print("removed expenses with day", int(consoleInputWordsList[1]), "from list")
                        elif isValidDay(int(consoleInputWordsList[1])) and consoleInputWordsList[2] == "to":
                            expensesList = expensesWithoutDayInIntervalList(int(consoleInputWordsList[1]),
                                                                            int(consoleInputWordsList[3]), expensesList)
                            print("removed expenses with day", int(consoleInputWordsList[1]), "to", int(consoleInputWordsList[3]), "from list")
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "list":
                    if isValidListCommand(consoleInputWordsList):
                        if len(consoleInputWordsList) == 1:
                            print("printing list of expenses:")
                            printExpensesList(expensesList)
                        elif len(consoleInputWordsList) == 2:
                            print("printing expenses with type", consoleInputWordsList[1])
                            printExpensesWithType(consoleInputWordsList[1], expensesList)
                        else:
                            if consoleInputWordsList[2] == ">":
                                print("printing all expenses for type", consoleInputWordsList[1], "with amount",
                                      consoleInputWordsList[2], "than", consoleInputWordsList[3])
                                printExpensesWithTypeWhenAmountGreaterThan(consoleInputWordsList[1],
                                                                           int(consoleInputWordsList[3]), expensesList)
                            elif consoleInputWordsList[2] == "=":
                                print("printing all expenses for type", consoleInputWordsList[1], "with amount",
                                      "equal with", consoleInputWordsList[3])
                                printExpensesWithTypeWhenAmountEquals(consoleInputWordsList[1],
                                                                      int(consoleInputWordsList[3]), expensesList)
                            elif consoleInputWordsList[2] == "<":
                                print("printing all expenses for type", consoleInputWordsList[1], "with amount",
                                      consoleInputWordsList[2], "than", consoleInputWordsList[3])
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
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "sort":
                    if isValidSortCommand(consoleInputWordsList):
                        if consoleInputWordsList[1].isdigit():
                            printExpensesForDayInAscendingOrder(int(consoleInputWordsList[1]), expensesList)
                        else:
                            printDailyExpensesForExpenseTypeSortedAscending(consoleInputWordsList[1], expensesList)
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "filter":
                    if isValidFilterCommand(consoleInputWordsList):
                        if len(consoleInputWordsList) == 2:
                            print("all expenses without type", consoleInputWordsList[1], "removed from the list")
                            expensesList = expensesWithTypeList(consoleInputWordsList[1], expensesList)
                        else:
                            if consoleInputWordsList[2] == ">":
                                print("all expenses with type", consoleInputWordsList[1], "and amount smaller than", consoleInputWordsList[3], "removed from list")
                                expensesList = expensesWithTypeWhenAmountGreaterThanList(consoleInputWordsList[1],
                                                                                         int(consoleInputWordsList[3]),
                                                                                         expensesList)
                            elif consoleInputWordsList[2] == "=":
                                print("all expenses with type", consoleInputWordsList[1], "and amount different than",
                                      consoleInputWordsList[3], "removed from list")
                                expensesList = expensesWithoutBothExpenseTypeAndAmount(consoleInputWordsList[1],
                                                                                       int(consoleInputWordsList[3]),
                                                                                       expensesList)
                            elif consoleInputWordsList[2] == "<":
                                print("all expenses with type", consoleInputWordsList[1], "and amount greater than",
                                      consoleInputWordsList[3], "removed from list")
                                expensesList = expensesWithTypeWhenAmountSmallerThanList(consoleInputWordsList[1],
                                                                                         int(consoleInputWordsList[3]),
                                                                                         expensesList)
                    else:
                        print("wrong input. try again!")
                elif consoleInputWordsList[0] == "exit":
                    return
            else:
                print("wrong input. try again!")
        else:
            print("wrong input. try again!")
