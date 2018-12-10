def stringsPartiallyMatch(string1, string2):
    """
    Check whether string1 and string2 match with precision over 0.6
    """
    return string2.lower() in string1.lower()
    # sequenceMatcher = SequenceMatcher(None, string1.lower(), string2.lower())
    # return sequenceMatcher.ratio() > 0.5


def sortListById(listToSort):
    """
    sort ascending list of items having getId method
    """
    for i in range(0, len(listToSort) - 1):
        for j in range(i + 1, len(listToSort)):
            if (listToSort[j]).getId() < listToSort[i].getId():
                aux = listToSort[j]
                listToSort[j] = listToSort[i]
                listToSort[i] = aux
