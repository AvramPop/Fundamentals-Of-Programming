from Test.CommandsTest import *
from Test.ExpenseTest import *
from Test.ExpenseValidationTest import *


def test():
    newExpenseTest()
    isValidAddCommandTest()
    isValidInsertCommandTest()
    isValidRemoveCommandTest()
    isValidListCommandTest()
    removeExpensesForDayTest()
    removeExpensesForExpenseTypeTest()
    removeExpensesForDaysIntervalTest()
    isCommandTest()
    isValidDayTest()
    isValidAmountTest()
    isValidExpenseTypeTest()
    addExpenseToListTest()
    print("testing done successfully")
