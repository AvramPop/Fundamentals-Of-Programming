from BusinessLogic.Model.Expense import *


def populateExpensesList(expensesList):
    """
    Populate expensesList with 10 arbitrary expenses
    :param expensesList: the list to be populated
    """
    addExpenseToList(newExpense(2, 25, "food"), expensesList)
    addExpenseToList(newExpense(20, 150, "internet"), expensesList)
    addExpenseToList(newExpense(1, 40, "others"), expensesList)
    addExpenseToList(newExpense(30, 2, "transport"), expensesList)
    addExpenseToList(newExpense(14, 1000, "food"), expensesList)
    addExpenseToList(newExpense(15, 29, "housekeeping"), expensesList)
    addExpenseToList(newExpense(16, 40, "food"), expensesList)
    addExpenseToList(newExpense(17, 250, "transport"), expensesList)
    addExpenseToList(newExpense(24, 2500, "internet"), expensesList)
    addExpenseToList(newExpense(29, 25, "others"), expensesList)
    addExpenseToList(newExpense(30, 250, "food"), expensesList)
    addExpenseToList(newExpense(2, 250, "food"), expensesList)


def expensesWithTypeList(expenseType, expensesList):
    """
    List of expenses with expenseType from expensesList
    :param expenseType: the expenseType to find expenses with
    :param expensesList: (list) the list of expenses to take expenses with expenseType from
    :return: the list containing only elements from expensesList which have expenseType
    """
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountGreaterThanList(expenseType, amount, expensesList):
    """
    List of expenses with expenseType from expensesList, if their amount is greater than amount
    :param expenseType: the expenseType to find expenses with
    :param expensesList: (list) the list of expenses to take expenses from
    :param amount: (int) the amount to compare with
    :return: the list containing only elements from expensesList which have expenseType and amount greater than amount
    """
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) > amount:
                expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountSmallerThanList(expenseType, amount, expensesList):
    """
    List of expenses with expenseType from expensesList, if their amount is smaller than amount
    :param expenseType: the expenseType to find expenses with
    :param expensesList: (list) the list of expenses to take expenses from
    :param amount: (int) the amount to compare with
    :return: the list containing only elements from expensesList which have expenseType and amount smaller than amount
    """
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) < amount:
                expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountEqualsList(expenseType, amount, expensesList):
    """
    List of expenses with expenseType from expensesList, if their amount is equal to amount
    :param expenseType: the expenseType to find expenses with
    :param expensesList: (list) the list of expenses to take expenses from
    :param amount: (int) the amount to compare with
    :return: the list containing only elements from expensesList which have expenseType and amount equal to amount
    """
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) == amount:
                expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountDifferentThanList(expenseType, amount, expensesList):
    """
    List of expenses with expenseType from expensesList, if their amount is different from amount
    :param expenseType: the expenseType to find expenses with
    :param expensesList: (list) the list of expenses to take expenses from
    :param amount: (int) the amount to compare with
    :return: the list containing only elements from expensesList which have expenseType and amount different from amount
    """
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) != amount:
                expensesWithType.append(expense)
    return expensesWithType


def sumOfExpensesWithExpenseType(expenseType, expensesList):
    """
    Sum of expenses from expensesList which have expenseType
    :param expenseType:
    :param expensesList:
    :return:
    """
    sumOfExpensesWithType = 0
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            sumOfExpensesWithType += getAmount(expense)
    return sumOfExpensesWithType


def dayWithMaximumExpenses(expensesList):
    """
    Day with maximum expenses from expensesList
    :param expensesList: list of expenses
    :return: day with maximum expenses
    """
    expensesByDay = [0] * 31
    for expense in expensesList:
        expensesByDay[getDay(expense)] += getAmount(expense)
    maximumExpense = -1
    maxDay = -1
    for i in range(1, 31):
        if expensesByDay[i] > maximumExpense:
            maximumExpense = expensesByDay[i]
            maxDay = i
    return maxDay


def sortExpensesListByAmount(expensesForDay):
    """
    Sort expensesForDay by amount
    :param expensesForDay: list of expenses for a day
    :return: the list sorted by amount
    """
    for i in range(0, len(expensesForDay) - 1):
        for j in range(i + 1, len(expensesForDay)):
            if getAmount(expensesForDay[i]) > getAmount(expensesForDay[j]):
                expensesForDay[i], expensesForDay[j] = expensesForDay[j], expensesForDay[i]
    return expensesForDay


