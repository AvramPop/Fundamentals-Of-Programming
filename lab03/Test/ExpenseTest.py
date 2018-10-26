from BusinessLogic.Utils.RepositoryUtils import *


def test():
    newExpenseTest()
    removeExpensesForDaysIntervalTest()
    removeExpensesForExpenseTypeTest()
    removeExpensesForDayTest()
    addExpenseToListTest()
    removeExpenseFromListTest()
    expensesWithTypeListTest()
    expensesWithTypeWhenAmountGreaterThanListTest()
    expensesWithTypeWhenAmountSmallerThanListTest()
    expensesWithTypeWhenAmountEqualsListTest()
    expensesWithTypeWhenAmountDifferentThanListTest()
    sumOfExpensesWithExpenseTypeTest()
    dayWithMaximumExpensesTest()
    sortExpensesListByAmountTest()
    expensesWithDayListTest()
    dailyExpensesForExpensesTypeSortedAscendingDictionaryTest()
    expenseWithoutThatWithExpenseTypeButNotAmountListTest()
    expensesWithDayInIntervalTest()


def newExpenseTest():
    # TODO check if exception is raised
    assert newExpense(25, 600, 'food') == {"day": 25, "amount": 600, "expenseType": "food"}


def expensesWithTypeWhenAmountEqualsListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 600, "food"), expensesList)
    addExpenseToList(newExpense(2, 600, "food"), expensesList)
    addExpenseToList(newExpense(3, 600, "food"), expensesList)
    addExpenseToList(newExpense(4, 500, "food"), expensesList)
    expensesList = expensesWithTypeWhenAmountEqualsList("food", 500, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(4, 500, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def expensesWithTypeWhenAmountDifferentThanListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 600, "food"), expensesList)
    addExpenseToList(newExpense(2, 600, "food"), expensesList)
    addExpenseToList(newExpense(3, 600, "food"), expensesList)
    addExpenseToList(newExpense(4, 500, "food"), expensesList)
    expensesList = expensesWithTypeWhenAmountDifferentThanList("food", 500, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(1, 600, "food"), expensesListCorrect)
    addExpenseToList(newExpense(2, 600, "food"), expensesListCorrect)
    addExpenseToList(newExpense(3, 600, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def sumOfExpensesWithExpenseTypeTest():
    expensesList = []
    addExpenseToList(newExpense(1, 600, "food"), expensesList)
    addExpenseToList(newExpense(2, 600, "food"), expensesList)
    addExpenseToList(newExpense(3, 600, "food"), expensesList)
    addExpenseToList(newExpense(4, 500, "food"), expensesList)
    sumOfExpenses = sumOfExpensesWithExpenseType("food", expensesList)
    assert sumOfExpenses == 2300


def dayWithMaximumExpensesTest():
    expensesList = []
    addExpenseToList(newExpense(1, 600, "food"), expensesList)
    addExpenseToList(newExpense(2, 600, "food"), expensesList)
    addExpenseToList(newExpense(3, 600, "food"), expensesList)
    addExpenseToList(newExpense(4, 700, "food"), expensesList)
    dayMax = dayWithMaximumExpenses(expensesList)
    assert dayMax == 4


def sortExpensesListByAmountTest():
    expensesList = []
    addExpenseToList(newExpense(1, 100, "food"), expensesList)
    addExpenseToList(newExpense(2, 50, "food"), expensesList)
    addExpenseToList(newExpense(3, 200, "food"), expensesList)
    addExpenseToList(newExpense(4, 300, "food"), expensesList)
    expensesList = sortExpensesListByAmount(expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(2, 50, "food"), expensesListCorrect)
    addExpenseToList(newExpense(1, 100, "food"), expensesListCorrect)
    addExpenseToList(newExpense(3, 200, "food"), expensesListCorrect)
    addExpenseToList(newExpense(4, 300, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def expensesWithDayListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 600, "food"), expensesList)
    addExpenseToList(newExpense(2, 600, "food"), expensesList)
    addExpenseToList(newExpense(3, 600, "food"), expensesList)
    addExpenseToList(newExpense(4, 500, "food"), expensesList)
    expensesList = expensesWithDayList(1, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(1, 600, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def dailyExpensesForExpensesTypeSortedAscendingDictionaryTest():  # TODO write test
    assert True is True


def expensesWithDayInIntervalTest():
    expensesList = []
    addExpenseToList(newExpense(1, 100, "food"), expensesList)
    addExpenseToList(newExpense(2, 50, "food"), expensesList)
    addExpenseToList(newExpense(3, 200, "food"), expensesList)
    addExpenseToList(newExpense(4, 300, "food"), expensesList)
    expensesList = expensesWithDayInInterval(1, 2, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(1, 100, "food"), expensesListCorrect)
    addExpenseToList(newExpense(2, 50, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def expenseWithoutThatWithExpenseTypeButNotAmountListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 100, "food"), expensesList)
    addExpenseToList(newExpense(2, 50, "food"), expensesList)
    addExpenseToList(newExpense(3, 200, "others"), expensesList)
    addExpenseToList(newExpense(4, 300, "others"), expensesList)
    expensesList = expenseWithoutThatWithExpenseTypeButNotAmountList("food", 50, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(2, 50, "food"), expensesListCorrect)
    addExpenseToList(newExpense(3, 200, "others"), expensesListCorrect)
    addExpenseToList(newExpense(4, 300, "others"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def expensesWithTypeListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 100, "food"), expensesList)
    addExpenseToList(newExpense(2, 50, "food"), expensesList)
    addExpenseToList(newExpense(3, 200, "food"), expensesList)
    addExpenseToList(newExpense(4, 300, "food"), expensesList)
    expensesList = expensesWithTypeList("food", expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(1, 100, "food"), expensesListCorrect)
    addExpenseToList(newExpense(2, 50, "food"), expensesListCorrect)
    addExpenseToList(newExpense(3, 200, "food"), expensesListCorrect)
    addExpenseToList(newExpense(4, 300, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect
    expensesList = []
    addExpenseToList(newExpense(1, 100, "food"), expensesList)
    addExpenseToList(newExpense(2, 50, "food"), expensesList)
    addExpenseToList(newExpense(3, 200, "food"), expensesList)
    addExpenseToList(newExpense(4, 300, "others"), expensesList)
    expensesList = expensesWithTypeList("food", expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(1, 100, "food"), expensesListCorrect)
    addExpenseToList(newExpense(2, 50, "food"), expensesListCorrect)
    addExpenseToList(newExpense(3, 200, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def expensesWithTypeWhenAmountGreaterThanListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 100, "food"), expensesList)
    addExpenseToList(newExpense(2, 50, "food"), expensesList)
    addExpenseToList(newExpense(3, 200, "food"), expensesList)
    addExpenseToList(newExpense(4, 300, "food"), expensesList)
    expensesList = expensesWithTypeWhenAmountGreaterThanList("food", 150, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(3, 200, "food"), expensesListCorrect)
    addExpenseToList(newExpense(4, 300, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def expensesWithTypeWhenAmountSmallerThanListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 100, "food"), expensesList)
    addExpenseToList(newExpense(2, 50, "food"), expensesList)
    addExpenseToList(newExpense(3, 200, "food"), expensesList)
    addExpenseToList(newExpense(4, 300, "food"), expensesList)
    expensesList = expensesWithTypeWhenAmountSmallerThanList("food", 150, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(1, 100, "food"), expensesListCorrect)
    addExpenseToList(newExpense(2, 50, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def removeExpenseFromListTest():
    expensesList = []
    addExpenseToList(newExpense(1, 600, "food"), expensesList)
    addExpenseToList(newExpense(2, 600, "food"), expensesList)
    addExpenseToList(newExpense(3, 600, "food"), expensesList)
    addExpenseToList(newExpense(4, 600, "food"), expensesList)
    expensesList = removeExpenseFromList(newExpense(4, 600, "food"), expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(1, 600, "food"), expensesListCorrect)
    addExpenseToList(newExpense(2, 600, "food"), expensesListCorrect)
    addExpenseToList(newExpense(3, 600, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def removeExpensesForDaysIntervalTest():
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "food"), expensesList)
    addExpenseToList(newExpense(30, 600, "food"), expensesList)
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    expensesList = expensesWithoutDayInIntervalList(20, 25, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(30, 600, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def removeExpensesForExpenseTypeTest():
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "clothing"), expensesList)
    addExpenseToList(newExpense(30, 600, "transport"), expensesList)
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    expensesList = expensesWithoutExpenseTypeList("food", expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(20, 600, "clothing"), expensesListCorrect)
    addExpenseToList(newExpense(30, 600, "transport"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def removeExpensesForDayTest():
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "food"), expensesList)
    addExpenseToList(newExpense(30, 600, "food"), expensesList)
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    expensesList = expensesWithoutDayList(25, expensesList)
    expensesListCorrect = []
    addExpenseToList(newExpense(20, 600, "food"), expensesListCorrect)
    addExpenseToList(newExpense(30, 600, "food"), expensesListCorrect)
    assert expensesList == expensesListCorrect


def addExpenseToListTest():
    expensesList = []
    addExpenseToList(newExpense(25, 600, "food"), expensesList)
    addExpenseToList(newExpense(20, 600, "food"), expensesList)
    expensesListCorrect = [newExpense(25, 600, "food"), newExpense(20, 600, "food")]
    assert expensesList == expensesListCorrect
