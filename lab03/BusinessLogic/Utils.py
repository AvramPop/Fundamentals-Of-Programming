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
