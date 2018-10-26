def pushExpensesListToStack(expensesList, expensesListStack):
    expensesListStack.append(expensesList)


def popExpensesListStack(expensesListStack):
    stackLastElement = expensesListStack[-1]
    del expensesListStack[-1]
    return stackLastElement
