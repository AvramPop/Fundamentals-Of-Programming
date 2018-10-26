from BusinessLogic.Model.ExpensesListHistoryStack import pushExpensesListToStack, popExpensesListStack
from BusinessLogic.Utils.RepositoryUtils import *


def test():
    pushExpensesListToStackTest()
    popExpensesListStackTest()


def pushExpensesListToStackTest():
    stack = []
    expensesList = []
    addExpenseToList(newExpense(1, 600, "food"), expensesList)
    addExpenseToList(newExpense(2, 600, "food"), expensesList)
    addExpenseToList(newExpense(3, 600, "food"), expensesList)
    addExpenseToList(newExpense(4, 600, "food"), expensesList)
    pushExpensesListToStack(expensesList, stack)
    correctStack = [[newExpense(1, 600, "food"), newExpense(2, 600, "food"), newExpense(3, 600, "food"), newExpense(4, 600, "food")]]
    assert stack == correctStack


def popExpensesListStackTest():
    stack = [[newExpense(1, 600, "food"), newExpense(2, 600, "food"), newExpense(3, 600, "food"), newExpense(4, 600, "food")]]
    assert popExpensesListStack(stack) == [newExpense(1, 600, "food"), newExpense(2, 600, "food"), newExpense(3, 600, "food"), newExpense(4, 600, "food")]
    assert stack == []
    stack = [[newExpense(1, 600, "food"), newExpense(2, 600, "food"), newExpense(3, 600, "food"), newExpense(4, 600, "food")], [newExpense(1, 600, "food"), newExpense(2, 600, "food"), newExpense(3, 600, "food"), newExpense(4, 600, "transport")]]
    assert popExpensesListStack(stack) == [newExpense(1, 600, "food"), newExpense(2, 600, "food"), newExpense(3, 600, "food"), newExpense(4, 600, "transport")]
    assert stack == [[newExpense(1, 600, "food"), newExpense(2, 600, "food"), newExpense(3, 600, "food"), newExpense(4, 600, "food")]]
