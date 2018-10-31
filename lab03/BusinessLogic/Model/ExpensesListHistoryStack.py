def pushExpensesListToStack(expensesList, expensesListStack):
    """
    Push expensesList to top of expensesListStack
    :param expensesList: (list) the list to be pushed to the top of the stack
    :param expensesListStack: (list) the stack of lists to be pushed into
    """
    expensesListStack.append(expensesList)


def popExpensesListStack(expensesListStack):
    """
    Return the top element of the stack, removing it
    :param expensesListStack: (list) the stack of lists to pop from
    :return: (list) the top element of the stack
    """
    stackLastElement = expensesListStack[-1]
    del expensesListStack[-1]
    return stackLastElement