def expensesWithDayList(day, expensesList):
    """
    List of expenses with day from expensesList
    :param day: the day to find expenses with
    :param expensesList: the list to take expenses from
    :return: list of expenses with day
    """
    expensesForDay = []
    for expense in expensesList:
        if getDay(expense) == day:
            expensesForDay.append(expense)
    return expensesForDay


def dailyExpensesForExpensesTypeSortedAscendingDictionary(expenseType, expensesList):
    """
    Dictionary having each key as a day of the month, and the value the list of expenses with expenseType for that day, sorted ascending

    :param expenseType: the expenseType to get expenses with
    :param expensesList: the list of expenses
    :return: the dictionary with each day-key corresponding to list-sorted-ascending-value
    """
    dailyExpenses = {}
    for i in range(1, 31):
        dailyExpenses[str(i)] = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            expensesForDayTemp = dailyExpenses.get(str(getDay(expense)))
            expensesForDayTemp.append(expense)
            dailyExpenses[str(getDay(expense))] = expensesForDayTemp
    for i in range(1, 31):
        expensesForDayTemp = sortExpensesListByAmount(dailyExpenses.get(str(i)))
        dailyExpenses[str(i)] = expensesForDayTemp
    return dailyExpenses


def addExpenseToList(expense, expensesList):
    """
    Add expense to expenseList
    :param expense: (dictionary) the expense to add
    :param expensesList: (list) the list to which expense should be added
    """
    expensesList.append(expense)


def expensesWithoutExpenseTypeList(expenseType, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the expense type attribute expenseType
    :param expenseType: (string) the expense type with which expenses should be popped
    :param expensesList: (list) a list of expenses
    :return: the updated list, without the elements with expenseType attribute set to expenseType
    """
    updatedExpensesList = [expense for expense in expensesList if getExpenseType(expense) != expenseType]
    return updatedExpensesList


def expensesWithoutDayList(day, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the day attribute set to day
    :param day: (int) the day with which expenses should be popped
    :param expensesList: (list) a list of expenses
    :return: the updated list, without the elements with day attribute set to day
    """
    updatedExpensesList = [expense for expense in expensesList if getDay(expense) != day]
    return updatedExpensesList


def expensesWithoutDayInIntervalList(startDay, endDay, expensesList):
    """
    Return updated expenses list without every expense from expensesList that has the day attribute set to any day in the closed interval [startDay, endDay]
    :param startDay: (int) the first day of the closed interval of days with which expenses should be popped from the list
    :param endDay: (int) the last day of the closed interval of days with which expenses should be popped from the list
    :param expensesList: (list) a list of expenses
    :return: the updated list, without the elements with day attribute in [startDay, endDay]
    """
    for day in range(startDay, endDay + 1):
        expensesList = expensesWithoutDayList(day, expensesList)
    return expensesList


def expenseWithoutThatWithExpenseTypeButNotAmountList(expenseType, amount, expensesList):
    """
    List of expenses containing al expenses from expensesList excepting that with expenseType but not amount
    :param expenseType: the expenseType for filtering
    :param amount: the amount for filtering
    :param expensesList: the list of expenses to filter
    :return: the list containing all elements in expensesList without that with expenseType but not amount
    """
    expenses = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) == amount:
                expenses.append(expense)
        else:
            expenses.append(expense)
    return expenses


def removeExpenseFromList(expense, expensesList):
    """
    Remove expense from expensesList, returning the updated list
    :param expense: the expense to remove
    :param expensesList: the list of expenses to remove expense from
    :return: the updated list
    """
    for i in range(len(expensesList) - 1, 0, -1):
        if expensesList[i] == expense:
            del expensesList[i]
            return expensesList


def expensesWithDayInInterval(startDay, endDay, expensesList):
    """
    List of expenses that have day in interval [startDay, endDay]
    :param startDay: the first day of the interval
    :param endDay: the last day of the interval
    :param expensesList: the list of expenses to take expenses from
    :return: the list containing expenses in expensesList with day in interval [startDay, endDay]
    """
    expenses = []
    for expense in expensesList:
        if startDay <= getDay(expense) <= endDay:
            expenses.append(expense)
    return expenses
