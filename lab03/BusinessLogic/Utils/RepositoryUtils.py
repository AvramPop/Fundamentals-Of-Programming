from BusinessLogic.Expense import *


def populateExpensesList(expensesList):
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
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountGreaterThanList(expenseType, amount, expensesList):
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) > amount:
                expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountSmallerThanList(expenseType, amount, expensesList):
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) < amount:
                expensesWithType.append(expense)
    return expensesWithType


def expensesWithTypeWhenAmountEqualsList(expenseType, amount, expensesList):
    expensesWithType = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            if getAmount(expense) == amount:
                expensesWithType.append(expense)
    return expensesWithType


def sumOfExpensesWithExpenseType(expenseType, expensesList):
    sumOfExpensesWithType = 0
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            sumOfExpensesWithType += getAmount(expense)
    return sumOfExpensesWithType


def dayWithMaximumExpenses(expensesList):
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


def sortExpensesList(expensesForDay):
    for i in range(0, len(expensesForDay) - 1):
        for j in range(i + 1, len(expensesForDay)):
            if getAmount(expensesForDay[i]) > getAmount(expensesForDay[j]):
                expensesForDay[i], expensesForDay[j] = expensesForDay[j], expensesForDay[i]
    return expensesForDay


def expensesWithDayList(day, expensesList):
    expensesForDay = []
    for expense in expensesList:
        if getDay(expense) == day:
            expensesForDay.append(expense)
    return expensesForDay


def dailyExpensesForExpensesTypeSortedAscendingDictionary(expenseType, expensesList):
    dailyExpenses = {}
    for i in range(1, 31):
        dailyExpenses[str(i)] = []
    for expense in expensesList:
        if getExpenseType(expense) == expenseType:
            expensesForDayTemp = dailyExpenses.get(str(getDay(expense)))
            expensesForDayTemp.append(expense)
            dailyExpenses[str(getDay(expense))] = expensesForDayTemp
    for i in range(1, 31):
        expensesForDayTemp = sortExpensesList(dailyExpenses.get(str(i)))
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


def expensesWithoutBothExpenseTypeAndAmount(expenseType, amount, expensesList):
    updatedExpensesList = [expense for expense in expensesList if not (getExpenseType(expense) == expenseType and getAmount(expense) == amount)]
    return updatedExpensesList
