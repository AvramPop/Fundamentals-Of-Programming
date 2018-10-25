from Validation.CommandsValidation import *


def removeExpensesForExpenseType(expenseType, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the expense type attribute expenseType
    :param expenseType: (string) the expense type with which expenses should be popped
    :param expensesList: (list) a list of expenses
    :return: the updated list, without the elements with expenseType attribute set to expenseType
    """
    updatedExpensesList = [expense for expense in expensesList if getExpenseType(expense) != expenseType]
    return updatedExpensesList


def removeExpensesForDay(day, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the day attribute set to day
    :param day: (int) the day with which expenses should be popped
    :param expensesList: (list) a list of expenses
    :return: the updated list, without the elements with day attribute set to day
    """
    updatedExpensesList = [expense for expense in expensesList if getDay(expense) != day]
    return updatedExpensesList


def removeExpensesForDaysInterval(startDay, endDay, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the day attribute set to any day in the closed interval [startDay, endDay]
    :param startDay: (int) the first day of the closed interval of days with which expenses should be popped from the list
    :param endDay: (int) the last day of the closed interval of days with which expenses should be popped from the list
    :param expensesList: (list) a list of expenses
    :return: the updated list, without the elements with day attribute in [startDay, endDay]
    """
    for day in range(startDay, endDay + 1):
        expensesList = removeExpensesForDay(day, expensesList)
    return expensesList


def toString(expense):
    return "day:" + str(getDay(expense)) + " sum:" + str(getAmount(expense)) + " type:" + getExpenseType(expense)


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


def newExpense(day, amount, expenseType):
    """
    Return a new expense in the format of a dictionary having 'day', 'amount' and 'expenseType' as keys, with the values set accordingly to the function;s params
    :param day: (int) the day value to be set for the new expense, 1 <= day <= 30
    :param amount: (int) the amount value to be set for the new expense, 0 < amount
    :param expenseType: (string) the expenseType value to be set for the new expense (one of: housekeeping, food, transport, clothing, internet, others)
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
    """
    Add expense to expenseList
    :param expense: (dictionary) the expense to add
    :param expensesList: (list) the list to which expense should be added
    """
    expensesList.append(expense)
