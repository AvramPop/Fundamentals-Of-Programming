from Validation.ExpenseValidation import *


def isValidDayTest():
    assert isValidDay(5) is True
    assert isValidDay(5.5) is False
    assert isValidDay(-30) is False
    assert isValidDay(0) is False
    assert isValidDay("sad") is False
    assert isValidDay([]) is False
    assert isValidDay(202) is False


def isValidAmountTest():
    assert isValidAmount(5) is True
    assert isValidAmount(5.5) is False
    assert isValidAmount(300) is True
    assert isValidAmount(0) is False
    assert isValidAmount("sad") is False
    assert isValidAmount([]) is False
    assert isValidAmount(-202) is False


def isValidExpenseTypeTest():
    assert isValidExpenseType("food") is True
    assert isValidExpenseType(5.5) is False
    assert isValidExpenseType(0) is False
    assert isValidExpenseType("sad") is False
    assert isValidExpenseType([]) is False
    assert isValidExpenseType(-202) is False
