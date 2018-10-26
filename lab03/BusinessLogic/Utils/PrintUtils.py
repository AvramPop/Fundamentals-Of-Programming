from BusinessLogic.Utils.RepositoryUtils import *


def printExpense(expense):
    print(toString(expense))


def printExpensesList(expensesList):
    if len(expensesList) == 0:
        print("expenses list is empty!")
    else:
        for expense in expensesList:
            printExpense(expense)
        print()


def printExpensesWithType(expenseType, expensesList):
    printExpensesList(expensesWithTypeList(expenseType, expensesList))


def printExpensesWithTypeWhenAmountGreaterThan(expenseType, amount, expensesList):
    printExpensesList(expensesWithTypeWhenAmountGreaterThanList(expenseType, amount, expensesList))


def printExpensesWithTypeWhenAmountSmallerThan(expenseType, amount, expensesList):
    printExpensesList(expensesWithTypeWhenAmountSmallerThanList(expenseType, amount, expensesList))


def printExpensesWithTypeWhenAmountEquals(expenseType, amount, expensesList):
    printExpensesList(expensesWithTypeWhenAmountEqualsList(expenseType, amount, expensesList))


def printExpensesForDayInAscendingOrder(day, expensesList):
    printExpensesList(sortExpensesList(expensesWithDayList(day, expensesList)))


def printSumOfExpensesWithExpenseType(expenseType, expensesList):
    print("Sum of all expenses for type", expenseType, "=", sumOfExpensesWithExpenseType(expenseType, expensesList))


def printDayWithMaximumExpenses(expensesList):
    if len(expensesList) == 0:
        print("expenses list is empty!")
    else:
        print("The day with the maximum expenses is", dayWithMaximumExpenses(expensesList))


def printDailyExpensesForExpenseTypeSortedAscending(expenseType, expensesList):
    if len(expensesList) == 0:
        print("expenses list is empty!")
    else:
        dailyExpensesForExpensesTypeSortedAscending = dailyExpensesForExpensesTypeSortedAscendingDictionary(expenseType, expensesList)
        for i in range(1, 31):
            dailyExpensesListTemp = dailyExpensesForExpensesTypeSortedAscending.get(str(i))
            if len(dailyExpensesListTemp) > 0:
                printExpensesList(dailyExpensesListTemp)
