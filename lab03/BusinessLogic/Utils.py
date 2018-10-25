from BusinessLogic.Expense import *


def printExpense(expense):
    print(toString(expense))


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


def expensesWithTypeList(expenseType, expensesList):
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountGreaterThanList(expenseType, amount, expensesList):
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) > amount:
                expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountSmallerThanList(expenseType, amount, expensesList):
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) < amount:
                expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountEqualsList(expenseType, amount, expensesList):
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) == amount:
                expensesWithType.append(expense)
    return expensesWithType


def printExpensesWithType(expenseType, expensesList):
    printExpensesList(expensesWithTypeList(expenseType, expensesList))


def printExpensesWithTypeWhenAmountGreaterThan(expenseType, amount, expensesList):
    printExpensesList(expensesWithTypeWhenAmountGreaterThanList(expenseType, amount, expensesList))


def printExpensesWithTypeWhenAmountSmallerThan(expenseType, amount, expensesList):
    printExpensesList(expensesWithTypeWhenAmountSmallerThanList(expenseType, amount, expensesList))


def printExpensesWithTypeWhenAmountEquals(expenseType, amount, expensesList):
    printExpensesList(expensesWithTypeWhenAmountEqualsList(expenseType, amount, expensesList))


def printSumOfExpensesWithExpenseType(expenseType, expensesList):
    sumOfExpensesWithType = 0
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            sumOfExpensesWithType += getAmount(expense)
    print("Sum of all expenses for type", expenseType, "=", sumOfExpensesWithType)


def printDayWithMaximumExpenses(expensesList):
    expensesByDay = [0] * 31
    for expense in expensesList:
        expensesByDay[getDay(expense)] += getAmount(expense)
    maximumExpense = -1
    maxDay = -1
    for i in range(1, 31):
        if expensesByDay[i] > maximumExpense:
            maximumExpense = expensesByDay[i]
            maxDay = i
    print("The day with the maximum expenses is", maxDay)


def sortExpensesList(expensesForDay):
    for i in range(0, len(expensesForDay) - 1):
        for j in range(i + 1, len(expensesForDay)):
            if getAmount(expensesForDay[i]) > getAmount(expensesForDay[j]):
                expensesForDay[i], expensesForDay[j] = expensesForDay[j], expensesForDay[i]
    return expensesForDay


def printExpensesForDayInAscendingOrder(day, expensesList):
    printExpensesList(sortExpensesList(expensesForDayList(day, expensesList)))


def expensesForDayList(day, expensesList):
    expensesForDay = []
    for expense in expensesList:
        if getDay(expense) == day:
            expensesForDay.append(expense)
    return expensesForDay

