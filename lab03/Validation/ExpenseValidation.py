from Constants import *


def isValidDay(day):
    """
    Checks whether day is a valid day (it is a natural number between 1 and 30)
    :param day: (int) the day to be checked
    :return: True if day is valid, False otherwise
    """
    return type(day) == int and 1 <= day <= 30


def isValidAmount(amount):
    """
    Checks whether amount is a valid amount (it is a natural number)
    :param amount: (int) the amount to be checked
    :return: True if amount is valid, False otherwise
    """
    return type(amount) == int and amount > 0


def isValidExpenseType(expenseType):
    """
    Checks whether expenseType is a valid expenseType (one of: housekeeping, food, transport, clothing, internet, others)
    :param expenseType: (string) the expenseType to be checked
    :return: True if expenseType is valid, False otherwise
    """
    return expenseType in expenseTypeEnum
