from Validation.ExpenseValidation import *


def isCommand(command):
    """
    Check whether the command is a valid one (one of: "add", "insert", "remove", "remove", "list", "sum", "max", "sort", "filter", "undo", "exit")
    :param command: (string) the command to be checked
    :return: True if command is valid, False otherwise
    """
    return command in commandsEnum


def isValidAddCommand(addCommand):
    """
    Check whether addCommand is a valid add command (of format: add <sum> <category>)
    :param addCommand: (string) the command to be checked
    :return: True if addCommand is a valid add command, False otherwise
    """
    if addCommand[0] != 'add':
        return False
    if len(addCommand) != 3:
        return False
    if not all(isinstance(item, str) for item in addCommand):
        return False
    if not addCommand[1].isdigit():
        return False
    return isValidAmount(int(addCommand[1])) and isValidExpenseType(addCommand[2])


def isValidInsertCommand(insertCommand):
    """
    Check whether insertCommand is a valid insert command (of format: insert <day> <sum> <category>)
    :param insertCommand: (string) the command to be checked
    :return: True if insertCommand is a valid insert command, False otherwise
    """
    if insertCommand[0] != 'insert':
        return False
    if len(insertCommand) != 4:
        return False
    if not all(isinstance(item, str) for item in insertCommand):
        return False
    if not insertCommand[1].isdigit():
        return False
    if not insertCommand[2].isdigit():
        return False
    return isValidDay(int(insertCommand[1])) and \
           isValidAmount(int(insertCommand[2])) and \
           isValidExpenseType(insertCommand[3])


def isValidRemoveCommand(removeCommand):
    """
    Check whether removeCommand is a valid remove command (of format: remove <day>, or: remove <start day> to <end day>, or remove <category>)
    :param removeCommand: (string) the command to be checked
    :return: True if removeCommand is a valid remove command, False otherwise
    """
    if removeCommand[0] != 'remove':
        return False
    if len(removeCommand) != 2 and len(removeCommand) != 4:
        return False
    if not all(isinstance(item, str) for item in removeCommand):
        return False
    elif len(removeCommand) == 4:
        if not removeCommand[1].isdigit() or not removeCommand[3].isdigit():
            return False
    elif len(removeCommand) == 2:
        if removeCommand[1].isdigit():
            if isValidDay(int(removeCommand[1])):
                return True
            else:
                return False
        else:
            return isValidExpenseType(removeCommand[1])
    if int(removeCommand[3]) <= int(removeCommand[1]):
        return False
    return isValidDay(int(removeCommand[1])) and removeCommand[2] == "to" and isValidDay(int(removeCommand[3]))


def isValidListCommand(listCommand):
    """
    Check whether listCommand is a valid list command (of format: list, or: list <category>, or list <category> [ < | = | > ] <value>)
    :param listCommand: (string) the command to be checked
    :return: True if listCommand is a valid list command, False otherwise
    """
    if listCommand[0] != 'list':
        return False
    if len(listCommand) == 1:
        return True
    if not all(isinstance(item, str) for item in listCommand):
        return False
    if len(listCommand) == 2:
        if isValidExpenseType(listCommand[1]):
            return True
        else:
            return False
    if len(listCommand) != 4:
        return False
    if not listCommand[3].isdigit():
        return False
    return isValidExpenseType(listCommand[1]) and \
           (listCommand[2] == "<" or listCommand[2] == "=" or listCommand[2] == ">") and \
           isValidAmount(int(listCommand[3]))


def isValidSumCommand(sumCommand):
    """
    Check whether sumCommand is a valid sum command (of format: sum <category>)
    :param sumCommand: (string) the command to be checked
    :return: True if sumCommand is a valid sum command, False otherwise
    """
    if len(sumCommand) != 2:
        return False
    if sumCommand[0] != 'sum':
        return False
    if len(sumCommand) == 1 or len(sumCommand) > 2:
        return False
    if not all(isinstance(item, str) for item in sumCommand):
        return False
    return isValidExpenseType(sumCommand[1])


def isValidMaxCommand(maxCommand):
    """
    Check whether maxCommand is a valid max command (of format: max <day>)
    :param maxCommand: (string) the command to be checked
    :return: True if maxCommand is a valid max command, False otherwise
    """
    if len(maxCommand) != 2:
        return False
    if maxCommand[0] != 'max':
        return False
    if not all(isinstance(item, str) for item in maxCommand):
        return False
    if not maxCommand[1].isdigit():
        return False
    return isValidDay(int(maxCommand[1]))


def isValidSortCommand(sortCommand):
    """
    Check whether sortCommand is a valid sort command (of format: sort <day>, or: sort <category>)
    :param sortCommand: (string) the command to be checked
    :return: True if sortCommand is a valid sort command, False otherwise
    """
    if len(sortCommand) != 2:
        return False
    if sortCommand[0] != 'sort':
        return False
    if len(sortCommand) == 1 or len(sortCommand) > 2:
        return False
    if not all(isinstance(item, str) for item in sortCommand):
        return False
    if sortCommand[1].isdigit():
        return isValidDay(int(sortCommand[1]))
    else:
        return isValidExpenseType(sortCommand[1])


def isValidFilterCommand(filterCommand):
    """
    Check whether filterCommand is a valid filter command (of format: filter <category>, or: filter <category> [ < | = | > ] <value>)
    :param filterCommand: (string) the command to be checked
    :return: True if filterCommand is a valid filter command, False otherwise
    """
    if filterCommand[0] != 'filter':
        return False
    if len(filterCommand) != 2 and len(filterCommand) != 4:
        return False
    if not all(isinstance(item, str) for item in filterCommand):
        return False
    if len(filterCommand) == 4:
        if not filterCommand[3].isdigit():
            return False
    return isValidExpenseType(filterCommand[1]) or \
           (isValidExpenseType(filterCommand[1]) and
            (filterCommand[2] == "<" or filterCommand[2] == "=" or filterCommand[2] == ">") and
            isValidAmount(int(filterCommand[3])))
