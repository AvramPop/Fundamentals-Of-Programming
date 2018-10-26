from Validation.CommandsValidation import *


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


