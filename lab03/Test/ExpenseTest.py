from BusinessLogic.Utils.RepositoryUtils import *


def test():
    newExpenseTest()
    removeExpensesForDaysIntervalTest()
    removeExpensesForExpenseTypeTest()
    removeExpensesForDayTest()
    addExpenseToListTest()
    removeExpenseFromListTest()


def newExpenseTest():
    # TODO check if exception is raised
    assert newExpense(25, 600, 'food') == {"day": 25, "amount": 600, "expenseType": "food"}


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
